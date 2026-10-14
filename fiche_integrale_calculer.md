# Calculer une intégrale

Cette fiche déroule le calcul d'une intégrale en trois temps : trouver une primitive, calculer $F(b) - F(a)$, puis utiliser les propriétés pour simplifier. Suivre chaque étape en refaisant les calculs.

---

## 1. Grand exemple guidé

### Calculer l'intégrale d'une fonction à l'aide d'une primitive

**Énoncé.** Calculer :

$$I = \int_0^1 \left(3x^2 - 2x + e^{2x}\right)dx$$

### Trouver une primitive

Traiter la fonction terme par terme, et gérer les coefficients.

- $3x^2 \longrightarrow x^3$ ;
- $-2x \longrightarrow -x^2$ ;
- $e^{2x} \longrightarrow \dfrac{1}{2}e^{2x}$ (on divise par le coefficient $2$ de $x$ dans l'exposant).

Une primitive de $f(x) = 3x^2 - 2x + e^{2x}$ est :

$$F(x) = x^3 - x^2 + \frac{1}{2}e^{2x}$$

**Vérification :** $F'(x) = 3x^2 - 2x + \dfrac{1}{2} \times 2e^{2x} = 3x^2 - 2x + e^{2x} = f(x)$.

### Calculer l'intégrale à partir de celle-ci

Appliquer la définition : $I = F(1) - F(0)$.

- $F(1) = 1^3 - 1^2 + \dfrac{1}{2}e^{2} = 0 + \dfrac{1}{2}e^2 = \dfrac{e^2}{2}$ ;
- $F(0) = 0 - 0 + \dfrac{1}{2}e^{0} = \dfrac{1}{2}$.

$$I = \frac{e^2}{2} - \frac{1}{2} = \frac{e^2 - 1}{2} \approx 3{,}19$$

### Simplifier un calcul avec les propriétés de l'intégrale

**Avec la linéarité.** On peut aussi découper l'intégrale :

$$I = 3\int_0^1 x^2\,dx - 2\int_0^1 x\,dx + \int_0^1 e^{2x}\,dx$$

avec

- $\displaystyle \int_0^1 x^2\,dx = \left[\frac{x^3}{3}\right]_0^1 = \frac{1}{3}$ ;
- $\displaystyle \int_0^1 x\,dx = \left[\frac{x^2}{2}\right]_0^1 = \frac{1}{2}$ ;
- $\displaystyle \int_0^1 e^{2x}\,dx = \left[\frac{1}{2}e^{2x}\right]_0^1 = \frac{e^2 - 1}{2}$.

Donc $I = 3 \times \dfrac{1}{3} - 2 \times \dfrac{1}{2} + \dfrac{e^2 - 1}{2} = 1 - 1 + \dfrac{e^2 - 1}{2} = \dfrac{e^2 - 1}{2}$. On retrouve le même résultat.

**Avec Chasles et le changement de sens des bornes (sans primitive).** Parfois, on ne connaît pas la fonction mais seulement certaines intégrales. Soit $g$ une fonction continue telle que :

$$\int_0^2 g(x)\,dx = 3 \qquad \text{et} \qquad \int_5^2 g(x)\,dx = -4$$

- Changement de sens des bornes : $\displaystyle \int_2^5 g(x)\,dx = -\int_5^2 g(x)\,dx = 4$.
- Relation de Chasles : $\displaystyle \int_0^5 g(x)\,dx = \int_0^2 g(x)\,dx + \int_2^5 g(x)\,dx = 3 + 4 = 7$.
- Linéarité : $\displaystyle \int_0^2 \big(2g(x) + 1\big)\,dx = 2 \times 3 + \int_0^2 1\,dx = 6 + 2 = 8$.

---

## 2. Erreurs fréquentes

### Utiliser une mauvaise primitive

Revoir le tableau des primitives usuelles, et vérifier en dérivant.

Une primitive de $\dfrac{1}{x^2}$ est $-\dfrac{1}{x}$, et non $\ln(x)$. Ainsi $\displaystyle \int_1^2 \frac{1}{x^2}\,dx = \left[-\frac{1}{x}\right]_1^2 = -\frac{1}{2} + 1 = \frac{1}{2}$.

### Oublier de prendre en compte les coefficients lors du calcul d'une primitive

Une primitive de $e^{2x}$ est $\dfrac{1}{2}e^{2x}$, et non $e^{2x}$.

Avec cette erreur, on trouverait $\displaystyle \int_0^1 e^{2x}\,dx = e^2 - 1$ au lieu de la bonne valeur $\dfrac{e^2 - 1}{2}$.

### Se tromper dans le calcul de $F(b) - F(a)$

Mettre $F(a)$ entre parenthèses, surtout quand elle est négative.

Pour $\displaystyle \int_{-1}^{2} x^2\,dx$, avec $F(x) = \dfrac{x^3}{3}$ : $F(2) - F(-1) = \dfrac{8}{3} - \left(-\dfrac{1}{3}\right) = \dfrac{9}{3} = 3$. Écrire $\dfrac{8}{3} - \dfrac{1}{3}$ conduit à un résultat faux.

### Inverser les bornes ou les valeurs $a$ et $b$

Calculer toujours $F(b) - F(a)$ : la borne du haut **moins** la borne du bas, dans cet ordre.

$\displaystyle \int_2^0 x\,dx$ vaut $F(0) - F(2) = -2$, et non $2$.

### Oublier qu'une intégrale peut être négative lorsqu'on l'interprète comme une aire algébrique

Une intégrale est une aire **algébrique** : elle peut être négative, ou nulle.

$\displaystyle \int_0^2 (x - 3)\,dx = -4$ : la fonction est négative sur $[0\ ;\ 2]$. L'aire géométrique est de $4$ u.a., mais l'intégrale vaut $-4$. Dire « une aire ne peut pas être négative, donc j'ai fait une erreur » est faux.

### Mal utiliser les propriétés de l'intégrale, notamment la linéarité ou la relation de Chasles

- **Linéarité :** elle s'applique aux sommes et aux constantes, pas aux produits. $\displaystyle \int_0^1 x \times x\,dx = \frac{1}{3}$, alors que $\displaystyle \int_0^1 x\,dx \times \int_0^1 x\,dx = \frac{1}{4}$.
- **Chasles :** les bornes doivent s'enchaîner. On a $\displaystyle \int_0^1 f + \int_1^3 f = \int_0^3 f$, mais $\displaystyle \int_0^1 f + \int_2^3 f \neq \int_0^3 f$ en général. Avec $f = 1$ : $1 + 1 = 2 \neq 3$.
