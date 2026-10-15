# Rappels : vecteurs, colinéarité et produit scalaire

Cette fiche reprend dans le **plan** les outils de Première dont on aura besoin en géométrie dans l'espace. Dans l'espace, il suffira d'ajouter une troisième coordonnée : les idées seront les mêmes.

Dans toute la fiche, le plan est muni d'un repère orthonormé.

---

## 1. Coordonnées et vecteurs

### Coordonnées d'un point

Un point $A$ du plan est repéré par ses deux coordonnées : $A(x_A\ ;\ y_A)$.

**Exemple :** $A(1\ ;\ 2)$ est le point d'abscisse $1$ et d'ordonnée $2$.

### Coordonnées d'un vecteur

Les coordonnées du vecteur $\overrightarrow{AB}$ se calculent en faisant « arrivée moins départ » :

$$\overrightarrow{AB}\begin{pmatrix} x_B - x_A \\ y_B - y_A \end{pmatrix}$$

**Exemple :** avec $A(1\ ;\ 2)$ et $B(4\ ;\ 6)$ : $\overrightarrow{AB}\begin{pmatrix} 4 - 1 \\ 6 - 2 \end{pmatrix} = \begin{pmatrix} 3 \\ 4 \end{pmatrix}$.

### Opérations sur les vecteurs

Pour $\vec{u}\begin{pmatrix} x \\ y \end{pmatrix}$, $\vec{v}\begin{pmatrix} x' \\ y' \end{pmatrix}$ et un réel $k$ :

- **somme :** $\vec{u} + \vec{v}\begin{pmatrix} x + x' \\ y + y' \end{pmatrix}$ ;
- **multiplication par un réel :** $k\vec{u}\begin{pmatrix} kx \\ ky \end{pmatrix}$ ;
- **norme (longueur) :** $\|\vec{u}\| = \sqrt{x^2 + y^2}$.

**Exemple :** avec $\vec{u}\begin{pmatrix} 3 \\ 4 \end{pmatrix}$ et $\vec{v}\begin{pmatrix} -1 \\ 2 \end{pmatrix}$ :

- $\vec{u} + \vec{v}\begin{pmatrix} 2 \\ 6 \end{pmatrix}$ ;
- $2\vec{u}\begin{pmatrix} 6 \\ 8 \end{pmatrix}$ ;
- $\|\vec{u}\| = \sqrt{9 + 16} = 5$.

---

## 2. Colinéarité

### Reconnaître deux vecteurs colinéaires

Deux vecteurs non nuls sont **colinéaires** lorsqu'ils ont la même direction : l'un s'obtient en multipliant l'autre par un réel $k$. Soit :

$$\vec{v} = k\,\vec{u}$$

$\vec{u}\begin{pmatrix} x \\ y \end{pmatrix}$ et $\vec{v}\begin{pmatrix} x' \\ y' \end{pmatrix}$ sont colinéaires si et seulement si :

$$x\,y' - x'\,y = 0$$

**Exemple 1 :** $\vec{u}\begin{pmatrix} 2 \\ 3 \end{pmatrix}$ et $\vec{v}\begin{pmatrix} 4 \\ 6 \end{pmatrix}$ : $2 \times 6 - 4 \times 3 = 12 - 12 = 0$. Ils sont colinéaires (et $\vec{v} = 2\vec{u}$).

**Exemple 2 :** $\vec{u}\begin{pmatrix} 2 \\ 3 \end{pmatrix}$ et $\vec{w}\begin{pmatrix} 4 \\ 5 \end{pmatrix}$ : $2 \times 5 - 4 \times 3 = -2 \neq 0$. Ils ne sont pas colinéaires.

Remarque : $\vec{u}$ et $\vec{v}$ sont colinéaires si $x$ et $x'$ sont proportionnelles et si $y$ et $y'$ sont proportionnelles.

**Exemple 1 :** $\vec{u}\begin{pmatrix} 2 \\ 3 \end{pmatrix}$ et $\vec{v}\begin{pmatrix} 4 \\ 6 \end{pmatrix}$ : $x$ et $x'$ a pour coefficient de proportionnalité 2, de même pour $y$ et $y'$.

### Utiliser la colinéarité

La colinéarité sert à démontrer deux choses :

- **trois points sont alignés** : $A$, $B$, $C$ sont alignés si $\overrightarrow{AB}$ et $\overrightarrow{AC}$ sont colinéaires ;
- **deux droites sont parallèles** : $(AB)$ et $(CD)$ sont parallèles si $\overrightarrow{AB}$ et $\overrightarrow{CD}$ sont colinéaires.

**Exemple :** $A(1\ ;\ 1)$, $B(3\ ;\ 2)$ et $C(7\ ;\ 4)$.

$\overrightarrow{AB}\begin{pmatrix} 2 \\ 1 \end{pmatrix}$ et $\overrightarrow{AC}\begin{pmatrix} 6 \\ 3 \end{pmatrix}$ : le coefficient de proportionnalité entre $x$ et $x'$ et $y$ et $y'$ est $3$. Les vecteurs sont colinéaires : les points $A$, $B$ et $C$ sont alignés.

---

## 3. Produit scalaire

### Calcul du produit scalaire

Le **produit scalaire** de deux vecteurs $\vec{u}$ et $\vec{v}$ est un **nombre**, noté $\vec{u} \cdot \vec{v}$. Il se calcule de deux façons.

**Avec les coordonnées :** pour $\vec{u}\begin{pmatrix} x \\ y \end{pmatrix}$ et $\vec{v}\begin{pmatrix} x' \\ y' \end{pmatrix}$ :

$$\vec{u} \cdot \vec{v} = x\,x' + y\,y'$$

**Avec les normes et l'angle :**

$$\vec{u} \cdot \vec{v} = \|\vec{u}\| \times \|\vec{v}\| \times \cos(\widehat{\vec{u}, \vec{v}})$$

**Exemple :** $\vec{u}\begin{pmatrix} 1 \\ 2 \end{pmatrix}$ et $\vec{v}\begin{pmatrix} 3 \\ 1 \end{pmatrix}$.

- Avec les coordonnées : $\vec{u} \cdot \vec{v} = 1 \times 3 + 2 \times 1 = 5$.
- Pour trouver l'angle, on utilise $\|\vec{u}\| = \sqrt{5}$ et $\|\vec{v}\| = \sqrt{10}$ : $\cos(\widehat{\vec{u}, \vec{v}}) = \dfrac{5}{\sqrt{5} \times \sqrt{10}} = \dfrac{5}{\sqrt{50}} \approx 0{,}707$, soit un angle d'environ $45^\circ$.

### Reconnaître les vecteurs orthogonaux

Deux vecteurs sont **orthogonaux** (leurs directions forment un angle droit) si et seulement si leur produit scalaire est nul :

$$\vec{u} \perp \vec{v} \iff \vec{u} \cdot \vec{v} = 0$$

**Exemple :** $\vec{u}\begin{pmatrix} 2 \\ 3 \end{pmatrix}$ et $\vec{v}\begin{pmatrix} -3 \\ 2 \end{pmatrix}$ : $\vec{u} \cdot \vec{v} = 2 \times (-3) + 3 \times 2 = -6 + 6 = 0$. Les vecteurs sont orthogonaux.
