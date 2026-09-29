import streamlit as st

if "page" not in st.session_state:
    st.session_state.page = "accueil"

if st.session_state.page == "accueil":

    st.title("Mon application de maths")

    if st.button("Je suis élève"):
        st.session_state.page = "eleve"
        st.rerun()

    if st.button("Je suis professeur"):
        st.session_state.page = "professeur"
        st.rerun()

elif st.session_state.page == "eleve":

    st.title("Espace élève")
    st.write("Bienvenue dans ton espace élève ?")
    st.write("Que veux tu faire ?")

    if st.button("Faire un diagnostic"):
        st.session_state.page = "Faire un diagnostic"
        st.rerun()

    if st.button ("Choisir un chapitre"):
        st.session_state.page = "Choisir un chapitre"
        st.rerun()


    if st.button("Retour"):
        st.session_state.page = "accueil"
        st.rerun()

elif st.session_state.page == "professeur":

    st.title("Espace professeur")
    st.write("Cette fonctionnalité sera disponible prochainement !")

    if st.button("Retour"):
        st.session_state.page = "accueil"
        st.rerun()