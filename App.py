import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import time

def show_graph(name):
    st.success(f"Bonjour {name} 👋")
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
            st.rerun()
    else:
        show_graph(st.session_state.username)

if __name__ == "__main__":
    main()
