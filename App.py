import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def show_home():
    st.subheader("Bienvenue sur l'application")
    st.write("Utilisez le menu pour naviguer entre les pages.")

def show_login():
    st.subheader("Se connecter")
    username = st.text_input("Nom d'utilisateur")
    password = st.text_input("Mot de passe", type="password")
    if st.button("Connexion"):
        st.success("Connexion réussie (fictif) !")

def show_register():
    st.subheader("Créer un compte")
    new_username = st.text_input("Nom d'utilisateur")
    new_password = st.text_input("Mot de passe", type="password")
    confirm_password = st.text_input("Confirmer le mot de passe", type="password")
    if st.button("S'inscrire"):
        if new_password == confirm_password:
            st.success("Compte créé avec succès (fictif) !")
        else:
            st.error("Les mots de passe ne correspondent pas")

def show_graph():
    st.subheader("Graphique des ventes")
    
    # Données fictives
    data = {
        "Mois": ["Jan", "Fév", "Mar", "Avr", "Mai", "Juin"],
        "Ventes": [150, 200, 250, 180, 300, 220]
    }
    df = pd.DataFrame(data)
    
    # Affichage du barplot
    fig, ax = plt.subplots()
    ax.bar(df["Mois"], df["Ventes"], color='skyblue')
    ax.set_xlabel("Mois")
    ax.set_ylabel("Ventes")
    ax.set_title("Ventes mensuelles")
    
    st.pyplot(fig)
    
    # Export des données
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("Télécharger les données", data=csv, file_name="ventes.csv", mime="text/csv")

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Aller à", ["Accueil", "Connexion", "Inscription", "Graphique"])
    
    if page == "Accueil":
        show_home()
    elif page == "Connexion":
        show_login()
    elif page == "Inscription":
        show_register()
    elif page == "Graphique":
        show_graph()

if __name__ == "__main__":
    main()