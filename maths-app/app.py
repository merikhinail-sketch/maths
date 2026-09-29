import streamlit as st
exercices = {
        "Limites": [
            {
                "question": "Déterminer la limite de (3x² − 5x + 2) quand x → +infini",
            "bonne_reponse": "+infini"
            },

            {
                "question": "Déterminer la limite de 2x / (x + 1) quand x → +infini",
            "bonne_reponse": "2"
            },

            {
                "question": "Déterminer la limite de (2x − 3)/(−x + 5) quand x → +infini.",
            "bonne_reponse": "-2"
            }
        ]
    }
questions = [
    {
        "question": "Déterminer la limite de (3x² - 2) / x quand x → +∞.",
        "reponses": ["A. 0", "B. +∞", "C. 3", "D. −∞"],
        "bonne_reponse": "B. +∞",
        "competence": "Limites"
    },
    {
        "question": "Déterminer la limite de 1 / x quand x → 0⁺.",
        "reponses": ["A. 0", "B. +∞", "C. −∞", "D. 1"],
        "bonne_reponse": "B. +∞",
        "competence": "Limites"
    },
    {
        "question": "Déterminer la limite de eˣ quand x → −∞.",
        "reponses": ["A. 0", "B. 1", "C. +∞", "D. −∞"],
        "bonne_reponse": "A. 0",
        "competence": "Limites"
    },
    {
        "question": "Donner la dérivée de ln(x).",
        "reponses": ["A. x", "B. 1/x", "C. x²", "D. −1/x²"],
        "bonne_reponse": "B. 1/x",
        "competence": "Dérivation"
    },
    {
        "question": "Donner la dérivée de x³.",
        "reponses": ["A. 3x²", "B. x²", "C. 3x", "D. x³"],
        "bonne_reponse": "A. 3x²",
        "competence": "Dérivation"
    },
    {
        "question": "P(A ∩ B) =",
        "reponses": [
            "A. P(A) + P(B)",
            "B. P(A)P(B)",
            "C. P(A|B)P(B)",
            "D. P(A|B) + P(B)"
        ],
        "bonne_reponse": "C. P(A|B)P(B)",
        "competence": "Probabilités"
    },
    {
        "question": "Si P(A) = 0,4, P(B) = 0,5 et P(A ∩ B) = 0,2, alors P(A|B) =",
        "reponses": ["A. 0,4", "B. 0,5", "C. 0,2", "D. 0,8"],
        "bonne_reponse": "A. 0,4",
        "competence": "Probabilités"
    },
    {
        "question": "ln(e³) =",
        "reponses": ["A. 3", "B. e³", "C. ln(3)", "D. 1"],
        "bonne_reponse": "A. 3",
        "competence": "Logarithme"
    },
    {
        "question": "ln(ab) =",
        "reponses": [
            "A. ln(a) + ln(b)",
            "B. ln(a)ln(b)",
            "C. ln(a − b)",
            "D. ln(a) + b"
        ],
        "bonne_reponse": "A. ln(a) + ln(b)",
        "competence": "Logarithme"
    },
    {
        "question": "ln(1/x) =",
        "reponses": ["A. ln(x)", "B. −ln(x)", "C. 1/ln(x)", "D. x ln(x)"],
        "bonne_reponse": "B. −ln(x)",
        "competence": "Logarithme"
    },
    {
        "question": "e⁰ =",
        "reponses": ["A. 0", "B. 1", "C. e", "D. −1"],
        "bonne_reponse": "B. 1",
        "competence": "Exponentielle"
    },
    {
        "question": "e^(a+b) =",
        "reponses": ["A. e^a + e^b", "B. e^a e^b", "C. e^(ab)", "D. a + b"],
        "bonne_reponse": "B. e^a e^b",
        "competence": "Exponentielle"
    },
    {
        "question": "La fonction eˣ est :",
        "reponses": ["A. décroissante", "B. constante", "C. croissante", "D. périodique"],
        "bonne_reponse": "C. croissante",
        "competence": "Exponentielle"
    },
    {
        "question": "Une fonction est convexe si :",
        "reponses": [
            "A. Sa dérivée est négative",
            "B. Sa dérivée seconde est positive",
            "C. Elle est bornée",
            "D. Elle est continue"
        ],
        "bonne_reponse": "B. Sa dérivée seconde est positive",
        "competence": "Convexité"
    },
    {
        "question": "Une fonction convexe vérifie :",
        "reponses": [
            "A. La courbe est au-dessus des tangentes",
            "B. La courbe est en dessous des tangentes",
            "C. Elle est toujours croissante",
            "D. Elle est toujours décroissante"
        ],
        "bonne_reponse": "A. La courbe est au-dessus des tangentes",
        "competence": "Convexité"
    },
    {
        "question": "Un vecteur normal au plan ax + by + cz + d = 0 est :",
        "reponses": [
            "A. (a,b,c)",
            "B. (b,a,c)",
            "C. (c,b,a)",
            "D. (a,c,b)"
        ],
        "bonne_reponse": "A. (a,b,c)",
        "competence": "Géométrie dans l'espace"
    },
    {
        "question": "La distance d’un point à un plan est :",
        "reponses": [
            "A. Une longueur",
            "B. Un angle",
            "C. Un vecteur",
            "D. Une aire"
        ],
        "bonne_reponse": "A. Une longueur",
        "competence": "Géométrie dans l'espace"
    },
    {
        "question": "Deux droites sont parallèles si :",
        "reponses": [
            "A. Elles ont le même point",
            "B. Leurs vecteurs directeurs sont colinéaires",
            "C. Leurs vecteurs directeurs sont orthogonaux",
            "D. Elles n’ont aucun point commun"
        ],
        "bonne_reponse": "B. Leurs vecteurs directeurs sont colinéaires",
        "competence": "Géométrie dans l'espace"
    },
    {
        "question": "∫₀¹ x dx =",
        "reponses": ["A. 1", "B. 0", "C. 1/2", "D. 1/3"],
        "bonne_reponse": "C. 1/2",
        "competence": "Intégration"
    },
    {
        "question": "Une primitive de 2x est :",
        "reponses": ["A. x²", "B. 2x²", "C. x³", "D. x²/2"],
        "bonne_reponse": "A. x²",
        "competence": "Primitives"
    }
]

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
    st.write("Bienvenue dans ton espace élève !")
    st.write("Que veux tu faire ?")

    if st.button("Faire un diagnostic"):
        st.session_state.page = "Faire un diagnostic de mon niveau"
        st.rerun()

    if st.button("Choisir un chapitre"):
        st.session_state.page = "Choisir un chapitre"
        st.rerun()

    if st.button("Retour"):
        st.session_state.page = "accueil"
        st.rerun()

elif st.session_state.page == "Faire un diagnostic de mon niveau":
    st.title("Diagnostic du niveau")
    st.write("Pour évaluer ton niveau, tu vas passer un test de 20 questions, bon courage !")

    if st.button("Continuer"):
        st.session_state.page = "Choisir une classe"
        st.rerun()

    if st.button("Retour"):
        st.session_state.page = "eleve"
        st.rerun()

elif st.session_state.page == "Choisir une classe":
    st.title("Choisis ta classe")
    classes = ["Seconde", "Première", "Terminale"]

    for classe in classes:
        if st.button(classe):
            st.session_state.classe = classe
            st.session_state.question = 0
            st.session_state.reponses = {}
            st.session_state.page = "diagnostic"
            st.rerun()

    if st.button("Retour"):
        st.session_state.page = "Faire un diagnostic de mon niveau"
        st.rerun()

elif st.session_state.page == "diagnostic":
    if st.session_state.classe == "Terminale":
        st.title("Questions")

        if "question" not in st.session_state:
            st.session_state.question = 0

        if "reponses" not in st.session_state:
            st.session_state.reponses = {}

        question = questions[st.session_state.question]
        st.write(question["question"])

        for reponse in question["reponses"]:
            if st.button(reponse):
                st.session_state.reponses[st.session_state.question] = reponse

                if reponse == question["bonne_reponse"]:
                    st.write("Bonne réponse !")
                else:
                    st.write("Mauvaise réponse !")

        if st.button("Question suivante"):
            if st.session_state.question not in st.session_state.reponses:
                st.write("Choisis une réponse avant de continuer.")

            elif st.session_state.question < len(questions) - 1:
                st.session_state.question += 1
                st.rerun()

            else:
                st.session_state.page = "resultats"
                st.rerun()
    else:
        st.write("Bientôt disponible")

    if st.button("Retour"):
        st.session_state.page = "Choisir une classe"
        st.rerun()
    
    if st.button("TEST RESULTATS"):
        st.session_state.reponses = {
            0: "A. 0",
            1: "A. 0",
            2: "B. 1",
            3: "B. 1/x",
            4: "A. 3x²",
            5: "C. P(A|B)P(B)",
            6: "A. 0,4",
            7: "A. 3",
            8: "A. ln(a) + ln(b)",
            9: "B. −ln(x)",
            10: "B. 1",
            11: "B. e^a e^b",
            12: "C. croissante",
            13: "B. Sa dérivée seconde est positive",
            14: "A. La courbe est au-dessus des tangentes",
            15: "A. (a,b,c)",
            16: "A. Une longueur",
            17: "B. Leurs vecteurs directeurs sont colinéaires",
            18: "C. 1/2",
            19: "A. x²"
            }
        st.session_state.page = "resultats"
        st.rerun()

elif st.session_state.page == "resultats":
    st.title("Résultats du diagnostic")
    score = 0

    competences = {}

    for numero, reponse in st.session_state.reponses.items():
        competence = questions[numero]["competence"]

        if competence not in competences:
            competences[competence] = [0, 0]

        competences[competence][1] += 1

        if reponse == questions[numero]["bonne_reponse"]:
            score += 1
            competences[competence][0] += 1

    st.write("Ton score est :", score, "/", len(questions))

    for competence, resultats in competences.items():
        st.write(competence, ":", resultats[0], "/", resultats[1])
        pourcentage = (resultats[0] / resultats[1]) * 100

        if pourcentage == 100:
            st.write("Cette compétence est maîtrisée")

        elif pourcentage >= 50:
            st.write("À perfectionner")

        else:
            st.write("À travailler")

    competence_a_travailler = None

    for competence, resultats in competences.items():
        pourcentage = (resultats[0] / resultats[1]) * 100

        if pourcentage < 33:
            competence_a_travailler = competence
            break

    if st.button("Voir les exercices"):
        if competence_a_travailler is not None:
            st.session_state.competence_a_travailler = competence_a_travailler
            st.session_state.page = "exercices"
            st.rerun()
        else:
            st.write("Aucune compétence ne nécessite actuellement d'exercices supplémentaires.")

elif st.session_state.page == "exercices":
    competence = st.session_state.competence_a_travailler
    st.write("Tu as l'air d'avoir des difficultés en", competence)
    st.write("Voici des exercices pour t'améliorer")

    exercices = {
        "Limites": [
            {
                "question": "Déterminer la limite de (3x² − 5x + 2) quand x → +infini",
            "bonne_reponse": "+infini"
            },

            {
                "question": "Déterminer la limite de 2x / (x + 1) quand x → +infini",
            "bonne_reponse": "2"
            },

            {
                "question": "Déterminer la limite de (2x − 3)/(−x + 5) quand x → +infini.",
            "bonne_reponse": "-2"
            }
        ]
    }
    if competence in exercices:
        if "exercice" not in st.session_state:
            st.session_state.exercice = 0
        exercice = exercices[competence][st.session_state.exercice]
        if "exercice_valide" not in st.session_state:
            st.session_state.exercice_valide = False
        st.write(exercice["question"])
        reponse = st.text_input("Ta réponse :", key=f"reponse_{st.session_state.exercice}")
        if reponse:
            if st.button("Valider"):
                if reponse == exercice["bonne_reponse"]:
                    st.write("Bonne réponse")
                else:
                    st.write("Mauvaise réponse !")
                st.session_state.exercice_valide = True
        if st.session_state.exercice_valide:
            if st.session_state.exercice < len(exercices[competence]) - 1:
                if st.button("Question suivante"):
                    st.session_state.exercice += 1
                    st.rerun()

            else:
                if st.button("Voir les résultats"):
                    st.session_state.page = "bilan"
                    st.rerun()
    else:
        st.write("Les exercices pour cette compétence seront bientôt disponibles.")
    if "reponses_exercices" not in st.session_state:
        st.session_state.reponses_exercices = {}
    st.session_state.reponses_exercices[st.session_state.exercice] = reponse
    
elif st.session_state.page == "bilan":
    competence = st.session_state.competence_a_travailler
    st.title("Bilan des exercices")
    st.write("Exercices terminés, voyons tes performances !")
    score = 0
    for numero, reponse in st.session_state.reponses_exercices.items():
        st.write("Exercice", numero + 1, ":", reponse)
        exercice = exercices[competence][numero]
        if reponse == exercice["bonne_reponse"]:
            score += 1
    st.write("Ton score est :", score, "/", len(st.session_state.reponses_exercices))
    
    
    


elif st.session_state.page == "Choisir un chapitre":
    st.write("Choisis ta classe")
    classes = ["Seconde", "Première", "Terminale"]

    for classe in classes:
        if st.button(classe):
            st.session_state.classe = classe
            st.session_state.page = "classe"
            st.rerun()
    if st.button("Retour"):
            st.session_state.page = "eleve"
            st.rerun()


elif st.session_state.page == "classe":
    if st.session_state.classe == "Terminale":
        st.write("Choisis ton chapitre")

        chapitres = [
            "Suites",
            "Limites de suites",
            "Géométrie dans l’espace",
            "Combinatoire et dénombrement",
            "Continuité/Théorème de la bijection",
            "Dérivation",
            "Convexité",
            "Fonction logarithme",
            "Fonction exponentielle",
            "Primitives",
            "Équations différentielles",
            "Intégrales",
            "Probabilités conditionnelles",
            "Variables aléatoires",
            "Loi binomiale"
        ]

        for chapitre in chapitres:
            if st.button(chapitre):
                st.session_state.page = chapitre
                st.rerun()
        
    else:
        st.write("Les chapitres de cette classe seront bientôt disponibles.")

    if st.button("Retour"):
        st.session_state.page = "Choisir un chapitre"
        st.rerun()

elif st.session_state.page == "professeur":
    st.title("Espace professeur")
    st.write("Cette fonctionnalité sera disponible prochainement !")

    if st.button("Retour"):
        st.session_state.page = "accueil"
        st.rerun()

