import streamlit as st
from langchain_community.llms import Ollama
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.chains.llm import LLMChain
from langchain.prompts import PromptTemplate
import tempfile
from PyPDF2 import PdfReader
import docx
import requests

# Configuration de la page
st.set_page_config(
    page_title="Application RAG pour Documents",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# CSS personnalisé
st.markdown("""
<style>
    .stButton>button {
        width: 100%;
        border-radius: 15px;
        height: 3em;
        background-color: #4CAF50;
        color: white;
    }
    .stTextInput>div>div>input {
        border-radius: 15px;
    }
    section[data-testid="stSidebar"] > div {
        background-color: #f5f5f5;
        padding: 2rem;
        border-radius: 15px;
        margin: 1rem;
    }
    .chat-message {
        padding: 1.5rem;
        border-radius: 15px;
        margin-bottom: 1rem;
        display: flex;
        align-items: flex-start;
        gap: 1rem;
    }
    .user-message {
        background-color: #e3f2fd;
    }
    .bot-message {
        background-color: #f5f5f5;
    }
    .avatar {
        width: 40px;
        height: 40px;
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        font-size: 20px;
    }
    .message-content {
        flex: 1;
    }
</style>
""", unsafe_allow_html=True)

def get_available_models():
    try:
        response = requests.get('http://localhost:11434/api/tags')
        return [model['name'] for model in response.json()['models']]
    except:
        return ['llama3.1', 'mistral', 'codellama']

# Initialiser les états de session
if 'conversation_history' not in st.session_state:
    st.session_state.conversation_history = []
if 'vector_stores' not in st.session_state:  
    st.session_state.vector_stores = {}
if 'current_vector_store' not in st.session_state:
    st.session_state.current_vector_store = None
if 'regenerate' not in st.session_state:
    st.session_state.regenerate = False

st.title("Conversation avec Documents via Ollama")

# Sélection du modèle
with st.sidebar:
    st.header("Configuration du Modèle")
    model_name = st.selectbox("Sélectionner le Modèle Ollama", get_available_models())
    temperature = st.slider("Température", 0.0, 1.0, 0.7)
    chunk_size = st.number_input("Taille des Chunks", 100, 2000, 1000, 100)  
    chunk_overlap = st.number_input("Chevauchement des Chunks", 0, 500, 200, 50)

def process_pdf(file):
    pdf = PdfReader(file)
    return " ".join(page.extract_text() for page in pdf.pages)

def process_docx(file):  
    doc = docx.Document(file)
    return " ".join(para.text for para in doc.paragraphs)

def process_txt(file):
    return file.getvalue().decode()

# Upload de documents
uploaded_files = st.file_uploader(
    "Uploader vos documents", 
    type=["pdf", "docx", "txt"],
    accept_multiple_files=True,
    key='document_uploader'
)

if uploaded_files:
    with st.spinner("Traitement des documents..."):
        for file in uploaded_files:
            if file.name not in st.session_state.vector_stores:
                if file.type == "application/pdf":
                    all_text = process_pdf(file)
                elif file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
                    all_text = process_docx(file)
                else:  
                    all_text = process_txt(file)

                text_splitter = RecursiveCharacterTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)
                texts = text_splitter.split_text(all_text)
                
                embeddings = OllamaEmbeddings(model=model_name)
                st.session_state.vector_stores[file.name] = FAISS.from_texts(texts, embeddings)

        st.session_state.current_vector_store = list(st.session_state.vector_stores.values())[-1]
        st.success(f"{len(uploaded_files)} documents traités en {sum(len(store.index_to_docstore_id) for store in st.session_state.vector_stores.values())} chunks.")

# Sélection de document
with st.sidebar:
    st.header("Sélection de Document")  
    document_names = list(st.session_state.vector_stores.keys())
    selected_document = st.radio("Sélectionner un document", document_names, index=len(document_names)-1 if document_names else 0)
    if selected_document in st.session_state.vector_stores:
        st.session_state.current_vector_store = st.session_state.vector_stores[selected_document]
        
    if st.button("Effacer Tous les Documents"):
        st.session_state.vector_stores = {}
        st.session_state.current_vector_store = None 
        st.session_state.conversation_history = []
        st.session_state.regenerate = True

# Chat
if st.session_state.current_vector_store is not None:
    llm = Ollama(model=model_name, temperature=temperature)
    
    prompt_template = """Utilisez les éléments de contexte suivants pour répondre à la question. 
    Si la réponse se trouve dans les documents, répondez directement. 
    Sinon, commencez par "La réponse à cette question ne se trouve pas directement dans les documents fournis. Cependant, d'après mes connaissances générales, voici ce que je peux dire :" puis complétez avec une réponse basée sur vos connaissances.

    Contexte : {context}

    Question : {question}  
    Réponse :"""

    prompt = PromptTemplate(
        template=prompt_template, input_variables=["context", "question"]  
    )
    
    chain = LLMChain(llm=llm, prompt=prompt)
    
    st.header("Posez une question sur vos documents")
    
    query = st.text_input("Entrez votre question :", key='query_input')
    
    if query:
        with st.spinner("Recherche d'une réponse..."):
            docs = st.session_state.current_vector_store.similarity_search(query)
            context = " ".join([doc.page_content for doc in docs])
            
            response = chain.run(question=query, context=context)
            
            st.session_state.conversation_history.append((query, response))
                
    if st.button("Effacer la conversation"):
        st.session_state.conversation_history = []  
        st.session_state.regenerate = True

    if st.session_state.regenerate:
        st.session_state.regenerate = False
        st.rerun()
            
    with st.expander("Historique de conversation", expanded=True):
        for i, (query, result) in enumerate(st.session_state.conversation_history):
            st.markdown(f"""
                <div class="chat-message user-message">
                    <div class="avatar" style="background-color: #e3f2fd;">👤</div>  
                    <div class="message-content">{query}</div>
                </div>
                <div class="chat-message bot-message">
                    <div class="avatar" style="background-color: #f5f5f5;">🤖</div>
                    <div class="message-content">{result}</div>  
                </div>
            """, unsafe_allow_html=True)
            
            st.markdown("---")
else:
    st.info("Veuillez uploader des documents pour commencer la conversation.")
                        
# Pied de page  
st.markdown("---")
st.caption(f"Modèle utilisé : {model_name} | Température : {temperature}")