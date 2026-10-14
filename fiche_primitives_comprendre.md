# Comprendre les primitives

Une primitive est le « chemin inverse » de la dérivation : on part de la dérivée, et on retrouve la fonction. Cette fiche explique cette idée, puis donne les primitives usuelles à connaître.

---

## 1. Définition

### Lien entre fonction et dérivée

Dériver, c'est passer d'une fonction $F$ à sa dérivée $F'$. **Primitiver** fait le chemin inverse : on se donne une fonction $f$, et on cherche une fonction $F$ dont la dérivée est $f$.

**Définition.** Soit $f$ une fonction définie sur un intervalle $I$. Une **primitive** de $f$ sur $I$ est une fonction $F$ dérivable sur $I$ telle que, pour tout $x$ de $I$ :

$$F'(x) = f(x)$$

**Exemple :** $f(x) = 2x$ et $F(x) = x^2$. On a $F'(x) = 2x = f(x)$ : la fonction $F$ est une primitive de $f$ sur $\mathbb{R}$.

On admet que toute fonction **continue** sur un intervalle admet des primitives sur cet intervalle.

### Reconnaître une primitive

Pour vérifier qu'une fonction $F$ est une primitive de $f$ : **dériver $F$** et comparer le résultat à $f$.

**Exemple 1 :** $F(x) = x^3 - x$ est-elle une primitive de $f(x) = 3x^2 - 1$ ?

$F'(x) = 3x^2 - 1 = f(x)$. Oui.

**Exemple 2 :** $G(x) = x^3$ est-elle une primitive de $f(x) = 3x^2 - 1$ ?

$G'(x) = 3x^2 \neq 3x^2 - 1$. Non.

### Ajouter une constante $C$

La dérivée d'une constante est nulle. Donc, si $F$ est une primitive de $f$, alors $F + C$ en est une aussi, pour tout réel $C$ :

$$(F + C)' = F' + 0 = f$$

**Exemple :** $x^2$, $x^2 + 1$ et $x^2 - 5$ sont trois primitives de $2x$.

Réciproquement, sur un intervalle, **deux primitives d'une même fonction diffèrent d'une constante**. Ainsi, l'ensemble des primitives de $f$ sur $I$ est :

$$\left\{F + C \ ;\ C \in \mathbb{R}\right\}$$

Une fonction a donc une **infinité** de primitives. On parle d'**une** primitive de $f$, et non de **la** primitive. La valeur de $C$ se fixe avec une condition supplémentaire, comme on le verra dans la fiche suivante.

---

## 2. Primitives usuelles

### Reconnaître les principales formes et connaître les primitives correspondantes

Chaque ligne se lit dans le tableau des dérivées à l'envers. Dans le tableau, $F$ est **une** primitive de $f$ ; toutes les autres s'obtiennent en ajoutant une constante $C$.

| $f(x)$ | Une primitive $F(x)$ | Intervalle |
|---|---|---|
| $k$ (constante) | $kx$ | $\mathbb{R}$ |
| $x^n$ ($n$ entier, $n \neq -1$) | $\dfrac{x^{n+1}}{n+1}$ | $\mathbb{R}$ si $n \geq 0$ ; $]-\infty\ ;\ 0[$ ou $]0\ ;\ +\infty[$ si $n \leq -2$ |
| $\dfrac{1}{x^2}$ | $-\dfrac{1}{x}$ | $]-\infty\ ;\ 0[$ ou $]0\ ;\ +\infty[$ |
| $\dfrac{1}{x}$ | $\ln(x)$ | $]0\ ;\ +\infty[$ |
| $\dfrac{1}{\sqrt{x}}$ | $2\sqrt{x}$ | $]0\ ;\ +\infty[$ |
| $e^{x}$ | $e^{x}$ | $\mathbb{R}$ |
| $\cos(x)$ | $\sin(x)$ | $\mathbb{R}$ |
| $\sin(x)$ | $-\cos(x)$ | $\mathbb{R}$ |

Pour chaque ligne, on peut vérifier en dérivant. Par exemple : $\left(\dfrac{x^2}{2}\right)' = x$, $\left(-\dfrac{1}{x}\right)' = \dfrac{1}{x^2}$, $\left(2\sqrt{x}\right)' = \dfrac{1}{\sqrt{x}}$ et $\left(-\cos(x)\right)' = \sin(x)$.

**Exemples d'utilisation :**

- une primitive de $x^4$ est $\dfrac{x^5}{5}$ ;
- une primitive de $x$ est $\dfrac{x^2}{2}$ ;
- une primitive de $\dfrac{1}{x^3} = x^{-3}$ est $\dfrac{x^{-2}}{-2} = -\dfrac{1}{2x^2}$.

### Les formes avec une fonction composée

En lisant à l'envers le tableau de dérivation des fonctions composées, on obtient les formes suivantes, où $u$ est une fonction dérivable :

| $f(x)$ | Une primitive $F(x)$ | Condition | Exemple |
|---|---|---|---|
| $u'\,u^{n}$ ($n \neq -1$) | $\dfrac{u^{n+1}}{n+1}$ | | $2x\,(x^2+1)^3 \longrightarrow \dfrac{(x^2+1)^4}{4}$ |
| $u'\,e^{u}$ | $e^{u}$ | | $2x\,e^{x^2} \longrightarrow e^{x^2}$ |
| $\dfrac{u'}{u}$ | $\ln(u)$ | $u > 0$ | $\dfrac{2x}{x^2+1} \longrightarrow \ln(x^2+1)$ |
| $\dfrac{u'}{\sqrt{u}}$ | $2\sqrt{u}$ | $u > 0$ | $\dfrac{2x}{\sqrt{x^2+1}} \longrightarrow 2\sqrt{x^2+1}$ |

Pour reconnaître ces formes, repérer dans l'expression une fonction $u$ **et** sa dérivée $u'$.
