"""Banque de quiz : regroupe les questions de tous les fichiers JSON du projet
et tire au hasard des séances de quiz, sans aucune question en double.

Ce module ne fait aucun affichage : il est utilisé par app.py.
Pour enrichir la banque, il suffit d'ajouter un fichier JSON (même format que
les quiz existants) dans un dossier de chapitre : il est pris en compte tout seul.
"""
import json
import os
import random

# ---------- Réglages (les modifier ici suffit) ----------

MAX_CHAPITRES = 5          # nombre maximum de chapitres dans un quiz mélangé
FORMATS = {                # nom du format -> nombre de questions
    "Rapide": 5,
    "Standard": 10,
    "Approfondi": 20,
}
FORMATS_DISPONIBLES = ["Rapide"]   # les autres formats sont affichés « Bientôt disponible »
MAX_CHAPITRES_PAR_FORMAT = {       # limite propre à un format (sinon MAX_CHAPITRES)
    "Rapide": 2,
}
SEUIL_REUSSITE = 70

# Nom du chapitre écrit dans les JSON -> nom du chapitre dans l'appli
NOMS_CHAPITRES = {
    "Combinatoire": "Combinatoire et dénombrement",
    "Continuité et théorème des valeurs intermédiaires": "Continuité/Théorème de la bijection",
    "Géométrie dans l'espace": "Géométrie dans l’espace",
    "Logarithme": "Fonction logarithme",
}


def nom_chapitre(nom_json):
    return NOMS_CHAPITRES.get(nom_json, nom_json)


def charger_banque(dossier):
    """Lit tous les fichiers JSON de quiz du dossier et de ses sous-dossiers.
    Renvoie (questions, avertissements). Chaque question garde toutes ses
    métadonnées, plus « source » (le fichier d'origine) et le chapitre de l'appli."""
    questions = []
    deja_vues = set()
    avertissements = []

    for racine, sous_dossiers, fichiers in os.walk(dossier):
        # on ignore .git, .streamlit, etc.
        sous_dossiers[:] = sorted(d for d in sous_dossiers if not d.startswith("."))
        for nom in sorted(fichiers):
            if not nom.endswith(".json"):
                continue
            try:
                with open(os.path.join(racine, nom), encoding="utf-8-sig") as f:
                    contenu = json.load(f)
            except (OSError, json.JSONDecodeError) as erreur:
                avertissements.append(nom + " ignoré : " + str(erreur))
                continue
            if not isinstance(contenu, dict) or "questions" not in contenu:
                continue
            if contenu.get("type_quiz") == "diagnostic":
                continue   # les questions du diagnostic ne vont pas dans la banque

            for q in contenu["questions"]:
                identifiant = q.get("id")
                if identifiant is None:
                    avertissements.append("Question sans « id » ignorée dans " + nom)
                    continue
                if identifiant in deja_vues:
                    avertissements.append("Question en double ignorée : " + identifiant + " (" + nom + ")")
                    continue
                deja_vues.add(identifiant)
                chapitre = nom_chapitre(q.get("chapitre") or contenu.get("chapitre") or "Autre")
                questions.append(dict(q, chapitre=chapitre, source=nom))

    return questions, avertissements


def compter_par_chapitre(questions):
    compte = {}
    for q in questions:
        compte[q["chapitre"]] = compte.get(q["chapitre"], 0) + 1
    return compte


def repartir(nb_questions, disponibles, hasard=random):
    """Répartit nb_questions entre les chapitres de façon équilibrée.
    disponibles : {chapitre: nombre de questions dans la banque}.
    On distribue une question par chapitre à chaque tour (ordre tiré au hasard
    pour le reste), sans jamais dépasser ce qu'un chapitre contient."""
    parts = {chapitre: 0 for chapitre in disponibles}
    restant = min(nb_questions, sum(disponibles.values()))
    while restant > 0:
        ouverts = [c for c in parts if parts[c] < disponibles[c]]
        hasard.shuffle(ouverts)
        for chapitre in ouverts:
            if restant == 0:
                break
            parts[chapitre] += 1
            restant -= 1
    return parts


def melanger_options(q, hasard=random):
    """Copie de la question avec les options dans un ordre aléatoire
    (sauf si « melanger_options » vaut false), renommées A, B, C, D."""
    options = list(q.get("options", []))
    if q.get("melanger_options", True):
        hasard.shuffle(options)
    lettres = "ABCDEFGHIJ"
    return dict(q, options=[dict(o, id=lettres[n]) for n, o in enumerate(options)])


def generer_quiz(questions, chapitres, nb_questions, hasard=random):
    """Tire au hasard nb_questions questions (ou moins si la banque n'en a pas
    assez) dans les chapitres demandés, équilibrées entre chapitres, sans doublon."""
    par_chapitre = {c: [q for q in questions if q["chapitre"] == c] for c in chapitres}
    parts = repartir(nb_questions, {c: len(liste) for c, liste in par_chapitre.items()}, hasard)

    tirage = []
    for chapitre, nombre in parts.items():
        tirage += hasard.sample(par_chapitre[chapitre], nombre)
    hasard.shuffle(tirage)
    return [melanger_options(q, hasard) for q in tirage]
