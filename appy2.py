import streamlit as st
import streamlit_authenticator as stauth
from streamlit_option_menu import option_menu

# --- Données utilisateurs ---
lesDonneesDesComptes = {
    'usernames': {
        'utilisateur': {
            'name': 'Utilisateur',
            'password': 'utilisateurMDP',
            'email': 'utilisateur@gmail.com',
        },
        'admin': {
            'name': 'Administrateur',
            'password': 'adminMDP',
            'email': 'admin@gmail.com',
        }
    }
}

# --- Création de l’authentificateur ---
authenticator = stauth.Authenticate(
    credentials=lesDonneesDesComptes,
    cookie_name="cookie_name",
    key="key",
    cookie_expiry_days=30
)

# --- Formulaire de connexion ---
authenticator.login()

# --- Si l'utilisateur est connecté ---
if st.session_state["authentication_status"]:
    st.sidebar.title(f"Bienvenue {st.session_state['name']} 👋")

    # Bouton de déconnexion
    if st.sidebar.button("🔒 Se déconnecter"):
        authenticator.logout("Déconnexion", "sidebar")
        st.success("Vous avez été déconnecté.")
        st.experimental_rerun()

    # Menu de navigation
    selection = option_menu(
        menu_title="Menu",
        options=["Accueil", "Photos"],
        icons=["house", "image"],
        menu_icon="cast",
        default_index=0
    )

    # Pages conditionnelles
    if selection == "Accueil":
        st.title("🏡 Accueil")
        st.write("Bienvenue dans votre espace sécurisé !")
    elif selection == "Photos":
        st.title("📸 Galerie de photos")
        col1, col2, col3 = st.columns(3)
        with col1:
            st.image("https://static.streamlit.io/examples/cat.jpg", caption="Un chat")
        with col2:
            st.image("https://static.streamlit.io/examples/dog.jpg", caption="Un chien")
        with col3:
            st.image("https://static.streamlit.io/examples/owl.jpg", caption="Un hibou")

# --- Gestion des erreurs ---
elif st.session_state["authentication_status"] is False:
    st.error("Nom d'utilisateur ou mot de passe incorrect.")
elif st.session_state["authentication_status"] is None:
    st.warning("Veuillez entrer vos identifiants.")
