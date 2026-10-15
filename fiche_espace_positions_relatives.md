# Positions relatives

Dans l'espace, deux droites, une droite et un plan, ou deux plans peuvent se placer de plusieurs façons les uns par rapport aux autres. Cette fiche donne les cas possibles et une méthode pour reconnaître ces cas.

**Comment les objets sont donnés.**

- Une **droite** $(d)$ est donnée par un point $A$ et un vecteur directeur $\vec{u}\begin{pmatrix} a \\ b \\ c \end{pmatrix}$. Ses points $M(x\ ;\ y\ ;\ z)$ sont décrits par une **représentation paramétrique**, avec un paramètre réel $t$ :

$$\begin{cases} x = x_A + a\,t \\ y = y_A + b\,t \\ z = z_A + c\,t \end{cases}$$

- Un **plan** $(P)$ est donné par une **équation cartésienne** $ax + by + cz + d = 0$. Le vecteur $\vec{n}\begin{pmatrix} a \\ b \\ c \end{pmatrix}$ est un vecteur normal du plan (il est perpendiculaire au plan : voir la fiche suivante).

---

## 1. Positions relatives de deux droites

### Les quatre cas

- **Droites parallèles** (distinctes) : elles sont dans un même plan et ne se coupent pas.
- **Droites confondues** : ce sont les mêmes droites.
- **Droites sécantes** : elles se coupent en **un seul point**.
- **Droites non coplanaires** : il n'existe aucun plan qui contienne les deux droites ; elles ne se coupent pas et ne sont pas parallèles.

### Comment déterminer la position de deux droites

Soient $(d)$ de vecteur directeur $\vec{u}$, passant par $A$, et $(d')$ de vecteur directeur $\vec{v}$.

**Étape 1 : comparer les directions.** Les vecteurs $\vec{u}$ et $\vec{v}$ sont-ils colinéaires ?

**Si oui**, les droites sont parallèles ou confondues. Tester si un point de $(d')$ appartient à $(d)$ :

- si oui, les droites sont **confondues** ;
- sinon, elles sont **parallèles** (distinctes).

**Si non**, les droites sont sécantes ou non coplanaires. Chercher un **point commun** : écrire l'égalité des coordonnées avec deux paramètres différents $t$ et $s$, puis résoudre le système :

- si le système a une solution, les droites sont **sécantes** ;
- s'il n'en a pas, elles sont **non coplanaires**.

### Exemples

Soit $(d)$ la droite de représentation paramétrique $\begin{cases} x = 1 + t \\ y = 2t \\ z = 2 - t \end{cases}$, c'est-à-dire passant par $A(1\ ;\ 0\ ;\ 2)$ de vecteur directeur $\vec{u}\begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix}$.

**Parallèles ou confondues.** $(d_1)$ passe par $B(0\ ;\ 1\ ;\ 3)$ et a pour vecteur directeur $\vec{v}\begin{pmatrix} 2 \\ 4 \\ -2 \end{pmatrix}$.

- $\vec{v} = 2\vec{u}$ : directions colinéaires.
- Le point $B$ est-il sur $(d)$ ? On a $\overrightarrow{AB}\begin{pmatrix} -1 \\ 1 \\ 1 \end{pmatrix}$ ; cherchons $t$ tel que $\overrightarrow{AB} = t\vec{u}$ : la première coordonnée donne $t = -1$, mais alors la deuxième serait $-2 \neq 1$. Non.

Les droites $(d)$ et $(d_1)$ sont **parallèles** (distinctes). Avec le point $B'(3\ ;\ 4\ ;\ 0)$ à la place de $B$ : $\overrightarrow{AB'}\begin{pmatrix} 2 \\ 4 \\ -2 \end{pmatrix} = 2\vec{u}$, donc $B' \in (d)$ et les droites seraient **confondues**.

**Sécantes.** $(d_2)$ de représentation $\begin{cases} x = 2 + s \\ y = 2 - s \\ z = 1 + 2s \end{cases}$, de vecteur directeur $\begin{pmatrix} 1 \\ -1 \\ 2 \end{pmatrix}$, non colinéaire à $\vec{u}$.

Chercher un point commun :

$$\begin{cases} 1 + t = 2 + s \\ 2t = 2 - s \\ 2 - t = 1 + 2s \end{cases}$$

Les deux premières équations donnent $t - s = 1$ et $2t + s = 2$ ; en additionnant, $3t = 3$, donc $t = 1$ et $s = 0$. Vérification avec la troisième : $2 - 1 = 1$ et $1 + 0 = 1$ ✓.

Les droites sont **sécantes** au point obtenu avec $t = 1$ : $(2\ ;\ 2\ ;\ 1)$.

**Non coplanaires.** $(d_3)$ de représentation $\begin{cases} x = 2 + s \\ y = 2 - s \\ z = 3 + 2s \end{cases}$ (même direction que $(d_2)$).

Les deux premières équations restent $t = 1$ et $s = 0$. La troisième devient $2 - t = 3 + 2s$ : avec $t = 1$ et $s = 0$, on obtient $1 = 3$ ✗. Le système n'a pas de solution : les droites $(d)$ et $(d_3)$ sont **non coplanaires**.

---

## 2. Position relative d'une droite et d'un plan

### Les trois cas

- **Droite contenue dans le plan** : tous ses points sont dans le plan.
- **Droite parallèle au plan** (sans être contenue) : elle ne rencontre pas le plan.
- **Droite sécante au plan** : elle le coupe en **un seul point**.

### Comment déterminer la position à partir des équations disponibles

Remplacer $x$, $y$ et $z$ de la représentation paramétrique de la droite dans l'équation du plan. On obtient une équation d'inconnue $t$, qui se réduit à la forme $\alpha\,t + \beta = 0$ :

- si $\alpha \neq 0$ : une **seule** solution $t$, donc la droite est **sécante** au plan en un point ;
- si $\alpha = 0$ et $\beta \neq 0$ : **aucune** solution, donc la droite est **parallèle** au plan (et non contenue) ;
- si $\alpha = 0$ et $\beta = 0$ : **toutes** les valeurs de $t$ conviennent, donc la droite est **contenue** dans le plan.

### Exemples

Soit $(P)$ le plan d'équation $x + 2y - z - 3 = 0$.

**Sécante.** $(d)$ : $\begin{cases} x = 1 + t \\ y = 2t \\ z = 2 - t \end{cases}$.

$$(1 + t) + 2(2t) - (2 - t) - 3 = 1 + t + 4t - 2 + t - 3 = 6t - 4$$

L'équation $6t - 4 = 0$ a une unique solution, $t = \dfrac{2}{3}$. La droite $(d)$ est **sécante** à $(P)$.

**Parallèle.** $(d_4)$ : $\begin{cases} x = 1 + t \\ y = 1 \\ z = -1 + t \end{cases}$.

$$(1 + t) + 2 \times 1 - (-1 + t) - 3 = 1 + t + 2 + 1 - t - 3 = 1$$

L'équation $1 = 0$ est impossible : la droite $(d_4)$ est **parallèle** à $(P)$, sans y être contenue.

**Contenue.** $(d_5)$ : $\begin{cases} x = 1 + t \\ y = 1 \\ z = t \end{cases}$.

$$(1 + t) + 2 \times 1 - t - 3 = 0$$

L'égalité $0 = 0$ est vraie pour tout $t$ : la droite $(d_5)$ est **contenue** dans $(P)$.

---

## 3. Positions relatives de deux plans

### Les trois cas

- **Plans parallèles** (distincts) : ils ne se coupent pas.
- **Plans confondus** : ce sont les mêmes plans.
- **Plans sécants** : ils se coupent selon une **droite**.

### Comment déterminer leur position relative

Soient $(P) : ax + by + cz + d = 0$ et $(P') : a'x + b'y + c'z + d' = 0$, de vecteurs normaux $\vec{n}$ et $\vec{n'}$.

**Étape 1 : comparer les vecteurs normaux.** Sont-ils colinéaires ?

**Si oui**, les plans sont parallèles ou confondus :

- si les équations sont **proportionnelles** (y compris le terme constant), les plans sont **confondus** ;
- sinon, ils sont **parallèles** (distincts).

**Si non**, les plans sont **sécants** selon une droite.

### Exemples

Soit $(P) : x + 2y - z - 3 = 0$, de vecteur normal $\vec{n}\begin{pmatrix} 1 \\ 2 \\ -1 \end{pmatrix}$.

**Confondus.** $(P_1) : 2x + 4y - 2z - 6 = 0$. Chaque coefficient de $(P_1)$ vaut $2$ fois celui de $(P)$, terme constant compris : les plans sont **confondus**.

**Parallèles.** $(P_2) : 2x + 4y - 2z - 1 = 0$. Les vecteurs normaux sont colinéaires ($2\vec{n}$), mais le terme constant ne suit pas ($-1 \neq 2 \times (-3)$) : les plans sont **parallèles** (distincts).

**Sécants.** $(P_3) : x - y + z = 0$, de vecteur normal $\begin{pmatrix} 1 \\ -1 \\ 1 \end{pmatrix}$, non colinéaire à $\vec{n}$ : les plans sont **sécants** selon une droite.

Pour trouver cette droite, résoudre le système $\begin{cases} x + 2y - z = 3 \\ x - y + z = 0 \end{cases}$. En additionnant, $2x + y = 3$, donc $y = 3 - 2x$. La deuxième équation donne $z = y - x = 3 - 3x$. En posant $x = s$, la droite d'intersection a pour représentation paramétrique :

$$\begin{cases} x = s \\ y = 3 - 2s \\ z = 3 - 3s \end{cases}$$
