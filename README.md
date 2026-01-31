# Projet LLM - Léo MAURICE

# Lien vers l'application stremlit - version de production (PROD)
Ci-dessous le lien vers mon application déployée sur le cloud.

[Lien vers l'application déployée](https://projet-rag-portfolio-eqewklspeppuwmwpge24kf.streamlit.app/)


# Lancement de l'application Streamlit en version de dévellopement (DEV)
```bash
streamlit run src/app.py
```
Si page blanche au début, veuillez attendre.
L'application est en cours de chargement.

# Techno
    - Python
    - Streamlit
    - Upstach
    - Agent ChatGPT

# Objectif général
L'objectif de ce projet est de construire un RAG à partir des informations d'un portfolio.
Un RAG est une technique qui permet d'améliorer la réponse d'un agent d'intelligence artificielle générative en la reliant à une base de données.

Il facilite la recherche d'informations parmi une grande quantité de données.

Ici, l'utilisateur doit pouvoir poser des questions sur un étudiant à l'agent IA ; celui-ci répondra à partir des données stockées dans Upstash.

# Indexation
Les données ont été extraites de mon portfolio et regroupées dans des fichiers Markdown, stockés dans le dossier `data`.

Ensuite, `src/chunk.py` permet de découper les fichiers Markdown en plusieurs chunks.
À cette fin, il utilise `MarkdownHeaderTextSplitter` de la bibliothèque `langchain_text_splitters`.
Ainsi, on obtient une liste où, pour chaque chunk, on a un tuple contenant en premier les différents titres (h1, h2) associés, et en deuxième le texte lui-même.

# Insertion des données dans Upstash
Sur Upstash, nous avons créé et configuré un index vectoriel permettant de stocker l'ensemble des données.
Le script `inserer_vecteur.py` permet d'insérer l'ensemble des chunks dans l'index Upstash.
Ainsi, pour chaque morceau de Markdown, un item est associé dans la base Upstash, contenant le texte, les métadonnées (titres h1, h2, etc.) et un vecteur qui représente le texte.
C'est ce qu'on appelle l'embedding : il permet à un programme de comprendre le sens d'un texte.

# Agent
Le script `agent.py` permet de relier l'agent conversationnel à l'index Upstash et de lui poser des questions.
On lui fournit un prompt ; à partir de celui-ci, l'agent génère un texte qu'il envoie à l'index Upstash.
Ce dernier renvoie les 5 chunks les plus pertinents par rapport au résultat. Cela fournit des éléments d'information à l'agent pour répondre à la question posée dans le prompt.
Pour trouver les 5 chunks les plus pertinents, Upstash calcule un vecteur (embedding) associé au texte envoyé par l'agent. Dans l'index, il va chercher les 5 vecteurs les plus proches et renvoie à l'agent les 5 chunks correspondants.

# Interface utilisateur Streamlit
Le script `src/app.py` génère l'application Streamlit. Elle contient une interface utilisateur qui permet d'interroger directement l'agent IA créé dans `src/agent.py`.