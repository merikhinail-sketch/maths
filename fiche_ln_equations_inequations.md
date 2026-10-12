# Calcul avec la fonction logarithme

Cette fiche apprend à résoudre des équations et des inéquations qui contiennent des logarithmes. Deux réflexes à garder : **vérifier d'abord où l'expression existe**, puis utiliser le fait que $\ln$ est strictement croissante.

---

## 1. Équations

### Résoudre une équation de la forme $\ln(x) = a$

Pour un réel $a$ quelconque, l'équation $\ln(x) = a$ a une unique solution :

$$\ln(x) = a \iff x = e^a$$

**Exemples :**

- $\ln(x) = 3 \iff x = e^3$ ;
- $\ln(x) = -1 \iff x = e^{-1} = \dfrac{1}{e}$.

### Utiliser le lien entre le logarithme et l'exponentielle

Pour une équation de la forme $\ln(u(x)) = a$, appliquer l'exponentielle aux deux membres : $\ln(u(x)) = a \iff u(x) = e^a$, à condition que $u(x) > 0$.

**Exemple :** résoudre $\ln(x - 2) = 1$.

- **Condition d'existence :** $x - 2 > 0 \iff x > 2$.
- **Résolution :** $\ln(x - 2) = 1 \iff x - 2 = e^1 \iff x = 2 + e$.
- **Vérification :** $2 + e \approx 4{,}7 > 2$, donc la solution est dans le domaine.

La solution est $x = 2 + e$.

### Transformer une équation pour faire apparaître un même logarithme

Quand l'équation contient plusieurs logarithmes, utiliser les propriétés de calcul pour obtenir $\ln(\dots) = \ln(\dots)$. Comme $\ln$ est strictement croissante, $\ln(A) = \ln(B) \iff A = B$ (pour $A > 0$ et $B > 0$).

**Exemple 1 :** résoudre $\ln(x + 1) = \ln(2x - 3)$.

- **Conditions d'existence :** $x + 1 > 0 \iff x > -1$ et $2x - 3 > 0 \iff x > \dfrac{3}{2}$. Les deux sont vraies si $x > \dfrac{3}{2}$.
- **Résolution :** $x + 1 = 2x - 3 \iff x = 4$.
- **Vérification :** $4 > \dfrac{3}{2}$, donc $x = 4$ est dans le domaine.

La solution est $x = 4$.

**Exemple 2 :** résoudre $\ln(x) + \ln(x - 1) = \ln(6)$.

- **Conditions d'existence :** $x > 0$ et $x - 1 > 0$, donc $x > 1$.
- **Transformation :** $\ln(x) + \ln(x - 1) = \ln\left(x(x-1)\right)$. L'équation devient $\ln\left(x(x-1)\right) = \ln(6)$.
- **Résolution :** $x(x - 1) = 6 \iff x^2 - x - 6 = 0 \iff (x - 3)(x + 2) = 0$. Les candidats sont $x = 3$ et $x = -2$.
- **Vérification :** $-2$ n'est pas supérieur à $1$ : il est **rejeté**. $3 > 1$ : il convient.

La solution est $x = 3$.

### Vérifier les conditions d'existence

Cette étape revient à **chaque** équation. La méthode en quatre temps :

1. Écrire les conditions : l'argument de chaque logarithme doit être strictement positif.
2. Résoudre l'équation.
3. Garder seulement les solutions qui respectent les conditions.
4. Conclure en donnant l'ensemble des solutions.

---

## 2. Inéquations

### Utiliser le fait que le logarithme est strictement croissant

Comme $\ln$ est strictement croissante, elle **conserve l'ordre** : pour $a > 0$ et $b > 0$,

$$a < b \iff \ln(a) < \ln(b) \qquad \text{et} \qquad a \leq b \iff \ln(a) \leq \ln(b)$$

Le sens de l'inégalité ne change pas.

### Comparer les logarithmes

Pour comparer deux logarithmes, comparer leurs arguments.

**Exemple :** $3 < 5$, donc $\ln(3) < \ln(5)$.

Autre résultat utile : $\ln(x) \leq 0 \iff \ln(x) \leq \ln(1) \iff 0 < x \leq 1$, en n'oubliant pas la condition $x > 0$.

### Ramener une inéquation à une comparaison des nombres

Mettre l'inéquation sous la forme $\ln(A) < \ln(B)$ (ou avec un autre symbole), puis comparer $A$ et $B$.

Pour comparer à un nombre $a$ : écrire $a = \ln\left(e^a\right)$.

**Exemple 1 :** résoudre $\ln(x) > 2$.

$\ln(x) > 2 \iff \ln(x) > \ln\left(e^2\right) \iff x > e^2$. La condition $x > 0$ est automatiquement vérifiée. Les solutions sont $]e^2\ ;\ +\infty[$.

**Exemple 2 :** résoudre $\ln(x - 2) < \ln(5)$.

- **Condition d'existence :** $x - 2 > 0 \iff x > 2$.
- **Résolution :** $x - 2 < 5 \iff x < 7$.
- **Ensemble des solutions :** $x > 2$ et $x < 7$, donc $]2\ ;\ 7[$.

### Vérifier les conditions de définition

Garder l'intersection entre les solutions trouvées et le domaine de définition.

**Exemple :** résoudre $\ln(2x - 1) \geq \ln(x + 3)$.

- **Conditions de définition :** $2x - 1 > 0 \iff x > \dfrac{1}{2}$ et $x + 3 > 0 \iff x > -3$. Le domaine est $\left]\dfrac{1}{2}\ ;\ +\infty\right[$.
- **Résolution :** $2x - 1 \geq x + 3 \iff x \geq 4$.
- **Intersection :** $x \geq 4$ et $x > \dfrac{1}{2}$ donnent $x \geq 4$.

Les solutions sont $[4\ ;\ +\infty[$.

---

## 3. Erreurs fréquentes

### Oublier les conditions d'existence avant de résoudre une équation ou une inéquation

Écrire en premier : « Les logarithmes sont définis pour $x > \dots$ ». Sans cette étape, on peut accepter des « solutions » qui n'existent pas.

### Résoudre puis oublier de vérifier que la solution est positive

Après la résolution, comparer chaque candidat aux conditions d'existence.

Dans l'équation $\ln(x) + \ln(x - 1) = \ln(6)$, on trouve $x = 3$ et $x = -2$. Seul $x = 3$ est valide, car $-2$ ne vérifie pas $x > 1$.

### Mal utiliser la croissance stricte du logarithme dans une inéquation

$\ln$ est strictement croissante : **le sens de l'inégalité est conservé**.

$\ln(x) < \ln(5) \iff x < 5$, et non $x > 5$. N'oublier pas non plus la condition de domaine :

$\ln(x) < -1 \iff 0 < x < e^{-1}$, et non seulement $x < e^{-1}$.

### Conclure de $\ln(a) = \ln(b)$ à $a = b$ sans avoir vérifié que les deux expressions sont bien définies

L'équivalence $\ln(A) = \ln(B) \iff A = B$ n'est valable que si $A > 0$ et $B > 0$.

Pour $\ln(x - 5) = \ln(3x - 9)$, on trouve $x - 5 = 3x - 9 \iff x = 2$. Mais pour $x = 2$, on aurait $x - 5 = -3 < 0$ : les logarithmes n'existent pas. Les conditions $x > 5$ et $x > 3$ donnent $x > 5$, et $2$ n'y est pas. L'équation n'a **aucune solution**.

### Se tromper dans les transformations d'expressions avant de résoudre

Revoir les propriétés de calcul :

- $\ln(x) + \ln(x - 1) = \ln\left(x(x-1)\right)$, et non $\ln\left(x + (x - 1)\right)$ ;
- $\ln(a) - \ln(b) = \ln\left(\dfrac{a}{b}\right)$, et non $\ln(a - b)$.
