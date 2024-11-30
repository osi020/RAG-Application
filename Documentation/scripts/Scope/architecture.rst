Architecture
===========

Composants Principaux
------------------

Traitement des Documents
^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

   def process_pdf(file):
       pdf = PdfReader(file)
       return " ".join(page.extract_text() for page in pdf.pages)

Vector Store
^^^^^^^^^^
- Utilisation de FAISS pour le stockage
- Embeddings via OllamaEmbeddings
- Recherche par similarité

Chaîne de Question-Réponse
^^^^^^^^^^^^^^^^^^^^^^^^
Structure du prompt :

.. code-block:: python

   prompt_template = """
   Utilisez les éléments de contexte suivants pour répondre à la question.
   Contexte : {context}
   Question : {question}
   Réponse :"""

Gestion des Sessions
-----------------
États de Session
^^^^^^^^^^^^^
- conversation_history
- vector_stores
- current_vector_store
- regenerate

Flux de Données
------------
1. Upload du document
2. Traitement et chunking
3. Génération des embeddings
4. Stockage dans FAISS
5. Recherche de similarité
6. Génération de réponse