# Étudier la convexité d'une fonction

Cette fiche donne une méthode en quatre étapes pour trouver où une fonction est convexe ou concave. Un grand exemple guidé la déroule de A à Z.

---

## 1. Étudier la convexité d'une fonction
### Lien entre le signe de $f''$ et la convexité/concavité

**Propriété.** Soit $f$ une fonction deux fois dérivable sur un intervalle $I$ :

- si $f''(x) \geq 0$ sur $I$, alors $f$ est **convexe** sur $I$ ;
- si $f''(x) \leq 0$ sur $I$, alors $f$ est **concave** sur $I$.

Pourquoi ? La dérivée seconde $f''$ indique comment varie $f'$, c'est-à-dire la pente des tangentes :

- $f'' \geq 0$ : $f'$ est croissante, la pente des tangentes augmente, la courbe se courbe vers le haut : $f$ est convexe ;
- $f'' \leq 0$ : $f'$ est décroissante, la pente diminue, la courbe se courbe vers le bas : $f$ est concave.

### Grand exemple guidé de A à Z

**Énoncé.** Soit $f$ la fonction définie sur $\mathbb{R}$ par :

$$f(x) = x^3 - 3x^2 + 2$$

Étudier la convexité de $f$ : déterminer les intervalles sur lesquels elle est convexe et ceux sur lesquels elle est concave.

### Calcul de la dérivée seconde

La **dérivée seconde** $f''$ est la dérivée de la dérivée : on dérive la fonction $f$ deux fois.

La fonction $f$ est un polynôme, donc dérivable autant de fois que l'on veut.

**Première dérivée :**

$$f'(x) = 3x^2 - 6x$$

**Deuxième dérivée :**

$$f''(x) = 6x - 6 = 6(x - 1)$$

La forme factorisée $6(x - 1)$ sera pratique pour étudier le signe.

### Étude du signe de la dérivée seconde

Chercher quand $f''(x)$ est positif, nul ou négatif.

- $f''(x) = 0 \iff x = 1$ ;
- $f''(x) > 0 \iff 6(x - 1) > 0 \iff x > 1$ ;
- $f''(x) < 0 \iff x < 1$.

Résumer dans un tableau de signes :

| $x$ | $-\infty$ | | $1$ | | $+\infty$ |
|---|---|---|---|---|---|
| Signe de $f''(x)$ | | $-$ | $0$ | $+$ | |



### Détermination des intervalles de convexité et de concavité

D'après le tableau de signes :

- $f''(x) \leq 0$ sur $]-\infty\ ;\ 1]$, donc $f$ est **concave** sur $]-\infty\ ;\ 1]$ ;
- $f''(x) \geq 0$ sur $[1\ ;\ +\infty[$, donc $f$ est **convexe** sur $[1\ ;\ +\infty[$.

La courbe de $f$ passe donc de concave à convexe en $x = 1$.

**Vérification rapide :** $f''(0) = -6 < 0$, donc concave près de $0$ ; $f''(2) = 6 > 0$, donc convexe près de $2$. Les résultats sont cohérents.

**Rédaction de la conclusion :**

> La fonction $f$ est deux fois dérivable sur $\mathbb{R}$, et $f''(x) = 6(x - 1)$. Ainsi $f''(x) \leq 0$ sur $]-\infty\ ;\ 1]$ et $f''(x) \geq 0$ sur $[1\ ;\ +\infty[$. La fonction $f$ est donc concave sur $]-\infty\ ;\ 1]$ et convexe sur $[1\ ;\ +\infty[$.
