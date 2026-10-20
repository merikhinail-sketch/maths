# Résoudre une équation différentielle avec une condition initiale

Une équation différentielle a une infinité de solutions, car la constante $C$ reste libre. Une **condition initiale** donne un point de passage de la courbe : elle fixe $C$, et il ne reste alors qu'**une seule** solution.

---

## 1. Utiliser une condition initiale

Une condition initiale s'écrit sous la forme $y(x_0) = y_0$ : lorsque $x = x_0$, la fonction vaut $y_0$.

Par exemple, $y(0) = 5$ signifie que pour $x = 0$, la fonction vaut 5.

### Remplacer $x$ et $y$ par les valeurs données

Partir de la forme générale des solutions. Remplacer $x$ par $x_0$ et $y(x)$ par $y_0$. On obtient une équation dont l'inconnue est $C$.

### Déterminer la constante $C$

Résoudre cette équation d'inconnue $C$.

### Écrire la solution correspondante

Remplacer $C$ par sa valeur dans la forme générale. On obtient l'**unique** solution qui vérifie la condition initiale.

### Exemple 1

Résoudre $y' = 2y + 6$ avec la condition initiale $y(0) = 5$.

**Forme générale** (fiche précédente) : $y(x) = Ce^{2x} - 3$.

**Remplacer** $x = 0$ et $y = 5$ :

$$Ce^{2 \times 0} - 3 = 5$$

**Déterminer $C$** : comme $e^0 = 1$, on obtient

$$C - 3 = 5 \quad \Longrightarrow \quad C = 8$$

**Écrire la solution :**

$$y(x) = 8e^{2x} - 3$$

Contrôle rapide : $y(0) = 8 - 3 = 5$. La condition initiale est bien respectée.

### Exemple 2

Résoudre $y' = 3y$ avec la condition initiale $y(1) = 2$.

**Forme générale :** $y(x) = Ce^{3x}$.

**Remplacer** $x = 1$ et $y = 2$ (attention : $x$ est remplacé partout, y compris dans l'exposant) :

$$Ce^{3 \times 1} = 2 \quad \Longrightarrow \quad Ce^3 = 2$$

**Déterminer $C$ :**

$$C = \frac{2}{e^3} = 2e^{-3}$$

**Écrire la solution :**

$$y(x) = 2e^{-3}\,e^{3x} = 2e^{3x - 3}$$

---

## 2. Exploiter la solution

### Calculer une valeur demandée

Reprenons la boisson de la fiche précédente : $T'(t) = -0{,}1\,T(t) + 2$, dont les solutions sont $T(t) = Ce^{-0{,}1t} + 20$.

On sait que la boisson est servie à 90 °C, soit $T(0) = 90$.

**Déterminer $C$ :**

$$T(0) = C e^{0} + 20 = C + 20 = 90 \quad \Longrightarrow \quad C = 70$$

**La solution est :**

$$T(t) = 70e^{-0{,}1t} + 20$$

**Question :** quelle est la température au bout de 10 minutes ?

$$T(10) = 70e^{-0{,}1 \times 10} + 20 = 70e^{-1} + 20 \approx 25{,}75 + 20 \approx 45{,}8$$

### Interpréter le résultat dans le contexte

Écrire une phrase de réponse avec l'unité :

> Au bout de 10 minutes, la boisson est à environ **45,8 °C**.

On peut aussi vérifier que le résultat est cohérent : la boisson est partie de 90 °C et a refroidi, mais elle reste plus chaude que la pièce (20 °C), ce qui est normal.

---

## 3. Erreurs fréquentes

### Remplacer incorrectement les valeurs

La condition $y(0) = 5$ signifie $x = 0$ et $y = 5$. Ne pas inverser les deux.

Remplacer $x$ par 5 et $y$ par 0 donne une équation fausse, et donc une mauvaise valeur de $C$.

### Se tromper dans le calcul de $C$

Les erreurs viennent souvent d'un détail de calcul :

- **$e^0 = 1$**, et non 0 : dans $Ce^{2 \times 0}$, le facteur vaut 1, donc l'expression devient $C$ ;
- **les signes** : à partir de $C - 3 = 5$, on ajoute 3 des deux côtés, donc $C = 8$ et non $C = 2$.

### Oublier de remplacer dans toute l'expression

Remplacer $x$ **partout** où il apparaît, y compris dans l'exposant.

Avec $y(x) = Ce^{3x}$ et la condition $y(1) = 2$, il faut écrire $Ce^{3 \times 1} = 2$, et non $Ce^{3x} = 2$.
