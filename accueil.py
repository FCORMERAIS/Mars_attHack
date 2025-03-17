import streamlit as st

def show_accueil(username):
    st.title("Bienvenue sur l'application")
    st.success(f"Bonjour {username} 👋, vous êtes connecté avec succès !")
    
    st.write("\n")
    st.write("Utilisez la barre de navigation à gauche pour accéder aux différentes sections de l'application.")
    
if __name__ == "__main__":
    show_accueil("Utilisateur")
