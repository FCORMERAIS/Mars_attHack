import streamlit as st
import time
from accueil import show_accueil
from page1 import show_amelioration
from page2 import show_page2
from page3 import show_page3
from page4 import show_page4

def main():
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
        st.sidebar.title("Navigation")
        
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
        
        page = st.session_state.get("page", "Accueil")
        
        if page == "Accueil":
            show_accueil(st.session_state.username)
        elif page == "Amelioration":
            show_amelioration()
        elif page == "Calendrier":
            show_page2()
        elif page == "Tableaux de bord":
            show_page3()
        elif page == "Compte":
            show_page4()

if __name__ == "__main__":
    main()
