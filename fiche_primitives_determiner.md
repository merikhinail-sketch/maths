# Déterminer une primitive

Cette fiche apprend à calculer une primitive en pratique : lire le tableau des primitives usuelles, traiter une somme terme à terme, gérer les coefficients, et fixer la constante $C$ avec une condition.

---

## 1. Calculer une primitive

### Utiliser les primitives usuelles

Reconnaître la forme de $f$ dans le tableau de la fiche précédente, puis lire la primitive correspondante.

**Exemples :**

- $f(x) = x^4$ : une primitive est $F(x) = \dfrac{x^5}{5}$ ;
- $f(x) = \dfrac{1}{x^2}$ : une primitive est $F(x) = -\dfrac{1}{x}$ ;
- $f(x) = e^x$ : une primitive est $F(x) = e^x$.

### Décomposer une expression en plusieurs termes

Une primitive d'une somme est la somme des primitives. On traite donc l'expression **terme par terme**.

**Exemple 1 :** $f(x) = 3x^2 - 4x + 5$.

- $3x^2 \longrightarrow x^3$ ;
- $-4x \longrightarrow -2x^2$ ;
- $5 \longrightarrow 5x$.

Une primitive est $F(x) = x^3 - 2x^2 + 5x$. Les primitives de $f$ sont $F(x) + C$, avec $C$ réel.

**Exemple 2 :** $f(x) = x^2 + \dfrac{1}{x^2} + e^x$ sur $]0\ ;\ +\infty[$.

$$F(x) = \frac{x^3}{3} - \frac{1}{x} + e^x$$

### Gérer les constantes multiplicatives

Une primitive de $k \times f$ est $k \times F$ : le coefficient **reste devant**.

- $f(x) = 5e^x \longrightarrow F(x) = 5e^x$ ;
- $f(x) = \dfrac{6}{x} \longrightarrow F(x) = 6\ln(x)$ sur $]0\ ;\ +\infty[$ ;
- $f(x) = \dfrac{3}{\sqrt{x}} \longrightarrow F(x) = 3 \times 2\sqrt{x} = 6\sqrt{x}$.

**Cas d'une fonction de $ax + b$.** Si $f(x) = g(ax + b)$ avec $G$ une primitive de $g$, alors une primitive de $f$ est $\dfrac{1}{a}\,G(ax + b)$ : **diviser par le coefficient de $x$**, car la dérivée de $ax + b$ est $a$.

- $f(x) = e^{2x} \longrightarrow F(x) = \dfrac{1}{2}e^{2x}$ ;
- $f(x) = (3x - 1)^4 \longrightarrow F(x) = \dfrac{1}{3} \times \dfrac{(3x-1)^5}{5} = \dfrac{(3x-1)^5}{15}$ ;
- $f(x) = \cos(2x) \longrightarrow F(x) = \dfrac{1}{2}\sin(2x)$.

Vérification pour la première : $\left(\dfrac{1}{2}e^{2x}\right)' = \dfrac{1}{2} \times 2e^{2x} = e^{2x}$.

---

## 2. Déterminer une primitive avec une condition

Une condition de la forme $F(x_0) = y_0$ impose que la courbe de $F$ passe par le point $(x_0\ ;\ y_0)$. Elle fixe la constante $C$ : il ne reste qu'**une seule** primitive.

### Utiliser une condition du type $F(x_0) = y_0$

Procéder en trois temps :

1. écrire les primitives de $f$ sous la forme $F(x) + C$ ;
2. remplacer $x$ par $x_0$ et $F(x)$ par $y_0$ ;
3. résoudre l'équation obtenue d'inconnue $C$.

### Déterminer $C$

**Exemple 1 :** déterminer la primitive $F$ de $f(x) = 2x + 3$ telle que $F(1) = 4$.

Les primitives de $f$ sont $F(x) = x^2 + 3x + C$. La condition $F(1) = 4$ donne :

$$1^2 + 3 \times 1 + C = 4 \iff 4 + C = 4 \iff C = 0$$

La primitive cherchée est $F(x) = x^2 + 3x$.

**Exemple 2 :** déterminer la primitive $F$ de $f(x) = e^{2x}$ telle que $F(0) = 3$.

Les primitives de $f$ sont $F(x) = \dfrac{1}{2}e^{2x} + C$. La condition $F(0) = 3$ donne :

$$\frac{1}{2}e^{0} + C = 3 \iff \frac{1}{2} + C = 3 \iff C = \frac{5}{2}$$

La primitive cherchée est $F(x) = \dfrac{1}{2}e^{2x} + \dfrac{5}{2}$.

---

## 3. Exploiter une primitive

### Vérifier qu'une fonction obtenue est bien une primitive

Dériver la fonction proposée et comparer avec $f$. Cette vérification est toujours possible, même quand on ne sait pas trouver la primitive soi-même.

**Exemple :** montrer que $F(x) = (x - 1)e^x$ est une primitive de $f(x) = x\,e^x$ sur $\mathbb{R}$.

$F$ est un produit : $F'(x) = 1 \times e^x + (x - 1)e^x = e^x\left(1 + x - 1\right) = x\,e^x = f(x)$.

$F$ est bien une primitive de $f$.

### Utiliser une primitive dans un problème

Une primitive permet de retrouver une quantité dont on connaît la **vitesse de variation**.

**Exemple :** un mobile se déplace sur une droite avec la vitesse $v(t) = 6t + 2$ (en m/s). Sa position $s(t)$ (en mètres) vérifie $s'(t) = v(t)$, donc $s$ est une primitive de $v$. À l'instant $t = 0$, il est à la position $s(0) = 10$.

- Primitives de $v$ : $s(t) = 3t^2 + 2t + C$.
- Condition $s(0) = 10$ : $0 + 0 + C = 10$, donc $C = 10$.
- Donc $s(t) = 3t^2 + 2t + 10$.

Position à $t = 4$ secondes : $s(4) = 3 \times 16 + 2 \times 4 + 10 = 48 + 8 + 10 = 66$.

Au bout de 4 secondes, le mobile est à 66 mètres de l'origine.
