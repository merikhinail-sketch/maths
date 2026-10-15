# Orthogonalité dans l'espace

Cette fiche étend le produit scalaire à l'espace, puis l'utilise pour parler de droites orthogonales, de plans perpendiculaires et de projections orthogonales.

Dans toute la fiche, l'espace est muni d'un repère orthonormé.

---

## 1. Produit scalaire dans l'espace

### Définition et calcul du produit scalaire

Comme dans le plan, le **produit scalaire** de deux vecteurs $\vec{u}$ et $\vec{v}$ est un nombre, noté $\vec{u} \cdot \vec{v}$ :

$$\vec{u} \cdot \vec{v} = \|\vec{u}\| \times \|\vec{v}\| \times \cos(\widehat{\vec{u}, \vec{v}})$$

où $\widehat{\vec{u}, \vec{v}}$ est l'angle entre les deux vecteurs (ils sont toujours dans un même plan, même dans l'espace).

### Calcul à partir des coordonnées

Pour $\vec{u}\begin{pmatrix} x \\ y \\ z \end{pmatrix}$ et $\vec{v}\begin{pmatrix} x' \\ y' \\ z' \end{pmatrix}$ :

$$\vec{u} \cdot \vec{v} = x\,x' + y\,y' + z\,z'$$

La norme d'un vecteur se calcule avec la même idée : $\|\vec{u}\| = \sqrt{\vec{u} \cdot \vec{u}} = \sqrt{x^2 + y^2 + z^2}$.

**Exemple :** $\vec{u}\begin{pmatrix} 1 \\ 2 \\ 3 \end{pmatrix}$ et $\vec{v}\begin{pmatrix} 2 \\ -1 \\ 1 \end{pmatrix}$.

$$\vec{u} \cdot \vec{v} = 1 \times 2 + 2 \times (-1) + 3 \times 1 = 2 - 2 + 3 = 3$$

### Interprétation du signe et du résultat

Le signe du produit scalaire renseigne sur l'angle $\theta$ entre les vecteurs (non nuls) :

- $\vec{u} \cdot \vec{v} > 0$ : l'angle est **aigu** ($\cos \theta > 0$) ;
- $\vec{u} \cdot \vec{v} < 0$ : l'angle est **obtus** ($\cos \theta < 0$) ;
- $\vec{u} \cdot \vec{v} = 0$ : l'angle est **droit**.

On peut aussi retrouver l'angle : $\cos \theta = \dfrac{\vec{u} \cdot \vec{v}}{\|\vec{u}\| \times \|\vec{v}\|}$.

**Exemple :** pour les vecteurs précédents, $\|\vec{u}\| = \sqrt{14}$ et $\|\vec{v}\| = \sqrt{6}$, donc $\cos \theta = \dfrac{3}{\sqrt{84}} \approx 0{,}327$. Le produit scalaire est positif : l'angle est aigu, d'environ $71^\circ$.

### Lien entre produit scalaire nul et orthogonalité

Deux vecteurs sont **orthogonaux** si et seulement si leur produit scalaire est nul :

$$\vec{u} \perp \vec{v} \iff \vec{u} \cdot \vec{v} = 0$$

Le vecteur nul est considéré comme orthogonal à tous les vecteurs.

---

## 2. Orthogonalité des droites et des vecteurs

### Vecteurs orthogonaux

**Exemple :** $\vec{u}\begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix}$ et $\vec{v}\begin{pmatrix} 3 \\ 0 \\ 3 \end{pmatrix}$.

$\vec{u} \cdot \vec{v} = 3 + 0 - 3 = 0$. Les vecteurs sont orthogonaux.

### Deux droites orthogonales

Deux droites de l'espace sont **orthogonales** lorsque leurs **vecteurs directeurs sont orthogonaux**. Cette définition ne demande pas que les droites se coupent.

### Comment vérifier l'orthogonalité à partir des vecteurs directeurs

1. Repérer un vecteur directeur $\vec{u}$ de la première droite et $\vec{v}$ de la seconde.
2. Calculer $\vec{u} \cdot \vec{v}$.
3. Si le résultat est $0$, les droites sont orthogonales ; sinon, elles ne le sont pas.

### Attention à la différence entre orthogonales et perpendiculaires dans l'espace

- Deux droites sont **orthogonales** si leurs directions forment un angle droit.
- Deux droites sont **perpendiculaires** si elles sont orthogonales **et sécantes** (elles se coupent).

Deux droites perpendiculaires sont donc orthogonales, mais deux droites orthogonales ne sont pas toujours perpendiculaires.

**Exemple :** dans le cube $ABCDEFGH$, avec le repère $\left(A\ ;\ \overrightarrow{AB},\ \overrightarrow{AD},\ \overrightarrow{AE}\right)$, on a $A(0\ ;\ 0\ ;\ 0)$, $B(1\ ;\ 0\ ;\ 0)$, $C(1\ ;\ 1\ ;\ 0)$ et $G(1\ ;\ 1\ ;\ 1)$.

- $\overrightarrow{AB}\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}$ et $\overrightarrow{CG}\begin{pmatrix} 0 \\ 0 \\ 1 \end{pmatrix}$ : $\overrightarrow{AB} \cdot \overrightarrow{CG} = 0$. Les droites $(AB)$ et $(CG)$ sont **orthogonales**.
- Mais elles ne se coupent pas ($(AB)$ a pour équations $y = 0$ et $z = 0$ ; $(CG)$ a pour équations $x = 1$ et $y = 1$ : aucun point commun). Elles ne sont donc **pas perpendiculaires**.

---

## 3. Droite et plan

### Droite orthogonale à un plan

Une droite $(d)$ est **orthogonale à un plan** $(P)$ lorsqu'elle est orthogonale à **toutes** les droites de $(P)$.

### Critère permettant de montrer qu'une droite est orthogonale à un plan

Il suffit de vérifier l'orthogonalité avec **deux directions non colinéaires** du plan.

**Critère.** Soit $\vec{u}$ un vecteur directeur de $(d)$, et soient $\vec{v_1}$ et $\vec{v_2}$ deux vecteurs non colinéaires dirigeant $(P)$. Si $\vec{u} \cdot \vec{v_1} = 0$ et $\vec{u} \cdot \vec{v_2} = 0$, alors $(d)$ est orthogonale à $(P)$.

**Exemple :** $(P)$ est le plan passant par $A(0\ ;\ 0\ ;\ 0)$ dirigé par $\vec{v_1}\begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix}$ et $\vec{v_2}\begin{pmatrix} 0 \\ 1 \\ -1 \end{pmatrix}$, et $\vec{u}\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$.

- $\vec{u} \cdot \vec{v_1} = 1 - 1 + 0 = 0$ ;
- $\vec{u} \cdot \vec{v_2} = 0 + 1 - 1 = 0$.

Toute droite de vecteur directeur $\vec{u}$ est orthogonale à $(P)$.

### Utilisation des vecteurs normaux

Un **vecteur normal** à un plan $(P)$ est un vecteur non nul orthogonal à ce plan, c'est-à-dire un vecteur directeur d'une droite orthogonale à $(P)$. Dans l'exemple précédent, $\vec{n}\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$ est un vecteur normal à $(P)$.

**Équation d'un plan.** Le plan passant par $A(x_A\ ;\ y_A\ ;\ z_A)$ et de vecteur normal $\vec{n}\begin{pmatrix} a \\ b \\ c \end{pmatrix}$ est l'ensemble des points $M$ tels que $\overrightarrow{AM} \cdot \vec{n} = 0$, soit :

$$a(x - x_A) + b(y - y_A) + c(z - z_A) = 0$$

On en tire une équation de la forme $ax + by + cz + d = 0$. Les coefficients de $x$, $y$ et $z$ donnent donc directement un vecteur normal.

**Exemple :** plan passant par $A(1\ ;\ 0\ ;\ 2)$ de vecteur normal $\vec{n}\begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix}$.

$$(x - 1) + 2y - (z - 2) = 0 \iff x + 2y - z + 1 = 0$$

Vérification : pour $A$, $1 + 0 - 2 + 1 = 0$ ✓.

### Plans perpendiculaires

Deux plans sont **perpendiculaires** lorsque leurs **vecteurs normaux sont orthogonaux**.

**Exemple :** $(P) : x + y + z = 0$ (normal $\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$) et $(P') : x - y = 0$ (normal $\begin{pmatrix} 1 \\ -1 \\ 0 \end{pmatrix}$).

Produit scalaire des vecteurs normaux : $1 - 1 + 0 = 0$. Les plans $(P)$ et $(P')$ sont perpendiculaires.

---

## 4. Projection orthogonale

### Projection orthogonale d'un point sur une droite

Soit $(d)$ une droite de vecteur directeur $\vec{u}$ et $M$ un point. Le **projeté orthogonal** de $M$ sur $(d)$ est le point $H$ de $(d)$ tel que $\overrightarrow{MH}$ est orthogonal à $\vec{u}$. C'est le point de $(d)$ **le plus proche** de $M$.

### Projection orthogonale d'un point sur un plan

Soit $(P)$ un plan de vecteur normal $\vec{n}$ et $M$ un point. Le **projeté orthogonal** de $M$ sur $(P)$ est le point $H$ de $(P)$ tel que $\overrightarrow{MH}$ est colinéaire à $\vec{n}$. C'est le point de $(P)$ **le plus proche** de $M$.

### Reconnaître et construire une projection orthogonale

Pour **construire** le projeté, il y a deux méthodes, selon l'objet.

**Sur une droite.** Soit $A \in (d)$. Écrire $H = A + t\,\vec{u}$ (un point de $(d)$ avec un paramètre $t$), puis imposer $\overrightarrow{MH} \cdot \vec{u} = 0$. On obtient une équation en $t$.

*Exemple :* $(d)$ passant par $A(1\ ;\ 0\ ;\ 1)$ de vecteur directeur $\vec{u}\begin{pmatrix} 1 \\ 1 \\ 0 \end{pmatrix}$, et $M(3\ ;\ 0\ ;\ 3)$.

Le point $H$ a pour coordonnées $(1 + t\ ;\ t\ ;\ 1)$. Donc $\overrightarrow{MH}\begin{pmatrix} t - 2 \\ t \\ -2 \end{pmatrix}$. La condition $\overrightarrow{MH} \cdot \vec{u} = 0$ donne :

$$(t - 2) + t + 0 = 0 \iff t = 1$$

Le projeté est $H(2\ ;\ 1\ ;\ 1)$.

**Sur un plan.** Écrire $H = M + k\,\vec{n}$ (on part de $M$ dans la direction normale), puis imposer que $H$ vérifie l'équation du plan. On obtient une équation en $k$.

*Exemple :* $(P) : x + y + z - 3 = 0$, de vecteur normal $\vec{n}\begin{pmatrix} 1 \\ 1 \\ 1 \end{pmatrix}$, et $M(2\ ;\ 2\ ;\ 2)$.

Le point $H$ a pour coordonnées $(2 + k\ ;\ 2 + k\ ;\ 2 + k)$. Dans l'équation du plan :

$$3(2 + k) - 3 = 0 \iff 3 + 3k = 0 \iff k = -1$$

Le projeté est $H(1\ ;\ 1\ ;\ 1)$.

### Lien entre projection orthogonale et perpendicularité

Si $M$ n'est pas sur la droite $(d)$, la droite $(MH)$ est **perpendiculaire** à $(d)$ : elle est orthogonale à $(d)$ et elles se coupent en $H$.

Pour un plan, la droite $(MH)$ est **orthogonale au plan** $(P)$.

### Utilisation de la projection pour déterminer des longueurs/distances

La **distance** d'un point $M$ à une droite ou à un plan est la longueur $MH$, où $H$ est le projeté orthogonal de $M$.

**Exemples :**

- distance de $M(3\ ;\ 0\ ;\ 3)$ à la droite $(d)$ de l'exemple précédent : $\overrightarrow{MH}\begin{pmatrix} -1 \\ 1 \\ -2 \end{pmatrix}$ (avec $H(2\ ;\ 1\ ;\ 1)$), donc $MH = \sqrt{1 + 1 + 4} = \sqrt{6}$ ;
- distance de $M(2\ ;\ 2\ ;\ 2)$ au plan $(P)$ : $\overrightarrow{MH}\begin{pmatrix} -1 \\ -1 \\ -1 \end{pmatrix}$, donc $MH = \sqrt{3}$.
