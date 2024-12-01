# Document Q&A with Ollama 📚

A powerful Streamlit application that enables intelligent document querying using Local Language Models through Ollama. Upload your documents and start asking questions to get context-aware answers powered by RAG (Retrieval Augmented Generation).

![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

## ✨ Features

- 📄 Support for multiple document formats (PDF, DOCX, TXT)
- 🤖 Integration with local LLMs through Ollama
- 💬 Interactive chat interface with conversation history
- 🎯 Context-aware answers from your documents
- 🎨 Clean and intuitive user interface
- ⚙️ Customizable model parameters
- 📊 Document chunk management
- 🔄 Real-time document switching

## 🛠️ Requirements

- Python 3.7+
- Ollama (with desired models installed)
- Required Python packages:
  ```
  streamlit
  langchain-community
  langchain
  faiss-cpu
  PyPDF2
  python-docx
  requests
  ```

## 🚀 Quick Start

1. **Clone the repository**
   ```bash
    git clone https://github.com/osi020/RAG-Application.git
    cd RAG-Application

   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Install Ollama**
   - Follow the instructions at [Ollama's official website](https://ollama.ai/)
   - Install desired models (e.g., llama3.1, mistral, codellama,aya-expanse)
   ```bash
   ollama pull llama3.1
   ```

4. **Run the application**
   ```bash
   streamlit run app.py
   ```

5. **Access the web interface**
   - Open your browser and go to `http://localhost:8501`

## 💡 Usage

1. **Upload Documents**
   - Click the upload button to select your documents (PDF, DOCX, or TXT)
   - Multiple documents can be uploaded simultaneously
   - Each document will be processed and indexed automatically

2. **Configure the Model**
   - Select your preferred Ollama model from the sidebar
   - Adjust the temperature (0.0 - 1.0) to control response creativity
   - Customize chunk size and overlap for document processing

3. **Ask Questions**
   - Type your questions in the input field
   - Get AI-powered answers based on your documents' content
   - View the conversation history in the expandable section

4. **Manage Documents**
   - Switch between documents using the sidebar radio buttons
   - Clear all documents and history when needed
   - Upload additional documents at any time

## ⚙️ Configuration

### Model Parameters
- `Temperature`: Controls response randomness (0.0 = focused, 1.0 = creative)
- `Chunk Size`: Determines the size of document segments (default: 1000)
- `Chunk Overlap`: Sets the overlap between segments (default: 200)

### Supported Models
All models available in your Ollama installation are automatically detected and can be selected from the dropdown menu. Common options include:
- llama3.1
- mistral
- codellama
- aya-expanse

## 🎨 UI Customization

The application includes custom styling for a better user experience:
- Rounded buttons and input fields
- Distinct user and AI message bubbles
- Clean sidebar layout
- Modern avatar designs
- Responsive layout

## 🔧 Advanced Features

### Document Processing
- Automatic text extraction from various formats
- Intelligent chunking for optimal context retrieval
- Vector store-based similarity search
- Session-based document management

### Question-Answering System
- RAG-based response generation
- Context-aware answers
- Fallback to model knowledge when needed
- Conversation memory

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- [Streamlit](https://streamlit.io/) for the amazing web framework
- [LangChain](https://langchain.org/) for the document processing capabilities
- [Ollama](https://ollama.ai/) for local LLM integration
- All contributors and users of this project

