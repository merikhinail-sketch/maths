# Vecteurs dans l'espace

Dans l'espace, un vecteur a **trois** coordonnées. Cette fiche étend les idées du plan : directions, colinéarité, puis deux notions nouvelles, la combinaison linéaire et la coplanarité.

Dans toute la fiche, l'espace est muni d'un repère orthonormé.

---

## 1. Vecteurs et directions dans l'espace

### Utiliser les coordonnées pour caractériser une direction

Un point de l'espace est repéré par trois coordonnées $A(x_A\ ;\ y_A\ ;\ z_A)$. Les coordonnées du vecteur $\overrightarrow{AB}$ s'obtiennent en faisant « arrivée moins départ » :

$$\overrightarrow{AB}\begin{pmatrix} x_B - x_A \\ y_B - y_A \\ z_B - z_A \end{pmatrix}$$

Une **direction** est portée par un vecteur non nul. Tous les vecteurs proportionnels à celui-ci ont la même direction.

**Exemple :** $\vec{u}\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$ et $\begin{pmatrix} 2 \\ 4 \\ 6 \end{pmatrix}$ ont la même direction, car le deuxième vaut $2\vec{u}$.

### Vecteurs directeurs

Un **vecteur directeur** d'une droite $(d)$ est un vecteur non nul dont la direction est celle de $(d)$.

Pour une droite $(AB)$, le vecteur $\overrightarrow{AB}$ est un vecteur directeur. Tout vecteur colinéaire à $\overrightarrow{AB}$ (et non nul) en est un aussi : une droite a donc une infinité de vecteurs directeurs.

**Exemple :** $A(1\ ;\ 0\ ;\ 2)$ et $B(3\ ;\ 2\ ;\ 3)$.

$\overrightarrow{AB}\begin{pmatrix} 2 \\ 2 \\ 1 \end{pmatrix}$ est un vecteur directeur de $(AB)$. Le vecteur $\begin{pmatrix} 4 \\ 4 \\ 2 \end{pmatrix}$ en est un autre.

### Reconnaître des vecteurs colinéaires

Deux vecteurs non nuls $\vec{u}$ et $\vec{v}$ sont **colinéaires** s'il existe un réel $k$ tel que $\vec{v} = k\,\vec{u}$. En coordonnées, cela veut dire que **leurs coordonnées sont proportionnelles**.

Méthode : trouver $k$ avec une coordonnée non nulle, puis **vérifier les deux autres**.

**Exemple 1 :** $\vec{u}\begin{pmatrix} 2 \\ -1 \\ 4 \end{pmatrix}$ et $\vec{v}\begin{pmatrix} -4 \\ 2 \\ -8 \end{pmatrix}$.

Avec la première coordonnée : $-4 = k \times 2$, donc $k = -2$. Vérification : $2 = -2 \times (-1)$ ✓ et $-8 = -2 \times 4$ ✓. Donc $\vec{v} = -2\vec{u}$ : les vecteurs sont colinéaires.

**Exemple 2 :** $\vec{u}\begin{pmatrix} 2 \\ -1 \\ 4 \end{pmatrix}$ et $\vec{w}\begin{pmatrix} 4 \\ -2 \\ 9 \end{pmatrix}$.

Avec la première coordonnée : $k = 2$. Vérification : $-2 = 2 \times (-1)$ ✓ mais $9 \neq 2 \times 4 = 8$ ✗. Les vecteurs ne sont pas colinéaires.

### Exploiter la colinéarité dans des problèmes géométriques

**Aligner trois points.** $A$, $B$, $C$ sont alignés si $\overrightarrow{AB}$ et $\overrightarrow{AC}$ sont colinéaires.

*Exemple :* $A(1\ ;\ 2\ ;\ 3)$, $B(2\ ;\ 4\ ;\ 5)$, $C(4\ ;\ 8\ ;\ 9)$. On a $\overrightarrow{AB}\begin{pmatrix} 1 \\ 2 \\ 2 \end{pmatrix}$ et $\overrightarrow{AC}\begin{pmatrix} 3 \\ 6 \\ 6 \end{pmatrix} = 3\overrightarrow{AB}$. Les points sont alignés.

**Montrer un parallélogramme.** $ABCD$ est un parallélogramme si $\overrightarrow{AB} = \overrightarrow{DC}$.

*Exemple :* $A(0\ ;\ 0\ ;\ 0)$, $B(1\ ;\ 2\ ;\ 0)$, $C(3\ ;\ 3\ ;\ 1)$, $D(2\ ;\ 1\ ;\ 1)$. On a $\overrightarrow{AB}\begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}$ et $\overrightarrow{DC}\begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}$ : égaux, donc $ABCD$ est un parallélogramme.

---

## 2. Combinaisons linéaires

### Écrire un vecteur comme combinaison de deux autres

Une **combinaison linéaire** de deux vecteurs $\vec{u}$ et $\vec{v}$ est un vecteur de la forme :

$$\vec{w} = a\,\vec{u} + b\,\vec{v}$$

où $a$ et $b$ sont deux réels.

Pour écrire $\vec{w}$ sous cette forme, poser les égalités sur chaque coordonnée, puis résoudre le système en $a$ et $b$.

**Exemple :** $\vec{u}\begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}$, $\vec{v}\begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}$ et $\vec{w}\begin{pmatrix} 2 \\ 3 \\ 5 \end{pmatrix}$. On cherche $a$ et $b$ tels que $\vec{w} = a\vec{u} + b\vec{v}$ :

$$\begin{cases} a = 2 \\ b = 3 \\ a + b = 5 \end{cases}$$

Les deux premières lignes donnent $a = 2$ et $b = 3$. La troisième ligne est vérifiée : $2 + 3 = 5$ ✓. Donc $\vec{w} = 2\vec{u} + 3\vec{v}$.

### Comprendre ce que cette relation signifie géométriquement

Si $\vec{u}$ et $\vec{v}$ ne sont pas colinéaires, les combinaisons linéaires $a\vec{u} + b\vec{v}$ sont exactement les vecteurs **contenus dans le plan dirigé par $\vec{u}$ et $\vec{v}$**.

Écrire $\vec{w} = a\vec{u} + b\vec{v}$ revient donc à dire que $\vec{w}$ « reste dans le plan » de $\vec{u}$ et $\vec{v}$ : on s'y déplace en avançant de $a$ fois $\vec{u}$ puis de $b$ fois $\vec{v}$.

### Utiliser une combinaison linéaire pour établir une propriété

Une combinaison linéaire permet de montrer que **quatre points sont dans un même plan**.

**Exemple :** $A(0\ ;\ 0\ ;\ 0)$, $B(1\ ;\ 0\ ;\ 1)$, $C(0\ ;\ 1\ ;\ 1)$ et $D(2\ ;\ 3\ ;\ 5)$.

On a $\overrightarrow{AB}\begin{pmatrix} 1 \\ 0 \\ 1 \end{pmatrix}$, $\overrightarrow{AC}\begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}$ et $\overrightarrow{AD}\begin{pmatrix} 2 \\ 3 \\ 5 \end{pmatrix}$. D'après l'exemple précédent :

$$\overrightarrow{AD} = 2\overrightarrow{AB} + 3\overrightarrow{AC}$$

Le point $D$ se trouve donc dans le plan $(ABC)$ : les quatre points sont coplanaires.

---

## 3. Coplanarité

### Comprendre ce que signifie « vecteurs coplanaires »

Trois vecteurs $\vec{u}$, $\vec{v}$ et $\vec{w}$ sont **coplanaires** lorsqu'on peut les représenter par des flèches qui partent d'un même point et restent **toutes dans un même plan**.

**Exemple :** trois vecteurs posés sur une table sont coplanaires. En revanche, les vecteurs formés par trois arêtes d'un cube qui partent d'un même sommet ne le sont pas.

### Caractériser la coplanarité avec une combinaison linéaire

**Propriété.** Soient $\vec{u}$ et $\vec{v}$ deux vecteurs **non colinéaires**. Alors $\vec{u}$, $\vec{v}$ et $\vec{w}$ sont coplanaires si et seulement s'il existe deux réels $a$ et $b$ tels que :

$$\vec{w} = a\,\vec{u} + b\,\vec{v}$$

Remarque : si $\vec{u}$ et $\vec{v}$ sont colinéaires, les trois vecteurs sont toujours coplanaires.

### Démontrer que des vecteurs sont ou ne sont pas coplanaires

Procéder en quatre temps :

1. choisir deux des vecteurs, non colinéaires : $\vec{u}$ et $\vec{v}$ ;
2. écrire $\vec{w} = a\vec{u} + b\vec{v}$, soit un système de trois équations ;
3. utiliser **deux équations** pour trouver $a$ et $b$ ;
4. **vérifier la troisième**. Si elle est vraie, les vecteurs sont coplanaires ; sinon, ils ne le sont pas.

**Exemple 1 (coplanaires) :** $\vec{u}\begin{pmatrix} 1 \\ 2 \\ 0 \end{pmatrix}$, $\vec{v}\begin{pmatrix} 0 \\ 1 \\ 1 \end{pmatrix}$ et $\vec{w}\begin{pmatrix} 2 \\ 5 \\ 1 \end{pmatrix}$.

Les vecteurs $\vec{u}$ et $\vec{v}$ ne sont pas colinéaires. On résout $\vec{w} = a\vec{u} + b\vec{v}$ :

$$\begin{cases} a = 2 \\ 2a + b = 5 \\ b = 1 \end{cases}$$

La première équation donne $a = 2$, la troisième donne $b = 1$. Vérification avec la deuxième : $2 \times 2 + 1 = 5$ ✓. Donc $\vec{w} = 2\vec{u} + \vec{v}$ : les trois vecteurs sont **coplanaires**.

**Exemple 2 (non coplanaires) :** mêmes $\vec{u}$ et $\vec{v}$, avec $\vec{w'}\begin{pmatrix} 2 \\ 5 \\ 2 \end{pmatrix}$.

$$\begin{cases} a = 2 \\ 2a + b = 5 \\ b = 2 \end{cases}$$

La première équation donne $a = 2$, la troisième donne $b = 2$. Vérification avec la deuxième : $2 \times 2 + 2 = 6 \neq 5$ ✗. Il n'existe pas de $a$ et $b$ convenables : les vecteurs $\vec{u}$, $\vec{v}$ et $\vec{w'}$ ne sont **pas coplanaires**.

**Exemple 3 (cas classique) :** $\vec{i}\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$, $\vec{j}\begin{pmatrix} 0 \\ 1 \\ 0 \end{pmatrix}$ et $\vec{k}\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$.

Si $\vec{k} = a\vec{i} + b\vec{j}$, alors $\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix} = \begin{pmatrix} a \\ b \\ 0 \end{pmatrix}$, ce qui est impossible car $1 \neq 0$. Les vecteurs $\vec{i}$, $\vec{j}$, $\vec{k}$ ne sont pas coplanaires.
