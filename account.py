import streamlit as st

def show_account():
    st.title("Compte")
    sommeil = st.time_input("Entrez votre nombre d'heures de sommeil")
    sport =  st.number_input("Saisissez le nombre de séance de sport à réalisé par semaine")
    travail =  st.number_input("Saisissez le nombre d'heures de travail par semaine")
    pause =  st.number_input("Saisissez le temps nécessaire de votre pause")
    transport =  st.number_input("Saisissez le temps moyen passé dans les transport")
    Divertisseement =  st.text_input("Saisissez le temps moyen passé à vous divertir")


if __name__ == "__main__":
    show_account()
