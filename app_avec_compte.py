import streamlit as st
import json
import os
import re
import time
import unicodedata

DOSSIER = os.path.dirname(os.path.abspath(__file__))

# Chaque entrée : identifiant -> (fichier de la leçon, fichier du quiz)
# Les leçons sont dans le dossier "lecons", les quiz dans le dossier "quiz".
FICHES = {
    "suites_rappels_suites": ("fiche_suites_rappels.md", "suites_fiche1_rappels.json"),
    "suites_monotonie": ("fiche_monotonie_suites_bornees.md", "suites_fiche2_monotonie.json"),
    "suites_convergence": ("fiche_convergence_suites.md", "suites_fiche3_convergence.json"),
    "suites_limites_suites": ("fiche_limites_suites.md", "suites_fiche4_limites.json"),
    "suites_recurrence": ("fiche_recurrence.md", "suites_fiche5_recurrence.json"),
    "suites_chapitre": (None, "suites_chapitre.json"),
    "lim_limites_fonction": ("fiche_limites_fonction.md", "lim_fiche1_limite_fonction.json"),
    "lim_comp_limites": ("fiche_composees_limites.md", "lim_fiche2_composees.json"),
    "lim_limites_calculs": ("fiche_limites_calculs.md", "lim_fiche3_calculs.json"),
    "lim_asymptotes": ("fiche_asymptotes.md", "lim_fiche4_asymptotes.json"),
    "lim_chapitre": (None, "lim_chapitre.json"),
    "esp_esp_rappels": ("fiche_espace_rappels.md", "esp_fiche1_rappels.json"),
    "esp_esp_vecteurs": ("fiche_espace_vecteurs.md", "esp_fiche2_vecteurs.json"),
    "esp_esp_param": ("fiche_espace_parametriques.md", "esp_fiche3_parametriques.json"),
    "esp_esp_ortho": ("fiche_espace_orthogonalite.md", "esp_fiche4_orthogonalite.json"),
    "esp_esp_positions": ("fiche_espace_positions_relatives.md", "esp_fiche5_positions.json"),
    "esp_chapitre": (None, "esp_chapitre.json"),
    "combi_principes": ("fiche_principes_additif_multiplicatif.md", "combi_fiche1_principes.json"),
    "combi_kuplets": ("fiche_k-uplets_permutations.md", "combi_fiche2_kuplets_permutations.json"),
    "combi_combinaisons": ("fiche_combinaisons.md", "combi_fiche3_combinaisons.json"),
    "combi_methode_denomb": ("fiche_choisir_methode_denombrement.md", "combi_fiche4_choisir_methode.json"),
    "combi_chapitre": (None, "combi_chapitre.json"),
    "cont_continuite": ("fiche_continuite.md", "cont_fiche1_continuite.json"),
    "cont_tvi": ("fiche_tvi_bijection.md", "cont_fiche2_tvi.json"),
    "cont_chapitre": (None, "cont_chapitre.json"),
    "convexite_convexite": ("fiche_convexite_concavite.md", "convexite_fiche1_convexite_concavite.json"),
    "convexite_etudier_convexite": ("fiche_etudier_convexite.md", "convexite_fiche2_etudier_convexite.json"),
    "convexite_chapitre": (None, "convexite_chapitre.json"),
    "ln_ln_proprietes": ("fiche_ln_proprietes.md", "ln_fiche1_proprietes.json"),
    "ln_ln_equations": ("fiche_ln_equations_inequations.md", "ln_fiche2_equations_inequations.json"),
    "ln_ln_etude": ("fiche_ln_etude_fonction.md", "ln_fiche3_etude_fonction.json"),
    "ln_chapitre": (None, "ln_chapitre.json"),
    "prim_prim_comprendre": ("fiche_primitives_comprendre.md", "prim_fiche1_comprendre.json"),
    "prim_prim_determiner": ("fiche_primitives_determiner.md", "prim_fiche2_determiner.json"),
    "prim_chapitre": (None, "prim_chapitre.json"),
    "comp_comp_reconnaitre": ("fiche_composees_reconnaitre.md", "comp_fiche1_reconnaitre.json"),
    "comp_comp_deriver": ("fiche_composees_deriver.md", "comp_fiche2_deriver.json"),
    "comp_chapitre": (None, "comp_chapitre.json"),
    "eqd_equadiff_comprendre": ("fiche_equadiff_comprendre.md", "eqd_fiche1_comprendre.json"),
    "eqd_equadiff_resoudre": ("fiche_equadiff_resoudre.md", "eqd_fiche2_resoudre.json"),
    "eqd_equadiff_ci": ("fiche_equadiff_condition_initiale.md", "eqd_fiche3_condition_initiale.json"),
    "eqd_chapitre": (None, "eqd_chapitre.json"),
    "int_int_comprendre": ("fiche_integrale_comprendre.md", "int_fiche1_comprendre.json"),
    "int_int_calculer": ("fiche_integrale_calculer.md", "int_fiche2_calculer.json"),
    "int_ipp": ("fiche_integration_par_parties.md", "int_fiche3_ipp.json"),
    "int_chapitre": (None, "int_chapitre.json"),
    "proba_probas_cond": ("fiche_probas_conditionnelles.md", "proba_fiche1_conditionnelles.json"),
    "proba_variables": ("fiche_variables_aleatoires.md", "proba_fiche2_variables.json"),
    "proba_binomiale": ("fiche_loi_binomiale.md", "proba_fiche3_binomiale.json"),
    "proba_chapitre": (None, "proba_chapitre.json"),
}

CHAPITRES_TERMINALE = [
    "Suites",
    "Limites de fonctions",
    "Géométrie dans l’espace",
    "Combinatoire et dénombrement",
    "Continuité/Théorème de la bijection",
    "Convexité",
    "Fonction logarithme",
    "Fonction exponentielle",
    "Primitives",
    "Fonctions composées",
    "Équations différentielles",
    "Intégrales",
    "Probabilités",
]

# Sans « Rester connecté », un élève qui revient plus de 5 minutes après
# s'être connecté avec Google est déconnecté.
DELAI_RECONNEXION = 5 * 60


# ---------- Compte élève (connexion Google + sauvegarde Supabase) ----------

@st.cache_resource
def base():
    from supabase import create_client
    return create_client(st.secrets["supabase"]["url"], st.secrets["supabase"]["key"])


def charger_profil():
    """Récupère le profil de l'élève connecté, ou le crée à sa première connexion."""
    email = st.user.email
    reponse = base().table("eleves").select("*").eq("email", email).execute()
    if reponse.data:
        profil = reponse.data[0]
        if profil.get("suivi") is None:
            profil["suivi"] = {}
        profil["rester_connecte"] = bool(profil.get("rester_connecte"))
        return profil
    profil = {"email": email, "nom": st.user.get("name", ""), "rester_connecte": False, "suivi": {}}
    base().table("eleves").insert(profil).execute()
    return profil


def sauver_profil():
    profil = st.session_state.profil
    base().table("eleves").update({
        "suivi": profil["suivi"],
        "rester_connecte": profil["rester_connecte"],
    }).eq("email", profil["email"]).execute()


def verifier_connexion():
    """À chaque nouvelle visite : charge le profil, ou déconnecte si « Rester connecté » n'est pas coché."""
    if not st.user.is_logged_in:
        st.session_state.pop("profil", None)
        return
    if "profil" in st.session_state:
        return
    profil = charger_profil()
    connecte_depuis = time.time() - st.user.get("iat", time.time())
    if not profil["rester_connecte"] and connecte_depuis > DELAI_RECONNEXION:
        st.logout()
        st.stop()
    st.session_state.profil = profil
    st.session_state.page = "eleve"


def noter_suivi(nom_fichier, titre_quiz, q, choisie):
    """Met à jour les rubriques « À revoir » / « En voie de maîtrise » après une réponse.
    erreur -> À revoir ; réussite -> En voie de maîtrise ; 2e réussite -> retirée."""
    if "profil" not in st.session_state:
        return
    suivi = st.session_state.profil["suivi"]
    cle = nom_fichier + "#" + str(q["numero"])

    if choisie["correcte"]:
        if cle not in suivi:
            return
        if suivi[cle]["statut"] == "a_revoir":
            suivi[cle]["statut"] = "en_voie"
        else:
            del suivi[cle]
    else:
        raison = choisie["feedback"] or ("Erreur sur la question : " + q["enonce"])
        suivi[cle] = {
            "statut": "a_revoir",
            "chapitre": st.session_state.get("page_chapitre", "Autre"),
            "parties": q["a_revoir"] or [titre_quiz],
            "raison": raison,
        }
    sauver_profil()


def afficher_suivi():
    suivi = st.session_state.profil["suivi"]
    rubriques = [
        ("a_revoir", "À revoir"),
        ("en_voie", "En voie de maîtrise"),
    ]
    for statut, titre in rubriques:
        st.subheader(titre)

        # chapitre -> liste de (partie, raison), sans doublons
        par_chapitre = {}
        for element in suivi.values():
            if element["statut"] != statut:
                continue
            lignes = par_chapitre.setdefault(element["chapitre"], [])
            for partie in element["parties"]:
                if (partie, element["raison"]) not in lignes:
                    lignes.append((partie, element["raison"]))

        if not par_chapitre:
            st.caption("Rien pour l'instant.")
            continue

        ordre = sorted(par_chapitre, key=lambda c: CHAPITRES_TERMINALE.index(c) if c in CHAPITRES_TERMINALE else 99)
        for chapitre in ordre:
            st.markdown("**" + chapitre + "**")
            for partie, raison in par_chapitre[chapitre]:
                if statut == "a_revoir":
                    st.caption("**" + partie + "** — " + preparer_markdown(raison))
                else:
                    st.caption("**" + partie + "** — réussie une fois, encore une bonne réponse pour la valider.")


def normaliser_nom(nom):
    """Nom de fichier simplifié : sans accents, en minuscules, espaces/tirets -> '_'."""
    nom = unicodedata.normalize("NFKD", nom)
    nom = "".join(c for c in nom if not unicodedata.combining(c))
    nom = nom.strip().lower()
    return re.sub(r"[\s_\-'’]+", "_", nom)


def trouver(nom_fichier):
    """Cherche le fichier dans le dossier de l'app et tous ses sous-dossiers.
    D'abord le nom exact, puis un nom « proche » (majuscules, accents, tirets, espaces)."""
    cible = normaliser_nom(nom_fichier)
    proche = None
    for racine, _, fichiers in os.walk(DOSSIER):
        if nom_fichier in fichiers:
            return os.path.join(racine, nom_fichier)
        if proche is None:
            for f in fichiers:
                if normaliser_nom(f) == cible:
                    proche = os.path.join(racine, f)
                    break
    if proche is not None:
        return proche
    raise FileNotFoundError("Fichier introuvable : " + nom_fichier + " (cherché dans " + DOSSIER + ")")


def lire_texte(nom_fichier):
    # "utf-8-sig" accepte aussi les fichiers enregistrés avec un BOM (fréquent sous Windows)
    with open(trouver(nom_fichier), encoding="utf-8-sig") as f:
        return f.read()


def preparer_markdown(texte):
    """Convertit les formules \\( ... \\) et \\[ ... \\] en $ ... $ et $$ ... $$ (seule syntaxe que Streamlit affiche)."""
    if texte is None:
        return ""
    texte = str(texte)
    texte = re.sub(r"\\\[(.+?)\\\]", lambda m: "$$" + m.group(1).strip() + "$$", texte, flags=re.S)
    texte = re.sub(r"\\\((.+?)\\\)", lambda m: "$" + m.group(1).strip() + "$", texte, flags=re.S)
    return texte


def afficher_lecon(nom_fichier):
    try:
        st.markdown(preparer_markdown(lire_texte(nom_fichier)))
    except FileNotFoundError as erreur:
        st.error(str(erreur))


def charger_quiz(nom_fichier):
    """Lit un quiz JSON et le remet toujours dans le même format,
    même si certaines clés manquent ou sont écrites autrement."""
    quiz = json.loads(lire_texte(nom_fichier))
    if isinstance(quiz, list):
        quiz = {"questions": quiz}

    questions = []
    for numero, q in enumerate(quiz.get("questions", [])):
        bonne = q.get("bonne_reponse", q.get("reponse"))
        options = []
        for n, o in enumerate(q.get("options", q.get("reponses", []))):
            if not isinstance(o, dict):
                o = {"texte": o}
            identifiant = str(o.get("id", "ABCDEFGHIJ"[n]))
            texte = str(o.get("texte", o.get("text", "")))
            correcte = o.get("correcte", o.get("correct"))
            if correcte is None:
                correcte = bonne is not None and str(bonne) in (identifiant, texte, identifiant + ". " + texte)
            options.append({
                "id": identifiant,
                "texte": texte,
                "correcte": bool(correcte),
                "feedback": o.get("feedback", ""),
            })

        a_revoir = q.get("a_revoir", [])
        if isinstance(a_revoir, str):
            a_revoir = [a_revoir]

        questions.append({
            # sert à reconnaître la question dans le suivi de l'élève
            "numero": q.get("id", numero),
            "enonce": q.get("enonce", q.get("question", "")),
            "figure": q.get("figure"),
            "options": options,
            "explication": q.get("explication", ""),
            "a_revoir": a_revoir,
        })

    return {
        "titre": quiz.get("titre", "Quiz"),
        "seuil_reussite": quiz.get("seuil_reussite", 50),
        "questions": questions,
    }


def afficher_quiz(nom_fichier):
    try:
        quiz = charger_quiz(nom_fichier)
    except FileNotFoundError as erreur:
        st.error(str(erreur))
        return
    except json.JSONDecodeError as erreur:
        st.error("Le fichier " + nom_fichier + " n'est pas un JSON valide : " + str(erreur))
        return

    questions = quiz["questions"]
    if not questions:
        st.warning("Ce quiz ne contient encore aucune question.")
        return

    cle = "quiz_" + nom_fichier
    if cle not in st.session_state:
        st.session_state[cle] = {"i": 0, "score": 0, "valide": False, "choix": None, "ratees": []}
    etat = st.session_state[cle]

    st.divider()
    st.subheader(quiz["titre"])

    # Fin du quiz : résultat
    if etat["i"] >= len(questions):
        score = etat["score"]
        pourcentage = round(score / len(questions) * 100)
        st.write("Ton score est :", score, "/", len(questions), "(", pourcentage, "% )")

        if pourcentage >= quiz["seuil_reussite"]:
            st.write("Bravo, tu as atteint le seuil de réussite !")
        else:
            st.write("Tu n'as pas encore atteint le seuil de réussite (", quiz["seuil_reussite"], "% ).")

        if etat["ratees"]:
            st.write("Parties à revoir :")
            a_revoir = []
            for q in etat["ratees"]:
                for partie in q["a_revoir"]:
                    if partie not in a_revoir:
                        a_revoir.append(partie)
            for partie in a_revoir:
                st.write("- " + partie)

        if st.button("Refaire le quiz", key=cle + "_refaire"):
            # on efface aussi les anciennes réponses cochées
            for k in list(st.session_state.keys()):
                if k.startswith(cle):
                    del st.session_state[k]
            st.rerun()
        return

    q = questions[etat["i"]]
    st.write("Question", etat["i"] + 1, "/", len(questions))
    st.markdown(preparer_markdown(q["enonce"]))

    if q["figure"]:
        try:
            st.image(trouver(q["figure"]))
        except FileNotFoundError as erreur:
            st.warning(str(erreur))

    options = {o["id"]: o for o in q["options"]}
    choix = st.radio(
        "Ta réponse :",
        list(options.keys()),
        format_func=lambda identifiant: identifiant + ". " + preparer_markdown(options[identifiant]["texte"]),
        index=None,
        key=cle + "_radio_" + str(etat["i"]),
        disabled=etat["valide"],
    )

    if not etat["valide"]:
        if st.button("Valider", key=cle + "_valider_" + str(etat["i"])):
            if choix is None:
                st.write("Choisis une réponse avant de valider.")
            else:
                etat["valide"] = True
                etat["choix"] = choix
                if options[choix]["correcte"]:
                    etat["score"] += 1
                else:
                    etat["ratees"].append(q)
                noter_suivi(nom_fichier, quiz["titre"], q, options[choix])
                st.rerun()
    else:
        choisie = options[etat["choix"]]
        if choisie["correcte"]:
            st.write("Bonne réponse !")
        else:
            st.write("Mauvaise réponse !")
            if choisie["feedback"]:
                st.markdown(preparer_markdown(choisie["feedback"]))
            for o in q["options"]:
                if o["correcte"]:
                    st.markdown("La bonne réponse était : **" + o["id"] + ".** " + preparer_markdown(o["texte"]))
        if q["explication"]:
            st.markdown(preparer_markdown(q["explication"]))
        if not choisie["correcte"] and q["a_revoir"]:
            st.write("À revoir :")
            for partie in q["a_revoir"]:
                st.write("- " + partie)

        if etat["i"] < len(questions) - 1:
            texte_bouton = "Question suivante"
        else:
            texte_bouton = "Voir le résultat"
        if st.button(texte_bouton, key=cle + "_suivante_" + str(etat["i"])):
            etat["i"] += 1
            etat["valide"] = False
            etat["choix"] = None
            st.rerun()


def ouvrir_fiche(identifiant):
    """Quitte la page du chapitre : leçon si elle existe, sinon directement le quiz de chapitre."""
    st.session_state.page_chapitre = st.session_state.page
    if FICHES[identifiant][0] is not None:
        st.session_state.page = "lecon"
    else:
        st.session_state.page = "quiz"
    st.rerun()

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

verifier_connexion()

if st.session_state.page == "accueil":
    st.title("Mon application de maths")

    if st.button("Je suis élève"):
        st.session_state.page = "eleve"
        st.rerun()

    if st.button("Je suis professeur"):
        st.session_state.page = "professeur"
        st.rerun()

elif st.session_state.page == "eleve" and "profil" not in st.session_state:
    st.title("Espace élève")
    st.write("Connecte-toi pour retrouver ton travail et ce qu'il te reste à revoir.")

    if st.button("Se connecter avec Google", type="primary"):
        st.login()

    if st.button("Retour"):
        st.session_state.page = "accueil"
        st.rerun()

elif st.session_state.page == "eleve":
    profil = st.session_state.profil
    st.title("Espace élève")
    st.write("Bienvenue dans ton espace élève" + (", " + profil["nom"] if profil.get("nom") else "") + " !")
    st.write("Que veux tu faire ?")

    if st.button("Faire un diagnostic"):
        st.session_state.page = "Faire un diagnostic de mon niveau"
        st.rerun()

    if st.button("Choisir un chapitre"):
        st.session_state.page = "Choisir un chapitre"
        st.rerun()

    st.divider()
    afficher_suivi()

    st.divider()
    rester = st.checkbox("Rester connecté", value=profil["rester_connecte"])
    if rester != profil["rester_connecte"]:
        profil["rester_connecte"] = rester
        sauver_profil()
    st.caption("Connecté avec " + profil["email"])
    if st.button("Se déconnecter"):
        st.session_state.clear()
        st.logout()

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
            st.session_state.exercice = 0
            st.session_state.exercice_valide = False
            st.session_state.reponses_exercices = {}
            st.session_state.page = "exercices"
            st.rerun()
        else:
            st.write("Aucune compétence ne nécessite actuellement d'exercices supplémentaires.")

elif st.session_state.page == "exercices":
    competence = st.session_state.competence_a_travailler
    st.write("Tu as l'air d'avoir des difficultés en", competence)
    st.write("Voici des exercices pour t'améliorer")

    # Doit exister AVANT le bouton "Valider" qui l'utilise
    if "reponses_exercices" not in st.session_state:
        st.session_state.reponses_exercices = {}

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
                st.session_state.reponses_exercices[st.session_state.exercice] = reponse

                if reponse == exercice["bonne_reponse"]:
                    st.write("Bonne réponse")
                else:
                    st.write("Mauvaise réponse !")
                st.session_state.exercice_valide = True
        if st.session_state.exercice_valide:
            if st.session_state.exercice < len(exercices[competence]) - 1:
                if st.button("Question suivante"):
                    st.session_state.exercice += 1
                    st.session_state.exercice_valide = False
                    st.rerun()

            else:
                if st.button("Voir les résultats"):
                    st.session_state.page = "bilan"
                    st.rerun()
    else:
        st.write("Les exercices pour cette compétence seront bientôt disponibles.")

elif st.session_state.page == "bilan":
    competence = st.session_state.competence_a_travailler
    st.title("Bilan des exercices")
    st.write("Exercices terminés, voyons tes performances !")
    score = 0
    for numero, reponse in st.session_state.reponses_exercices.items():
        exercice = exercices[competence][numero]

        st.write("Exercice", numero + 1)
        st.write("Question :", exercice["question"])
        st.write("Ta réponse :", reponse)
        st.write("Bonne réponse :", exercice["bonne_reponse"])

        if reponse == exercice["bonne_reponse"]:
            st.write("Bonne réponse !")
            score += 1
        else:
            st.write("Mauvaise réponse !")
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

        for chapitre in CHAPITRES_TERMINALE:
            if st.button(chapitre):
                st.session_state.page = chapitre
                st.rerun()

    else:
        st.write("Les chapitres de cette classe seront bientôt disponibles.")

    if st.button("Retour"):
        st.session_state.page = "Choisir un chapitre"
        st.rerun()
elif st.session_state.page == "Suites":
    st.title("Chapitre : Suites")
    st.write("Choisis une leçon :")

    if st.button("Rappels de Première : les suites"):
        st.session_state.fiche = "suites_rappels_suites"

    if st.button("Monotonie et suites bornées"):
        st.session_state.fiche = "suites_monotonie"

    if st.button("Convergence des suites"):
        st.session_state.fiche = "suites_convergence"

    if st.button("Limites de suites"):
        st.session_state.fiche = "suites_limites_suites"

    if st.button("Le raisonnement par récurrence"):
        st.session_state.fiche = "suites_recurrence"

    if st.button("Quiz de chapitre"):
        st.session_state.fiche = "suites_chapitre"

    fiche = st.session_state.get("fiche")
    if fiche is not None and fiche.startswith("suites_"):
        ouvrir_fiche(fiche)

    if st.button("Retour"):
        st.session_state.fiche = None
        st.session_state.page = "classe"
        st.rerun()
elif st.session_state.page == "Limites de fonctions":
    st.title("Chapitre : Limites de fonctions")
    st.write("Choisis une leçon :")

    if st.button("Limite d'une fonction"):
        st.session_state.fiche = "lim_limites_fonction"

    if st.button("Limites d'une fonction composée"):
        st.session_state.fiche = "lim_comp_limites"

    if st.button("Calculs de limites"):
        st.session_state.fiche = "lim_limites_calculs"

    if st.button("Asymptotes"):
        st.session_state.fiche = "lim_asymptotes"

    if st.button("Quiz de chapitre"):
        st.session_state.fiche = "lim_chapitre"

    fiche = st.session_state.get("fiche")
    if fiche is not None and fiche.startswith("lim_"):
        ouvrir_fiche(fiche)

    if st.button("Retour"):
        st.session_state.fiche = None
        st.session_state.page = "classe"
        st.rerun()
elif st.session_state.page == "Géométrie dans l’espace":
    st.title("Chapitre : Géométrie dans l’espace")
    st.write("Choisis une leçon :")

    if st.button("Rappels : vecteurs, colinéarité et produit scalaire"):
        st.session_state.fiche = "esp_esp_rappels"

    if st.button("Vecteurs dans l'espace"):
        st.session_state.fiche = "esp_esp_vecteurs"

    if st.button("Représentations paramétriques d'une droite"):
        st.session_state.fiche = "esp_esp_param"

    if st.button("Orthogonalité dans l'espace"):
        st.session_state.fiche = "esp_esp_ortho"

    if st.button("Positions relatives"):
        st.session_state.fiche = "esp_esp_positions"

    if st.button("Quiz de chapitre"):
        st.session_state.fiche = "esp_chapitre"

    fiche = st.session_state.get("fiche")
    if fiche is not None and fiche.startswith("esp_"):
        ouvrir_fiche(fiche)

    if st.button("Retour"):
        st.session_state.fiche = None
        st.session_state.page = "classe"
        st.rerun()
elif st.session_state.page == "Combinatoire et dénombrement":
    st.title("Chapitre : Combinatoire et dénombrement")
    st.write("Choisis une leçon :")

    if st.button("Principes additif et multiplicatif"):
        st.session_state.fiche = "combi_principes"

    if st.button("K-uplets et permutations"):
        st.session_state.fiche = "combi_kuplets"

    if st.button("Les combinaisons"):
        st.session_state.fiche = "combi_combinaisons"

    if st.button("Quelle méthode de dénombrement utiliser ?"):
        st.session_state.fiche = "combi_methode_denomb"

    if st.button("Quiz de chapitre"):
        st.session_state.fiche = "combi_chapitre"

    fiche = st.session_state.get("fiche")
    if fiche is not None and fiche.startswith("combi_"):
        ouvrir_fiche(fiche)

    if st.button("Retour"):
        st.session_state.fiche = None
        st.session_state.page = "classe"
        st.rerun()
elif st.session_state.page == "Continuité/Théorème de la bijection":
    st.title("Chapitre : Continuité/Théorème de la bijection")
    st.write("Choisis une leçon :")

    if st.button("La continuité"):
        st.session_state.fiche = "cont_continuite"

    if st.button("Le théorème des valeurs intermédiaires et de la bijection"):
        st.session_state.fiche = "cont_tvi"

    if st.button("Quiz de chapitre"):
        st.session_state.fiche = "cont_chapitre"

    fiche = st.session_state.get("fiche")
    if fiche is not None and fiche.startswith("cont_"):
        ouvrir_fiche(fiche)

    if st.button("Retour"):
        st.session_state.fiche = None
        st.session_state.page = "classe"
        st.rerun()
elif st.session_state.page == "Convexité":
    st.title("Chapitre : Convexité")
    st.write("Choisis une leçon :")

    if st.button("Convexité et concavité"):
        st.session_state.fiche = "convexite_convexite"

    if st.button("Étudier la convexité d'une fonction"):
        st.session_state.fiche = "convexite_etudier_convexite"

    if st.button("Quiz de chapitre"):
        st.session_state.fiche = "convexite_chapitre"

    fiche = st.session_state.get("fiche")
    if fiche is not None and fiche.startswith("convexite_"):
        ouvrir_fiche(fiche)

    if st.button("Retour"):
        st.session_state.fiche = None
        st.session_state.page = "classe"
        st.rerun()
elif st.session_state.page == "Fonction logarithme":
    st.title("Chapitre : Fonction logarithme")
    st.write("Choisis une leçon :")

    if st.button("Propriétés du logarithme népérien"):
        st.session_state.fiche = "ln_ln_proprietes"

    if st.button("Calcul avec la fonction logarithme"):
        st.session_state.fiche = "ln_ln_equations"

    if st.button("Étude de fonction logarithme"):
        st.session_state.fiche = "ln_ln_etude"

    if st.button("Quiz de chapitre"):
        st.session_state.fiche = "ln_chapitre"

    fiche = st.session_state.get("fiche")
    if fiche is not None and fiche.startswith("ln_"):
        ouvrir_fiche(fiche)

    if st.button("Retour"):
        st.session_state.fiche = None
        st.session_state.page = "classe"
        st.rerun()
elif st.session_state.page == "Fonction exponentielle":
    st.title("Chapitre : Fonction exponentielle")
    st.write("Les leçons de ce chapitre seront bientôt disponibles.")
    if st.button("Retour"):
        st.session_state.fiche = None
        st.session_state.page = "classe"
        st.rerun()
elif st.session_state.page == "Primitives":
    st.title("Chapitre : Primitives")
    st.write("Choisis une leçon :")

    if st.button("Comprendre les primitives"):
        st.session_state.fiche = "prim_prim_comprendre"

    if st.button("Déterminer une primitive"):
        st.session_state.fiche = "prim_prim_determiner"

    if st.button("Quiz de chapitre"):
        st.session_state.fiche = "prim_chapitre"

    fiche = st.session_state.get("fiche")
    if fiche is not None and fiche.startswith("prim_"):
        ouvrir_fiche(fiche)

    if st.button("Retour"):
        st.session_state.fiche = None
        st.session_state.page = "classe"
        st.rerun()
elif st.session_state.page == "Fonctions composées":
    st.title("Chapitre : Fonctions composées")
    st.write("Choisis une leçon :")

    if st.button("Reconnaître une fonction composée"):
        st.session_state.fiche = "comp_comp_reconnaitre"

    if st.button("Dériver une fonction composée"):
        st.session_state.fiche = "comp_comp_deriver"

    if st.button("Quiz de chapitre"):
        st.session_state.fiche = "comp_chapitre"

    fiche = st.session_state.get("fiche")
    if fiche is not None and fiche.startswith("comp_"):
        ouvrir_fiche(fiche)

    if st.button("Retour"):
        st.session_state.fiche = None
        st.session_state.page = "classe"
        st.rerun()
elif st.session_state.page == "Équations différentielles":
    st.title("Chapitre : Équations différentielles")
    st.write("Choisis une leçon :")

    if st.button("Comprendre ce qu'est une équation différentielle"):
        st.session_state.fiche = "eqd_equadiff_comprendre"

    if st.button("Résoudre une équation différentielle"):
        st.session_state.fiche = "eqd_equadiff_resoudre"

    if st.button("Résoudre une équation différentielle avec une condition initiale"):
        st.session_state.fiche = "eqd_equadiff_ci"

    if st.button("Quiz de chapitre"):
        st.session_state.fiche = "eqd_chapitre"

    fiche = st.session_state.get("fiche")
    if fiche is not None and fiche.startswith("eqd_"):
        ouvrir_fiche(fiche)

    if st.button("Retour"):
        st.session_state.fiche = None
        st.session_state.page = "classe"
        st.rerun()
elif st.session_state.page == "Intégrales":
    st.title("Chapitre : Intégrales")
    st.write("Choisis une leçon :")

    if st.button("Comprendre l'intégrale"):
        st.session_state.fiche = "int_int_comprendre"

    if st.button("Calculer une intégrale"):
        st.session_state.fiche = "int_int_calculer"

    if st.button("Intégration par parties"):
        st.session_state.fiche = "int_ipp"

    if st.button("Quiz de chapitre"):
        st.session_state.fiche = "int_chapitre"

    fiche = st.session_state.get("fiche")
    if fiche is not None and fiche.startswith("int_"):
        ouvrir_fiche(fiche)

    if st.button("Retour"):
        st.session_state.fiche = None
        st.session_state.page = "classe"
        st.rerun()
elif st.session_state.page == "Probabilités":
    st.title("Chapitre : Probabilités")
    st.write("Choisis une leçon :")

    if st.button("Rappels de Première : probabilités conditionnelles"):
        st.session_state.fiche = "proba_probas_cond"

    if st.button("Variables aléatoires"):
        st.session_state.fiche = "proba_variables"

    if st.button("La loi binomiale"):
        st.session_state.fiche = "proba_binomiale"

    if st.button("Quiz de chapitre"):
        st.session_state.fiche = "proba_chapitre"

    fiche = st.session_state.get("fiche")
    if fiche is not None and fiche.startswith("proba_"):
        ouvrir_fiche(fiche)

    if st.button("Retour"):
        st.session_state.fiche = None
        st.session_state.page = "classe"
        st.rerun()
elif st.session_state.page == "lecon":
    fichier_lecon, fichier_quiz = FICHES[st.session_state.fiche]
    afficher_lecon(fichier_lecon)

    st.divider()
    if st.button("Faire le quiz"):
        st.session_state.page = "quiz"
        st.rerun()

    if st.button("Retour au chapitre"):
        st.session_state.fiche = None
        st.session_state.page = st.session_state.page_chapitre
        st.rerun()
elif st.session_state.page == "quiz":
    fichier_lecon, fichier_quiz = FICHES[st.session_state.fiche]
    afficher_quiz(fichier_quiz)

    if fichier_lecon is not None:
        if st.button("Retour à la leçon"):
            st.session_state.page = "lecon"
            st.rerun()

    if st.button("Retour au chapitre"):
        st.session_state.fiche = None
        st.session_state.page = st.session_state.page_chapitre
        st.rerun()
elif st.session_state.page == "professeur":
    st.title("Espace professeur")
    st.write("Cette fonctionnalité sera disponible prochainement !")

    if st.button("Retour"):
        st.session_state.page = "accueil"
        st.rerun()
