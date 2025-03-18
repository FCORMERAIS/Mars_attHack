import streamlit as st
import pandas as pd
import plotly.express as px
from streamlit_calendar import calendar

def show_page1():
    #  Configuration de la page
    st.title("📅 Mon Agenda Hebdomadaire")

    st.write("""
    Ajoutez et gérez vos événements avec un affichage **hebdomadaire avec horaires**.  
    Visualisez votre emploi du temps et organisez vos rendez-vous ! 
    """)

    st.markdown("---")

    #  Stockage des événements en session pour interaction dynamique
    if "events" not in st.session_state:
        st.session_state.events = [
            {"title": "Zürich design days", "start": "2025-03-19T09:00:00", "end": "2025-03-19T17:00:00", "color": "green"},
            {"title": "Customer meeting", "start": "2025-03-20T10:00:00", "end": "2025-03-20T12:00:00", "color": "blue"},
            {"title": "Focus time", "start": "2025-03-21T12:00:00", "end": "2025-03-21T15:00:00", "color": "red"},
            {"title": "Prepare workshop", "start": "2025-03-20T11:00:00", "end": "2025-03-20T12:00:00", "color": "purple"},
        ]               

    #  Vue sous forme de calendrier interactif (par SEMAINE)
    st.subheader("📆 Vue Calendrier de la Semaine")

    calendar(events=st.session_state.events, options={
        "editable": True,
        "selectable": True,
        "initialView": "timeGridWeek",  # Mode semaine
        "slotDuration": "00:30:00",  # Intervalle de 30 min par défaut
        "allDaySlot": False,  # Pas d'affichage "Journée entière"
    })

    st.markdown("---")

    #  Ajout d’un nouvel événement
    st.subheader("➕ Ajouter un événement")

    col1, col2, col3 = st.columns(3)

    with col1:
        title = st.text_input("📝 Nom de l'événement", "")

    with col2:
        date = st.date_input("📅 Date de l'événement")

    col4, col5 = st.columns(2)

    with col4:
        start_time = st.time_input("⏰ Heure de début", value=None)

    with col5:
        end_time = st.time_input("⏳ Heure de fin", value=None)

    with col3:
        color = st.color_picker("🎨 Couleur", "#0000FF")

    if st.button("Ajouter à l'agenda"):
        if title and date and start_time and end_time:
            start_datetime = f"{date}T{start_time}:00"
            end_datetime = f"{date}T{end_time}:00"

            new_event = {"title": title, "start": start_datetime, "end": end_datetime, "color": color}
            st.session_state.events.append(new_event)
            st.success(f"✅ Événement '{title}' ajouté avec succès !")
            st.rerun()

    st.markdown("---")

    # 📌 Téléchargement de l'agenda
    df_events = pd.DataFrame(st.session_state.events)
    st.download_button(
        label="📥 Télécharger mon agenda",
        data=df_events.to_csv(index=False).encode("utf-8"),
        file_name="agenda.csv",
        mime="text/csv"
    )

    # Footer
    st.caption("© 2025 - Agenda interactif en Streamlit | Créé avec ❤️")

# Permet d’exécuter cette page indépendamment si nécessaire
if __name__ == "__main__":
    show_page1()
