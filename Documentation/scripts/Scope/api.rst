API Reference
============

Fonctions Principales
------------------

process_pdf()
^^^^^^^^^^
.. code-block:: python

   def process_pdf(file):
       """
       Traite un fichier PDF et extrait son texte.
       
       Args:
           file: FileUpload object du PDF
           
       Returns:
           str: Texte extrait du PDF
       """

process_docx()
^^^^^^^^^^^
.. code-block:: python

   def process_docx(file):
       """
       Traite un fichier DOCX et extrait son texte.
       
       Args:
           file: FileUpload object du DOCX
           
       Returns:
           str: Texte extrait du DOCX
       """

Classes
------

VectorStore
^^^^^^^^^
Méthodes principales du vector store FAISS :

- similarity_search()
- add_texts()
- save_local()
- load_local()