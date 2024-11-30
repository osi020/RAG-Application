Configuration
============

Paramètres du Modèle
------------------
Temperature
^^^^^^^^^^
- Contrôle la créativité des réponses
- Plage : 0.0 à 1.0
- Recommandation : 0.7 pour un bon équilibre

Taille des Chunks
^^^^^^^^^^^^^^^
- Définit la taille des segments de document
- Valeur par défaut : 1000
- Impact sur la précision des réponses

Chevauchement des Chunks
^^^^^^^^^^^^^^^^^^^^^
- Contrôle le chevauchement entre segments
- Valeur par défaut : 200
- Améliore la cohérence des réponses

Personnalisation de l'Interface
----------------------------
Style CSS
^^^^^^^^
L'application utilise des styles personnalisés pour :

.. code-block:: css

   .stButton>button {
       width: 100%;
       border-radius: 15px;
       height: 3em;
       background-color: #4CAF50;
       color: white;
   }

Configuration des Modèles
----------------------
Modèles Supportés
^^^^^^^^^^^^^^^
- llama3.1
- mistral
- codellama

Paramètres Avancés
----------------
Vector Store
^^^^^^^^^^^
- Type : FAISS
- Dimension : selon le modèle d'embedding
- Index : L2 normalisé