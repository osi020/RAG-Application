Installation
===========

Prérequis
--------
- Python 3.7 ou supérieur
- pip (gestionnaire de paquets Python)
- Git (pour le clonage du dépôt)
- Ollama installé et configuré

Installation des Dépendances
-------------------------
.. code-block:: bash

   git clone https://github.com/yourusername/document-qa-ollama.git
   cd document-qa-ollama
   pip install -r requirements.txt

Installation d'Ollama
------------------
1. Visitez le site officiel d'Ollama
2. Suivez les instructions d'installation pour votre système d'exploitation
3. Installez les modèles nécessaires :

.. code-block:: bash

   ollama pull llama3.1
   ollama pull mistral
   ollama pull codellama

Configuration Initiale
-------------------

1. Vérifiez que le serveur Ollama est en cours d'exécution
2. Lancez l'application :

.. code-block:: bash

   streamlit run app.py

3. Accédez à l'interface via votre navigateur à l'adresse http://localhost:8501