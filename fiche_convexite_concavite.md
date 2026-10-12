# Convexité et concavité


## 1. Fonction convexe

### Définition

Soit $f$ une fonction dérivable sur un intervalle $I$. On dit que $f$ est **convexe** sur $I$ si sa courbe est située **au-dessus de chacune de ses tangentes**, sur $I$.

**Exemple :** $f(x) = x^2$. La tangente en $x = 1$ a pour équation $y = 2x - 1$. Comparer la courbe et la tangente :

$$x^2 - (2x - 1) = (x - 1)^2 \geq 0$$

La courbe est au-dessus de la tangente. Et cela marche pour toutes les tangentes : $x^2$ est convexe sur $\mathbb{R}$.

### Interprétation graphique

Une courbe convexe a une forme de **coupe** (un « U ») : elle se courbe vers le haut.

Quand on la parcourt de gauche à droite, les tangentes « tournent vers le haut » : leur pente **augmente**.

**Exemples de fonctions convexes :** $x^2$ et $e^x$, sur $\mathbb{R}$.

### Position de la courbe par rapport aux cordes

Une **corde** est un segment qui relie deux points de la courbe.

Pour une fonction convexe, la courbe est **au-dessous de ses cordes** : entre deux points de la courbe, la courbe passe sous le segment qui les relie.

**Exemple :** $f(x) = x^2$. La corde reliant $A(0\ ;\ 0)$ et $B(2\ ;\ 4)$ est sur la droite d'équation $y = 2x$. Pour $x \in [0\ ;\ 2]$ :

$$x^2 \leq 2x \quad \Longleftrightarrow \quad x(x - 2) \leq 0$$

L'inégalité est vraie sur $[0\ ;\ 2]$ : la courbe est sous la corde.

---

## 2. Fonction concave

### Définition

Soit $f$ une fonction dérivable sur un intervalle $I$. On dit que $f$ est **concave** sur $I$ si sa courbe est située **au-dessous de chacune de ses tangentes**, sur $I$.

**Exemple :** $f(x) = -x^2$. La tangente en $x = 1$ a pour équation $y = -2x + 1$. Comparer la courbe et la tangente :

$$-x^2 - (-2x + 1) = -(x - 1)^2 \leq 0$$

La courbe est en-dessous de la tangente : $-x^2$ est concave sur $\mathbb{R}$.

### Interprétation graphique

Une courbe concave a une forme de **dôme** (un « ∩ ») : elle se courbe vers le bas.

Quand on la parcourt de gauche à droite, les tangentes « tournent vers le bas » : leur pente **diminue**.

**Exemples de fonctions concaves :** $-x^2$ sur $\mathbb{R}$, et $\sqrt{x}$ sur $]0\ ;\ +\infty[$.

### Position de la courbe par rapport aux cordes

Pour une fonction concave, la courbe est **au-dessus de ses cordes**.

**Exemple :** $f(x) = -x^2$. La corde reliant $A(0\ ;\ 0)$ et $B(2\ ;\ -4)$ est sur la droite d'équation $y = -2x$. Pour $x \in [0\ ;\ 2]$ :

$$-x^2 \geq -2x \quad \Longleftrightarrow \quad x(x - 2) \leq 0$$

L'inégalité est vraie sur $[0\ ;\ 2]$ : la courbe est au-dessus de la corde.

---

## À retenir

| | Fonction convexe | Fonction concave |
|---|---|---|
| Forme de la courbe | coupe (« U ») | dôme (« ∩ ») |
| Position par rapport aux tangentes | au-dessus | au-dessous |
| Position par rapport aux cordes | au-dessous | au-dessus |
| Pente des tangentes (de gauche à droite) | augmente | diminue |
