import streamlit as st
import time

from pages.Accueil import show_accueil
from pages.Calendrier import show_calendrier
from pages.Amlioration import show_amelioration
from pages.Dashboard import show_dashboard
from pages.account import show_account

def main():
    nav_image_url = "https://cdn-icons-png.flaticon.com/128/1738/1738691.png"

    if "username" not in st.session_state:
        st.session_state.username = ""
    
    if st.session_state.username == "":
        st.subheader("Connexion")
        username = st.text_input("Entrez votre nom")
        password = st.text_input("Mot de passe", type="password")
        if st.button("Se connecter"):
            st.success("Connexion réussie !")
            time.sleep(1)
            st.session_state.username = username
            st.session_state.page = "Accueil"
            st.rerun()
    else:
        st.sidebar.markdown(f'<img src="{nav_image_url}" width="100" style="display: block; margin-left: auto; margin-right: auto;">', unsafe_allow_html=True)

        
        st.sidebar.markdown("---")
        if st.sidebar.button("🏠 Accueil", use_container_width=True):
            st.session_state.page = "Accueil"
        if st.sidebar.button("🚀 Amélioration", use_container_width=True):
            st.session_state.page = "Amelioration"
        if st.sidebar.button("📅 Calendrier", use_container_width=True):
            st.session_state.page = "Calendrier"
        if st.sidebar.button("📊 Tableaux de bord", use_container_width=True):
            st.session_state.page = "Tableaux de bord"
        if st.sidebar.button("👤 Compte", use_container_width=True):
            st.session_state.page = "Compte"
        # Bouton Déconnexion avec redirection vers Connexion
        if st.sidebar.button("🔓 Déconnexion", use_container_width=True):
            st.session_state.username = ""
            st.session_state.page = "Connexion"
            st.rerun()
        
        page = st.session_state.get("page", "Accueil")
        
        if page == "Accueil":
            show_accueil(st.session_state.username)
        elif page == "Amelioration":
            show_amelioration()
        elif page ==  "Tableaux de bord":
            show_dashboard(st.session_state.username)
        elif page == "Calendrier":
            show_calendrier()
        elif page == "Compte":
            show_account()

if __name__ == "__main__":
    main()
