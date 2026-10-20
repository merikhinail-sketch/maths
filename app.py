import streamlit as st
import json
import os
import re
import datetime
import unicodedata

import banque

st.set_page_config(page_title="CapMaths", page_icon="📐")

# Streamlit déclare ses pages « en anglais » : le navigateur propose alors de les
# traduire, ce qui abîme le texte et les formules. On déclare la page en français
# et on demande aux navigateurs de ne pas la traduire.
PAS_DE_TRADUCTION = """<script>
for (const fenetre of [window.parent, window.top]) {
  try {
    const doc = fenetre.document;
    doc.documentElement.lang = "fr";
    doc.documentElement.setAttribute("translate", "no");
    doc.documentElement.classList.add("notranslate");
    if (!doc.querySelector('meta[name="google"]')) {
      const meta = doc.createElement("meta");
      meta.name = "google";
      meta.content = "notranslate";
      doc.head.appendChild(meta);
    }
  } catch (e) {}
}
</script>"""
if hasattr(st, "iframe"):
    st.iframe(PAS_DE_TRADUCTION, height=1)
else:  # anciennes versions de Streamlit
    import streamlit.components.v1 as components
    components.html(PAS_DE_TRADUCTION, height=0)

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

# Classes proposées, et le fichier JSON du diagnostic de chacune (quand il existe)
CLASSES = ["Seconde", "Première", "Terminale"]
DIAGNOSTICS = {
    "Terminale": "diagnostic_terminale.json",
}
CLASSES_AVEC_DIAGNOSTIC = list(DIAGNOSTICS)

MOIS = ["janvier", "février", "mars", "avril", "mai", "juin", "juillet",
        "août", "septembre", "octobre", "novembre", "décembre"]


# ---------- Données de l'élève ----------
# Version de test sans compte : tout est gardé dans la session,
# donc perdu si l'élève recharge la page ou ferme l'onglet.

def profil():
    if "profil" not in st.session_state:
        st.session_state.profil = {
            "classe": None,
            "suivi": {},        # classe -> {question -> élément à revoir}
            "diagnostics": {},  # classe -> {"date": "AAAA-MM-JJ", "bilan": {...}}
        }
    return st.session_state.profil


def date_en_toutes_lettres(date):
    return str(date.day) + " " + MOIS[date.month - 1] + " " + str(date.year)


def diagnostic_possible(classe):
    """Un diagnostic par mois du calendrier (non cumulable)."""
    dernier = profil()["diagnostics"].get(classe)
    if dernier is None:
        return True
    date = datetime.date.fromisoformat(dernier["date"])
    aujourd_hui = datetime.date.today()
    return (date.year, date.month) != (aujourd_hui.year, aujourd_hui.month)


def prochain_diagnostic():
    aujourd_hui = datetime.date.today()
    if aujourd_hui.month == 12:
        return "1er janvier " + str(aujourd_hui.year + 1)
    return "1er " + MOIS[aujourd_hui.month] + " " + str(aujourd_hui.year)


# ---------- Navigation ----------
# Les boutons utilisent on_click : la fonction s'exécute AVANT que la page soit
# redessinée, donc un seul passage du programme par clic (au lieu de deux avec st.rerun).

def aller_a(page, **valeurs):
    """Change de page, en modifiant au passage d'autres valeurs de la session."""
    for cle, valeur in valeurs.items():
        st.session_state[cle] = valeur
    st.session_state.page = page


def espace_eleve_ou_classe():
    aller_a("choix_classe" if profil()["classe"] is None else "eleve")


def choisir_classe(classe):
    profil()["classe"] = classe
    if classe in CLASSES_AVEC_DIAGNOSTIC and diagnostic_possible(classe):
        aller_a("proposition_diagnostic")
    else:
        aller_a("eleve")


def commencer_diagnostic():
    aller_a("diagnostic", question=0, reponses={}, diagnostic_alerte=False)


@st.cache_data
def questions_diagnostic(classe):
    """Questions du diagnostic de la classe, lues dans son fichier JSON (même format que les quiz)."""
    return charger_quiz(DIAGNOSTICS[classe])["questions"]


def repondre_diagnostic(identifiant_option):
    st.session_state.reponses[st.session_state.question] = identifiant_option


def diagnostic_suivant():
    questions = questions_diagnostic(profil()["classe"])
    if st.session_state.question not in st.session_state.reponses:
        st.session_state.diagnostic_alerte = True
    elif st.session_state.question < len(questions) - 1:
        st.session_state.question += 1
        st.session_state.diagnostic_alerte = False
    else:
        profil()["diagnostics"][profil()["classe"]] = {
            "date": datetime.date.today().isoformat(),
            "bilan": calculer_bilan(questions, st.session_state.reponses),
        }
        aller_a("resultats")


def calculer_bilan(questions, reponses):
    """Score global et score par chapitre (le chapitre est lu dans chaque question)."""
    score = 0
    competences = {}
    for numero, reponse in reponses.items():
        q = questions[numero]
        competence = q["chapitre"] or "Autre"
        if competence not in competences:
            competences[competence] = [0, 0]
        competences[competence][1] += 1
        if any(o["id"] == reponse and o["correcte"] for o in q["options"]):
            score += 1
            competences[competence][0] += 1
    return {"score": score, "total": len(questions), "competences": competences}


def afficher_bilan(bilan):
    st.write(f"Ton score est : {bilan['score']} / {bilan['total']}")
    for competence, resultats in bilan["competences"].items():
        st.write(f"**{competence}** : {resultats[0]} / {resultats[1]}")
        pourcentage = (resultats[0] / resultats[1]) * 100

        if pourcentage == 100:
            st.write("Cette compétence est maîtrisée")
        elif pourcentage >= 50:
            st.write("À perfectionner")
        else:
            st.write("À travailler")


def noter_suivi(titre_quiz, q, choisie):
    """Met à jour les rubriques « À améliorer » / « En voie de maîtrise » après une réponse.
    erreur -> À améliorer ; réussite -> En voie de maîtrise ; 2e réussite -> retirée.
    La question est reconnue par son id : la même question est suivie de la même
    façon dans un quiz de fiche et dans la banque."""
    suivi = profil()["suivi"].setdefault(profil()["classe"], {})
    cle = str(q["numero"])

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
            "chapitre": q.get("chapitre") or st.session_state.get("page_chapitre", "Autre"),
            "parties": q["a_revoir"] or [titre_quiz],
            "raison": raison,
        }


def afficher_suivi():
    suivi = profil()["suivi"].get(profil()["classe"], {})
    rubriques = [
        ("a_revoir", "À améliorer"),
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


def normaliser_question(q, identifiant_par_defaut):
    """Remet une question JSON dans le format attendu par jouer_quiz,
    même si certaines clés manquent ou sont écrites autrement.
    Les métadonnées (chapitre, fiche, notion, niveau, type, erreurs) sont conservées."""
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
            "erreur": o.get("erreur"),
        })

    a_revoir = q.get("a_revoir", [])
    if isinstance(a_revoir, str):
        a_revoir = [a_revoir]

    return {
        # sert à reconnaître la question dans le suivi de l'élève
        "numero": q.get("id", identifiant_par_defaut),
        "enonce": q.get("enonce", q.get("question", "")),
        "figure": q.get("figure"),
        "options": options,
        "explication": q.get("explication", ""),
        "a_revoir": a_revoir,
        "chapitre": banque.nom_chapitre(q["chapitre"]) if q.get("chapitre") else None,
        "fiche": q.get("fiche"),
        "notion": q.get("notion"),
        "niveau": q.get("niveau"),
        "type": q.get("type"),
        "figure_alt": q.get("figure_alt"),
    }


def charger_quiz(nom_fichier):
    """Lit un quiz JSON et le remet toujours dans le même format."""
    quiz = json.loads(lire_texte(nom_fichier))
    if isinstance(quiz, list):
        quiz = {"questions": quiz}

    questions = [normaliser_question(q, nom_fichier + "#" + str(numero))
                 for numero, q in enumerate(quiz.get("questions", []))]

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

    jouer_quiz(quiz, "quiz_" + nom_fichier)


def jouer_quiz(quiz, cle):
    """Moteur de quiz : affichage, correction, score et bilan.
    Sert aux quiz de fiche comme aux séances tirées de la banque."""
    questions = quiz["questions"]
    if not questions:
        st.warning("Ce quiz ne contient encore aucune question.")
        return

    if cle not in st.session_state:
        st.session_state[cle] = {"i": 0, "score": 0, "valide": False, "choix": None, "ratees": []}
    etat = st.session_state[cle]

    st.divider()
    st.subheader(quiz["titre"])

    # Fin du quiz : résultat
    if etat["i"] >= len(questions):
        score = etat["score"]
        pourcentage = round(score / len(questions) * 100)
        st.write(f"Ton score est : {score} / {len(questions)} ({pourcentage} %)")

        if pourcentage >= quiz["seuil_reussite"]:
            st.write("Bravo, tu as atteint le seuil de réussite !")
        else:
            st.write(f"Tu n'as pas encore atteint le seuil de réussite ({quiz['seuil_reussite']} %).")

        if etat["ratees"]:
            st.write("Parties à revoir :")
            a_revoir = []
            for q in etat["ratees"]:
                for partie in q["a_revoir"]:
                    if partie not in a_revoir:
                        a_revoir.append(partie)
            for partie in a_revoir:
                st.write("- " + partie)

        st.button("Refaire le quiz", key=cle + "_refaire", on_click=refaire_quiz, args=(cle,))
        return

    q = questions[etat["i"]]
    st.write(f"Question {etat['i'] + 1} / {len(questions)}")
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
        st.button("Valider", key=cle + "_valider_" + str(etat["i"]),
                  on_click=valider_reponse, args=(cle, q, quiz["titre"]))
        if etat.get("alerte"):
            st.write("Choisis une réponse avant de valider.")
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
        st.button(texte_bouton, key=cle + "_suivante_" + str(etat["i"]),
                  on_click=question_suivante, args=(cle,))


def valider_reponse(cle, q, titre_quiz):
    etat = st.session_state[cle]
    choix = st.session_state.get(cle + "_radio_" + str(etat["i"]))
    if choix is None:
        etat["alerte"] = True
        return
    choisie = next(o for o in q["options"] if o["id"] == choix)
    etat["alerte"] = False
    etat["valide"] = True
    etat["choix"] = choix
    if choisie["correcte"]:
        etat["score"] += 1
    else:
        etat["ratees"].append(q)
    noter_suivi(titre_quiz, q, choisie)


def question_suivante(cle):
    etat = st.session_state[cle]
    etat["i"] += 1
    etat["valide"] = False
    etat["choix"] = None


def refaire_quiz(cle):
    # on efface aussi les anciennes réponses cochées
    for k in list(st.session_state.keys()):
        if k.startswith(cle):
            del st.session_state[k]


def ouvrir_fiche(identifiant):
    """Quitte la page du chapitre : leçon si elle existe, sinon directement le quiz de chapitre."""
    st.session_state.fiche = identifiant
    st.session_state.page_chapitre = st.session_state.page
    if FICHES[identifiant][0] is not None:
        st.session_state.page = "lecon"
    else:
        st.session_state.page = "quiz"


# ---------- Banque de quiz ----------

@st.cache_data
def questions_de_la_banque():
    return banque.charger_banque(DOSSIER)


def lancer_seance(chapitres, nb_questions):
    """Tire une nouvelle séance et la garde en mémoire : le tirage ne doit pas
    changer à chaque clic (Streamlit relance tout le programme à chaque clic)."""
    questions, _ = questions_de_la_banque()
    tirage = banque.generer_quiz(questions, chapitres, nb_questions)

    message = None
    if len(tirage) < nb_questions:
        message = ("La banque ne contient que " + str(len(tirage)) + " question(s) pour ta sélection : "
                   "ton quiz en comptera " + str(len(tirage)) + ".")

    st.session_state.numero_seance = st.session_state.get("numero_seance", 0) + 1
    st.session_state.seance = {
        "cle": "seance_" + str(st.session_state.numero_seance) + "_",
        "chapitres": chapitres,
        "nb_questions": nb_questions,
        "message": message,
        "quiz": {
            "titre": "Quiz — " + ", ".join(chapitres),
            "seuil_reussite": banque.SEUIL_REUSSITE,
            "questions": [normaliser_question(q, q["id"]) for q in tirage],
        },
    }
    st.session_state.page = "seance"


def lancer_depuis_le_choix(nb_questions):
    """Callback des boutons de format : lit le ou les chapitres choisis."""
    if st.session_state.get("banque_mode", "Un chapitre") == "Un chapitre":
        choisi = st.session_state.get("banque_un_chapitre")
        selection = [choisi] if choisi else []
    else:
        selection = list(st.session_state.get("banque_plusieurs_chapitres", []))
    if not selection:
        st.session_state.banque_alerte = True
        return
    st.session_state.banque_alerte = False
    lancer_seance(selection, nb_questions)


def afficher_choix_quiz():
    questions, avertissements = questions_de_la_banque()
    for avertissement in avertissements:
        st.warning(avertissement)

    compte = banque.compter_par_chapitre(questions)
    chapitres = [c for c in CHAPITRES_TERMINALE if c in compte]

    mode = st.radio("Type de quiz", ["Un chapitre", "Plusieurs chapitres"], horizontal=True, key="banque_mode")
    if mode == "Un chapitre":
        choisi = st.selectbox("Chapitre", chapitres, index=None,
                              placeholder="Choisis un chapitre", key="banque_un_chapitre")
        selection = [choisi] if choisi else []
    else:
        selection = st.multiselect("Chapitres (" + str(banque.MAX_CHAPITRES) + " maximum)", chapitres,
                                   max_selections=banque.MAX_CHAPITRES, placeholder="Choisis un chapitre",
                                   key="banque_plusieurs_chapitres")

    st.write("Choisis le format :")
    for format_quiz, nb_questions in banque.FORMATS.items():
        etiquette = format_quiz + " — " + str(nb_questions) + " questions"
        max_chapitres = banque.MAX_CHAPITRES_PAR_FORMAT.get(format_quiz, banque.MAX_CHAPITRES)
        disponible = format_quiz in banque.FORMATS_DISPONIBLES
        if not disponible:
            etiquette += " · Bientôt disponible"
        elif len(selection) > max_chapitres:
            disponible = False
            etiquette += " · Impossible pour plus de " + str(max_chapitres) + " chapitres"
        st.button(etiquette, disabled=not disponible, key="banque_format_" + format_quiz,
                  on_click=lancer_depuis_le_choix, args=(nb_questions,))
    if st.session_state.get("banque_alerte") and not selection:
        st.warning("Choisis au moins un chapitre.")


# Boutons de chaque page de chapitre : (texte du bouton, identifiant dans FICHES)
LECONS_PAR_CHAPITRE = {
    "Suites": [
        ("Rappels de Première : les suites", "suites_rappels_suites"),
        ("Monotonie et suites bornées", "suites_monotonie"),
        ("Convergence des suites", "suites_convergence"),
        ("Limites de suites", "suites_limites_suites"),
        ("Le raisonnement par récurrence", "suites_recurrence"),
        ("Quiz de chapitre", "suites_chapitre"),
    ],
    "Limites de fonctions": [
        ("Limite d'une fonction", "lim_limites_fonction"),
        ("Limites d'une fonction composée", "lim_comp_limites"),
        ("Calculs de limites", "lim_limites_calculs"),
        ("Asymptotes", "lim_asymptotes"),
        ("Quiz de chapitre", "lim_chapitre"),
    ],
    "Géométrie dans l’espace": [
        ("Rappels : vecteurs, colinéarité et produit scalaire", "esp_esp_rappels"),
        ("Vecteurs dans l'espace", "esp_esp_vecteurs"),
        ("Représentations paramétriques d'une droite", "esp_esp_param"),
        ("Orthogonalité dans l'espace", "esp_esp_ortho"),
        ("Positions relatives", "esp_esp_positions"),
        ("Quiz de chapitre", "esp_chapitre"),
    ],
    "Combinatoire et dénombrement": [
        ("Principes additif et multiplicatif", "combi_principes"),
        ("K-uplets et permutations", "combi_kuplets"),
        ("Les combinaisons", "combi_combinaisons"),
        ("Quelle méthode de dénombrement utiliser ?", "combi_methode_denomb"),
        ("Quiz de chapitre", "combi_chapitre"),
    ],
    "Continuité/Théorème de la bijection": [
        ("La continuité", "cont_continuite"),
        ("Le théorème des valeurs intermédiaires et de la bijection", "cont_tvi"),
        ("Quiz de chapitre", "cont_chapitre"),
    ],
    "Convexité": [
        ("Convexité et concavité", "convexite_convexite"),
        ("Étudier la convexité d'une fonction", "convexite_etudier_convexite"),
        ("Quiz de chapitre", "convexite_chapitre"),
    ],
    "Fonction logarithme": [
        ("Propriétés du logarithme népérien", "ln_ln_proprietes"),
        ("Calcul avec la fonction logarithme", "ln_ln_equations"),
        ("Étude de fonction logarithme", "ln_ln_etude"),
        ("Quiz de chapitre", "ln_chapitre"),
    ],
    "Fonction exponentielle": [],
    "Primitives": [
        ("Comprendre les primitives", "prim_prim_comprendre"),
        ("Déterminer une primitive", "prim_prim_determiner"),
        ("Quiz de chapitre", "prim_chapitre"),
    ],
    "Fonctions composées": [
        ("Reconnaître une fonction composée", "comp_comp_reconnaitre"),
        ("Dériver une fonction composée", "comp_comp_deriver"),
        ("Quiz de chapitre", "comp_chapitre"),
    ],
    "Équations différentielles": [
        ("Comprendre ce qu'est une équation différentielle", "eqd_equadiff_comprendre"),
        ("Résoudre une équation différentielle", "eqd_equadiff_resoudre"),
        ("Résoudre une équation différentielle avec une condition initiale", "eqd_equadiff_ci"),
        ("Quiz de chapitre", "eqd_chapitre"),
    ],
    "Intégrales": [
        ("Comprendre l'intégrale", "int_int_comprendre"),
        ("Calculer une intégrale", "int_int_calculer"),
        ("Intégration par parties", "int_ipp"),
        ("Quiz de chapitre", "int_chapitre"),
    ],
    "Probabilités": [
        ("Rappels de Première : probabilités conditionnelles", "proba_probas_cond"),
        ("Variables aléatoires", "proba_variables"),
        ("La loi binomiale", "proba_binomiale"),
        ("Quiz de chapitre", "proba_chapitre"),
    ],
}

if "page" not in st.session_state:
    st.session_state.page = "accueil"

if st.session_state.page == "accueil":
    st.title("CapMaths")
    st.write("Révise les maths du lycée à ton rythme : des leçons claires, des quiz corrigés pas à pas "
             "et un suivi de ce qu'il te reste à travailler.")

    st.button("Je suis élève", on_click=espace_eleve_ou_classe)
    st.button("Je suis professeur", on_click=aller_a, args=("professeur",))

elif st.session_state.page == "choix_classe":
    st.title("Choisis ta classe")

    for classe in CLASSES:
        st.button(classe, on_click=choisir_classe, args=(classe,))

    st.button("Retour", on_click=aller_a, args=("accueil" if profil()["classe"] is None else "eleve",))

elif st.session_state.page == "proposition_diagnostic":
    st.title("Diagnostic du niveau")
    nb_questions = len(questions_diagnostic(profil()["classe"]))
    st.write(f"Pour évaluer ton niveau, tu vas passer un test de {nb_questions} questions, bon courage !")

    st.button("Commencer le diagnostic", type="primary", on_click=commencer_diagnostic)
    st.button("Passer", on_click=aller_a, args=("eleve",))

elif st.session_state.page == "diagnostic":
    st.title("Diagnostic du niveau")

    questions = questions_diagnostic(profil()["classe"])
    question = questions[st.session_state.question]
    st.write(f"Question {st.session_state.question + 1} / {len(questions)}")
    st.markdown(preparer_markdown(question["enonce"]))

    # Une fois la réponse choisie, elle est fixée : les boutons sont désactivés
    choisie = st.session_state.reponses.get(st.session_state.question)

    for option in question["options"]:
        st.button(
            option["id"] + ". " + preparer_markdown(option["texte"]),
            key="diagnostic_" + str(st.session_state.question) + "_" + option["id"],
            disabled=choisie is not None,
            type="primary" if option["id"] == choisie else "secondary",
            on_click=repondre_diagnostic,
            args=(option["id"],),
        )

    if choisie is not None:
        option_choisie = next(o for o in question["options"] if o["id"] == choisie)
        if option_choisie["correcte"]:
            st.write("Bonne réponse !")
        else:
            st.write("Mauvaise réponse !")
            if option_choisie["feedback"]:
                st.markdown(preparer_markdown(option_choisie["feedback"]))
            bonne = next(o for o in question["options"] if o["correcte"])
            st.markdown("La bonne réponse était : **" + bonne["id"] + ".** " + preparer_markdown(bonne["texte"]))
        if question["explication"]:
            st.markdown(preparer_markdown(question["explication"]))

    if st.session_state.question < len(questions) - 1:
        texte_bouton = "Question suivante"
    else:
        texte_bouton = "Voir les résultats"

    st.button(texte_bouton, on_click=diagnostic_suivant)
    if st.session_state.get("diagnostic_alerte") and choisie is None:
        st.write("Choisis une réponse avant de continuer.")

elif st.session_state.page == "resultats":
    st.title("Résultats du diagnostic")
    afficher_bilan(profil()["diagnostics"][profil()["classe"]]["bilan"])

    st.button("Aller à mon espace élève", type="primary", on_click=aller_a, args=("eleve",))

elif st.session_state.page == "eleve":
    classe = profil()["classe"]
    if classe is None:
        st.session_state.page = "choix_classe"
        st.rerun()

    titre, bouton_classe = st.columns([3, 1])
    titre.title("Espace élève")
    with bouton_classe.popover(classe):
        st.button("Changer de classe ?", on_click=aller_a, args=("choix_classe",))

    lecons, quiz, diagnostic, a_revoir = st.tabs(["Leçons", "Quiz", "Diagnostic", "À améliorer"])

    with lecons:
        if classe == "Terminale":
            st.write("Choisis ton chapitre")
            for chapitre in CHAPITRES_TERMINALE:
                st.button(chapitre, on_click=aller_a, args=(chapitre,))
        else:
            st.write("Les leçons de cette classe seront bientôt disponibles.")

    with quiz:
        if classe == "Terminale":
            afficher_choix_quiz()
        else:
            st.write("La banque de quiz de cette classe sera bientôt disponible.")

    with diagnostic:
        if classe not in CLASSES_AVEC_DIAGNOSTIC:
            st.write("Le diagnostic de cette classe sera bientôt disponible.")
        else:
            dernier = profil()["diagnostics"].get(classe)
            if dernier is None:
                st.write("Tu n'as pas encore fait de diagnostic.")
            else:
                date = datetime.date.fromisoformat(dernier["date"])
                st.subheader("Dernier diagnostic : " + date_en_toutes_lettres(date))
                afficher_bilan(dernier["bilan"])

            possible = diagnostic_possible(classe)
            st.button("Faire un nouveau diagnostic", disabled=not possible, on_click=commencer_diagnostic)
            if not possible:
                st.caption("Prochain diagnostic possible à partir du " + prochain_diagnostic() + ".")

    with a_revoir:
        afficher_suivi()

    st.divider()
    st.button("Retour à l'accueil", on_click=aller_a, args=("accueil",))

elif st.session_state.page == "seance":
    seance = st.session_state.seance
    st.title("Quiz")
    if seance["message"]:
        st.info(seance["message"])

    jouer_quiz(seance["quiz"], seance["cle"])

    st.divider()
    st.button("Nouveau quiz sur les mêmes chapitres", on_click=lancer_seance,
              args=(seance["chapitres"], seance["nb_questions"]))
    st.button("Retour à l'espace élève", on_click=aller_a, args=("eleve",))

elif st.session_state.page in LECONS_PAR_CHAPITRE:
    chapitre = st.session_state.page
    st.title("Chapitre : " + chapitre)

    if LECONS_PAR_CHAPITRE[chapitre]:
        st.write("Choisis une leçon :")
        for texte, identifiant in LECONS_PAR_CHAPITRE[chapitre]:
            st.button(texte, on_click=ouvrir_fiche, args=(identifiant,))
    else:
        st.write("Les leçons de ce chapitre seront bientôt disponibles.")

    st.button("Retour", on_click=aller_a, args=("eleve",), kwargs={"fiche": None})

elif st.session_state.page == "lecon":
    fichier_lecon, fichier_quiz = FICHES[st.session_state.fiche]
    afficher_lecon(fichier_lecon)

    st.divider()
    st.button("Faire le quiz", on_click=aller_a, args=("quiz",))
    st.button("Retour au chapitre", on_click=aller_a, args=(st.session_state.page_chapitre,), kwargs={"fiche": None})

elif st.session_state.page == "quiz":
    fichier_lecon, fichier_quiz = FICHES[st.session_state.fiche]
    afficher_quiz(fichier_quiz)

    if fichier_lecon is not None:
        st.button("Retour à la leçon", on_click=aller_a, args=("lecon",))

    st.button("Retour au chapitre", on_click=aller_a, args=(st.session_state.page_chapitre,), kwargs={"fiche": None})

elif st.session_state.page == "professeur":
    st.title("Espace professeur")
    st.write("Cette fonctionnalité sera disponible prochainement !")

    st.button("Retour", on_click=aller_a, args=("accueil",))
