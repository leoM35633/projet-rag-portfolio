import streamlit as st
from agent import interoger_agent

st.set_page_config(page_title="Chatbot Portfolio Léo Maurice", layout="centered")


# Page de chargement
if "app_loaded" not in st.session_state: #Si l'appli est déjà en cours de lancement, on n'execute pas à ce code, à chaque envoie de prompt
    # Affiche le loader
    loading_placeholder = st.empty()
    with loading_placeholder.container():
        st.markdown("<h2 style='text-align:center;'>Application en cours de chargement...</h2>", unsafe_allow_html=True)
        with st.spinner("⏳ Veuillez patienter..."):
            import time
            time.sleep(2)  # remplace par tes initialisations réelles
    # Une fois le chargement terminé
    loading_placeholder.empty()
    st.session_state.app_loaded = True  # marque que l'app est chargée

# Chat
st.title("Chatbot Portfolio Léo Maurice")

# Initialiser l'historique des messages
if "messages" not in st.session_state:
    st.session_state.messages = []
    # Ajouter le premier message de l'assistant
    welcome_message = "Je suis un chatbot qui pourra vous renseigner sur le parcours et les projets de Léo Maurice. N'hésitez pas à me posez des questions."
    st.session_state.messages.append({"role": "assistant", "content": welcome_message})

# Afficher l'historique des messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Entrée utilisateur
if prompt := st.chat_input("Posez-moi une question…"):
    # Ajouter le message utilisateur
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Placeholder pour la réponse de l'assistant
    with st.chat_message("assistant"):
        response_placeholder = st.empty()
        # Affiche la molette pendant que l'agent réfléchit
        with st.spinner("L'assistant réfléchit..."):
            respons_agent = interoger_agent(prompt)

    # Remplacer la molette par la réponse finale
    response_placeholder.markdown(respons_agent)
    st.session_state.messages.append({"role": "assistant", "content": respons_agent})
