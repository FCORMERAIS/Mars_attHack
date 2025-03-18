import streamlit as st
import time
from accueil import show_accueil
from page1 import show_page1
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
        page = st.sidebar.radio("Aller à", ["Accueil", "Page 1", "Page 2", "Page 3", "Page 4"])
        
        if page == "Accueil":
            show_accueil(st.session_state.username)
        elif page == "Page 1":
            show_page1()
        elif page == "Page 2":
            show_page2(st.session_state.username)
        elif page == "Page 3":
            show_page3()
        elif page == "Page 4":
            show_page4()

if __name__ == "__main__":
    main()
