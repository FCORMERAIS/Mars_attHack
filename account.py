import streamlit as st

def show_account():
    st.title("Compte")
    sommeil = st.time_input("Heures de sommeil:")
    sport =  st.number_input("Séance de sport à réalisé:")
    travail =  st.number_input("Heures de travail:")
    pause =  st.number_input("Temps de pause nécessaire:")
    transport =  st.number_input("Durée moyenne passé dans les transport:")
    divertissement =  st.text_input("Temps passé à vous divertir")

if __name__ == "__main__":
    show_account()
