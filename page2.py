import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import datetime as dt
import pandas as pd
import folium
from streamlit_folium import st_folium

def show_page2(username):
    
    today = dt.datetime.now()
    next_year = today.year
    jan_1 = dt.date(next_year, 1, 1)
    dec_31 = dt.date(next_year, 12, 31)

    col1, col2, col3 = st.columns([4, 2, 4])
    
    with col1:
        d = st.date_input("📅 Sélectionner une période", (jan_1, dt.date(next_year, 1, 7)), jan_1, dec_31, format="MM.DD.YYYY",)
    
    with col3:
        activites = st.selectbox("📊 Filtrer par activité", ["Toutes","Sommeil", "Travail", "Pause", "Etude", "Sport", "Divertissement", "Préparation"])
    st.markdown("---")

    # Données simulées pour correspondre à l'image
    data = {
        "Date": ["Lun, 03 Mars", "Mar, 04 Mars", "Mer, 05 Mars", "Jeu, 06 Mars", "Ven, 07 Mars", "Sam, 08 Mars", "Dim, 09 Mars"],
        "Sommeil": [7, 7, 7, 6, 6, 9, 10],
        "Préparation": [1, 1, 1, 1, 1, 0.30, 1],
        "Travail": [7, 7, 7, 7, 7, 0, 0],
        "Pause": [1.30, 1, 1, 1.30, 1, 2, 3],
        "Transport": [2, 2, 2.30, 2, 2, 0, 1],
        "Divertissement": [3, 2.50, 3, 3, 3, 4, 5],
        "Etude": [2, 2, 2, 3, 3, 4, 4]
    }

    # Création du DataFrame
    df = pd.DataFrame(data)

    # Calcul du total time
    total_time = df.iloc[:, 1:].sum().sum()
    formatted_total_time = f"{int(total_time // 1)}:{int((total_time % 1) * 60):02d}:42"  # Format hh:mm:ss

    # Calcul du temps libre
    temps_libre = 168 - total_time 
    formatted_temps_libre = f"{int(temps_libre // 1)}:{int((temps_libre % 1) * 60):02d}:42"  # Format hh:mm:ss

    # Initialisation de la figure Plotly
    fig = go.Figure()

    # Couleurs correspondant à l'image
    colors = {
        "Sommeil": "#7FBF7F",
        "Préparation": "#7B1113",
        "Travail": "#2D67A3",
        "Pause": "#D73027",
        "Transport": "#A166AB",
        "Divertissement": "#F4A81D",
        "Etude": "#E97D3C"
    }

    # Ajout des barres empilées
    for category, color in colors.items():
        fig.add_trace(go.Bar(
            x=df["Date"], 
            y=df[category], 
            name=category, 
            marker=dict(color=color)
        ))

    # Mise en forme du graphique
    fig.update_layout(
        barmode="stack",
        title="Temps de travail par jour",
        xaxis_title="Date",
        yaxis_title="Heures",
        yaxis=dict(tickvals=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23], range=[0, 23]),
        plot_bgcolor="white",
        height=500,
        width=900
    )

    # Top section avec "Total Time" et "Top Project"
    col1, col2 = st.columns(2)

    with col1:
        st.metric(label="Temps total", value=formatted_total_time)

    with col2:
        st.metric(label="Temps libre", value=formatted_temps_libre)

    # Affichage du graphique
    st.plotly_chart(fig)

    # Données simulées
    quarters = ["Sommeil", "Travail", "Pause", "Etude", "Sport", "Divertissement", "Préparation", "Transport"]
    prevu = [56, 35, 11.30, 18, 0, 21, 7, 10]  
    realise = [52, 35, 11, 20, 0, 23.50, 6.30, 11.30]  

    # Création de la figure Plotly
    fig = go.Figure()

    # Ajout des courbes avec les bonnes couleurs
    fig.add_trace(go.Scatter(x=quarters, y=prevu, mode="lines+markers", 
                            line=dict(color="pink", width=2), marker=dict(size=8), name="Prévu"))

    fig.add_trace(go.Scatter(x=quarters, y=realise, mode="lines+markers", 
                            line=dict(color="deepskyblue", width=2), marker=dict(size=8), name="Réalisé"))

    # Mise en forme du graphique
    fig.update_layout(
        title="Temps prévu VS Temps réalisé",
        xaxis_title="Activités",
        yaxis_title="Heures",
        yaxis=dict(range=[0, 169], tickvals=[0, 24, 48, 72, 96, 25, 120, 144, 168]),
        plot_bgcolor="white",
        width=700,
        height=500
    )

    # Affichage dans Streamlit
    st.plotly_chart(fig)
    

    # --- CONFIGURATION DES DONNÉES ---
    tasks = [
        "Développement application web", "Développement application mobile", 
        "Interface Dataseaur", "Interface kelio", "Interface BO", 
        "Analyse des ventes", "Gestion collaborative du temps", "Modification du standard"
    ]

    time_spent = [7.32, 6.24, 5.49, 3.53, 3.16, 1.99, 1.89, 1.85]  # Temps en heures
    percentages = [18.07, 17.34, 15.70, 10.09, 9.03, 5.71, 5.40, 5.30]  # Pourcentages

    colors = ["#4CAF50", "#8BC34A", "#2E7D32", "#D32F2F", "#FFA000", "#FFC107", "#7B1FA2", "#D81B60"]

    # --- CRÉATION DU GRAPHIQUE EN ANNEAU ---
    fig = go.Figure(data=[go.Pie(
        labels=tasks,
        values=time_spent,
        marker=dict(colors=colors),
        hole=0.6,  # Pour effet donut
        textinfo="none"  # Supprime les labels sur le donut
    )])

    # Ajout du texte central (Total Time)
    fig.update_layout(
        title="Répartition du temps par projet",
        annotations=[dict(text="35:00:42", x=0.5, y=0.5, font_size=20, showarrow=False)],
        showlegend=False  # Supprime la légende automatique de Plotly
    )
    
    # Création de deux colonnes pour l'affichage
    col1, col2 = st.columns([2, 3])

    with col1:
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        st.subheader("Détail des temps passés sur différent projet")
        for i in range(len(tasks)):
            st.markdown(
                f"<div style='display: flex; align-items: center; padding: 5px;'>"
                f"<div style='width: 15px; height: 15px; background-color: {colors[i]}; margin-right: 10px;'></div>"
                f"<b>{tasks[i]}</b> - {time_spent[i]:.2f}h</div>",
                unsafe_allow_html=True
            )
            

    # Création de la carte
    m = folium.Map(location=[47.2184, -1.5536], zoom_start=13)

    # Ajout d'un trajet entre la gare et l'île de Nantes
    trajet = [[47.2173, -1.5428], [47.2067, -1.5555]]  # Gare de Nantes → Île de Nantes
    folium.PolyLine(trajet, color="red", weight=5, opacity=0.7).add_to(m)

    # Ajout d'un polygone autour du centre-ville
    folium.Polygon(
        locations=[[47.222, -1.561], [47.212, -1.561], [47.212, -1.545], [47.222, -1.545]],
        color="green",
        fill=True,
        fill_color="lightgreen",
        fill_opacity=0.4,
        popup="Centre-ville"
    ).add_to(m)

    # Affichage dans Streamlit
    st.markdown("<h6 style='text-align: left; color: black; font-weight: bolt;'>Lieu le plus visité et itinéaire le plus emprunté</h6>", unsafe_allow_html=True)
    st_folium(m, width=700, height=500)


if __name__ == "__main__":
    show_page2()
