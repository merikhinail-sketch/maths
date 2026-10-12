# Propriétés du logarithme népérien

Le logarithme népérien est la fonction « réciproque » de l'exponentielle : il permet de retrouver l'exposant. Cette fiche présente sa définition, ses propriétés de calcul, ses variations et ses limites.

---

## 1. Définition

### Définition de $\ln(x)$

Le logarithme néoérien, noté $\ln(x)$, est le nombre auquel mis élevé à l'exponentielle $e$ donne $x$. Le logarithme népérien admet un domaine de défintions sur $]0\ ;\ +\infty[$.



### Lien avec la fonction exponentielle

Les fonctions $\ln$ et $\exp$ s'annulent mutuellement :

- pour tout réel $x > 0$ : $e^{\ln(x)} = x$ ;
- pour tout réel $x$ : $\ln\left(e^{x}\right) = x$.

Et pour $x > 0$ et $y$ réel : $y = \ln(x) \iff x = e^y$.

**Exemples :** $e^{\ln(5)} = 5$ et $\ln\left(e^3\right) = 3$.

### Valeurs particulières

- $\ln(1) = 0$, car $e^0 = 1$ ;
- $\ln(e) = 1$, car $e^1 = e$.

On en déduit par exemple $\ln\left(\dfrac{1}{e}\right) = \ln\left(e^{-1}\right) = -1$.

---

## 2. Propriétés de la fonction logarithme

### Propriétés de calcul

Pour tous réels $a > 0$ et $b > 0$, et tout entier $n$ :

- $\ln(a \times b) = \ln(a) + \ln(b)$ ;
- $\ln\left(\dfrac{1}{a}\right) = -\ln(a)$ ;
- $\ln\left(\dfrac{a}{b}\right) = \ln(a) - \ln(b)$ ;
- $\ln\left(a^n\right) = n \ln(a)$ ;
- $\ln\left(\sqrt{a}\right) = \dfrac{1}{2}\ln(a)$.

- $(\ln(x))' = \dfrac{1}{x}$



Le logarithme **transforme les produits en sommes**, les quotients en différences et les puissances en produits.

### Transformations d'expressions

**Décomposer.** Exprimer un logarithme à l'aide de logarithmes connus.

- $\ln(6) = \ln(2 \times 3) = \ln(2) + \ln(3)$ ;
- $\ln(12) = \ln(4 \times 3) = \ln\left(2^2\right) + \ln(3) = 2\ln(2) + \ln(3)$.

**Simplifier.** Calculer $A = \ln(18) - 2\ln(3) + \ln(2)$.

Comme $18 = 2 \times 3^2$ : $\ln(18) = \ln(2) + 2\ln(3)$. Donc :

$$A = \ln(2) + 2\ln(3) - 2\ln(3) + \ln(2) = 2\ln(2)$$

**Faire apparaître $e$.** $\ln\left(5e^3\right) = \ln(5) + \ln\left(e^3\right) = \ln(5) + 3$.

**Regrouper.** Pour $x > 0$ : $\ln(x) + \ln(x+1) = \ln\left(x(x+1)\right)$.

---

## 3. Variations et limites

### Fonction strictement croissante

La dérivée de $\ln$ est $\ln'(x) = \dfrac{1}{x}$. Pour $x > 0$, elle est strictement positive : la fonction $\ln$ est **strictement croissante** sur $]0\ ;\ +\infty[$.

Conséquences, pour $a > 0$ et $b > 0$ :

- $a < b \iff \ln(a) < \ln(b)$ ;
- $a = b \iff \ln(a) = \ln(b)$ ;
- comme $\ln(1) = 0$ : $\ln(x) < 0$ pour $0 < x < 1$, et $\ln(x) > 0$ pour $x > 1$.

### Limites

$$\lim_{x \to +\infty} \ln(x) = +\infty \qquad \lim_{x \to 0^+} \ln(x) = -\infty$$

Le logarithme tend vers $+\infty$, mais très lentement.

| $x$ | $0$ | | $+\infty$ |
|---|---|---|---|
| Variations de $\ln$ | $-\infty$ | $\nearrow$ | $+\infty$ |

### Interprétation graphique

La courbe de $\ln$ :

- passe par les points $(1\ ;\ 0)$ et $(e\ ;\ 1)$ ;
- est strictement croissante ;
- admet l'axe des ordonnées ($x = 0$) comme **asymptote verticale** : elle descend vers $-\infty$ en se rapprochant de cet axe ;
- est la **symétrique de la courbe de l'exponentielle par rapport à la droite $y = x$**, puisque les deux fonctions sont réciproques.

---

## 4. Erreurs fréquentes

### Oublier que $\ln(x)$ n'est défini que pour $x > 0$

$\ln(-2)$ et $\ln(0)$ n'existent pas.

Avant d'écrire un logarithme, vérifier que son argument est strictement positif.

### Confondre $\ln(1) = 0$ et $\ln(0) = 0$

$\ln(1) = 0$ est vrai, car $e^0 = 1$. Mais $\ln(0)$ **n'existe pas** : aucun exposant ne donne $e^y = 0$.

### Confondre $\ln(a + b)$ avec $\ln(a) + \ln(b)$

Le logarithme transforme un **produit** en somme, pas une somme en somme : $\ln(a + b) \neq \ln(a) + \ln(b)$.

Avec $a = b = 1$ : $\ln(1 + 1) = \ln(2) \approx 0{,}69$, alors que $\ln(1) + \ln(1) = 0$.

### Mal utiliser les propriétés du logarithme, notamment pour les produits, quotients et puissances

Retenir la correspondance : produit → somme, quotient → différence, puissance → multiplication.

- $\ln(a^2) = 2\ln(a)$, et non $\left(\ln(a)\right)^2$ ;
- $\ln\left(\dfrac{a}{b}\right) = \ln(a) - \ln(b)$, et non $\dfrac{\ln(a)}{\ln(b)}$.

### Confondre le logarithme et l'exponentielle, notamment dans leur lien réciproque

Les deux fonctions s'annulent : $\ln\left(e^x\right) = x$ et $e^{\ln(x)} = x$.

- $\ln\left(e^3\right) = 3$, et non $e^3$ ;
- $e^{\ln(5)} = 5$, et non $\ln(5)$ ;
- $\ln(e) = 1$, et non $e$.
