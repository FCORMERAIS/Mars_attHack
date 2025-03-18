import streamlit as st

def show_amelioration():
    st.title("🔧 Améliorations")
    
    st.markdown("---")
    
    # Disposition en colonnes
    col1, col2 = st.columns(2)
    
    with col1:
        # Bloc Sommeil
        with st.container():
            st.subheader("💤 Sommeil")
            st.markdown("✅ **Objectif :** 8h/j")
            st.markdown("⚠️ **Manqué :** Mardi : 6h, Vendredi : 7h")
            st.markdown("---")
        
        # Bloc Alimentation
        with st.container():
            st.subheader("🍽️ Alimentation")
            st.markdown("✅ **Repas :** 3 repas / jour")
            st.markdown("---")
        
        # Bloc Temps libre
        with st.container():
            st.subheader("⏳ Temps libre")
            st.markdown("✅ **Disponible :** 2h/j")
    
    with col2:
        # Bloc Sport
        with st.container():
            st.subheader("🏋️ Sport")
            st.markdown("✅ **Séances :** 3 cette semaine")
            st.markdown("🕒 **Horaires recommandés :** Lundi 18h, Mercredi 19h, Samedi 10h")
            st.markdown("---")
        
        # Bloc Travail
        with st.container():
            st.subheader("💼 Travail")
            st.markdown("📅 **Réunion à décaler :** Bouger la réunion avec David le jeudi a 17h"
            " pour plus de repos")
            st.markdown("---")
        
        # Bloc Divertissement
        with st.container():
            st.subheader("🎮 Divertissement")
            st.markdown("✅ **Temps consacré :** 1h30/j")
    
    st.markdown("---")
    
    # Bloc Axes d'amélioration
    st.subheader("📈 Objectifs conseillés pour la semaine prochaine")
    st.markdown("- 💤 Respecter 8h de sommeil chaque nuit")
    st.markdown("- 🏋️ Ajouter une séance de sport supplémentaire")
    st.markdown("- 💼 Réduire la durée des réunions pour optimiser le temps libre")
