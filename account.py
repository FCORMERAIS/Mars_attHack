import streamlit as st


def show_account():
    st.title("💼 Mon Compte")
    st.markdown("### **📅 Votre emploi du temps quotidien**")
    with st.expander("🛌 Heures de sommeil et travail"):
        col1, col2 = st.columns(2)
        with col1:
            travail = st.time_input("💻 Heures de travail :")
            pause = st.time_input("☕ Temps de pause nécessaire :")
        with col2:
            sommeil = st.time_input("🕰️ Heures de sommeil :")
    with st.expander("🏋️‍♂️ Activités et déplacements"):
        col1, col2 = st.columns(2)
        with col1:
            sport = st.number_input("🏃 Séance de sport à réaliser :", min_value=0, step=1)
            transport = st.time_input("🚌 Durée moyenne des transports :")
        with col2:
            divertissement = st.time_input("🎮 Temps passé à vous divertir :")

    # Centrage du bouton avec CSS
    st.markdown(
        """
        <style>
        div.stButton > button {
            display: block;
            margin: 0 auto;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Affichage du bouton
    if st.button("💾 Enregistrer", key="save_button"):
        st.success("✅ Saisie enregistrée avec succès !")

if __name__ == "__main__":
    show_account()