# Représentations paramétriques d'une droite

Une représentation paramétrique décrit **tous les points d'une droite** à l'aide d'un seul nombre $t$, appelé paramètre. Cette fiche déroule un grand exemple, question par question, en expliquant chaque étape.

Dans toute la fiche, l'espace est muni d'un repère orthonormé.

---

## Grand exemple guidé

**Énoncé.** On considère les points $A(1\ ;\ 2\ ;\ -1)$ et $B(3\ ;\ 1\ ;\ 1)$, et le plan $(P)$ d'équation $x + y + z - 4 = 0$.

1. Déterminer une représentation paramétrique de la droite $(AB)$.
2. Les points $C(5\ ;\ 0\ ;\ 3)$ et $D(0\ ;\ 3\ ;\ 0)$ appartiennent-ils à $(AB)$ ?
3. Déterminer l'intersection de la droite $(AB)$ et du plan $(P)$.
4. Déterminer le projeté orthogonal du point $M(6\ ;\ 2\ ;\ 3)$ sur la droite $(AB)$, puis la distance de $M$ à cette droite.

### Question 1 : écrire une représentation paramétrique

**L'idée.** Pour décrire une droite, il faut deux choses : **un point** et **une direction** (un vecteur directeur). Un point $M(x\ ;\ y\ ;\ z)$ est sur la droite lorsqu'on y arrive en partant du point de départ $A$ et en avançant dans la direction $\vec{u}$, d'un certain multiple $t$ :

$$\overrightarrow{AM} = t\,\vec{u}$$

**Étape 1 : choisir le point et le vecteur directeur.** On prend $A$ comme point de départ. Un vecteur directeur de $(AB)$ est $\overrightarrow{AB}$ :

$$\overrightarrow{AB}\begin{pmatrix} 3 - 1 \\ 1 - 2 \\ 1 - (-1) \end{pmatrix} = \begin{pmatrix} 2 \\ -1 \\ 2 \end{pmatrix}$$

**Étape 2 : écrire l'égalité $\overrightarrow{AM} = t\,\overrightarrow{AB}$ coordonnée par coordonnée.**

$$\begin{pmatrix} x - 1 \\ y - 2 \\ z + 1 \end{pmatrix} = t\begin{pmatrix} 2 \\ -1 \\ 2 \end{pmatrix}$$

**Étape 3 : isoler $x$, $y$ et $z$.**

$$\begin{cases} x = 1 + 2t \\ y = 2 - t \\ z = -1 + 2t \end{cases} \qquad t \in \mathbb{R}$$

**Lecture :**

- pour $t = 0$, on est en $A(1\ ;\ 2\ ;\ -1)$ ;
- pour $t = 1$, on est en $B(3\ ;\ 1\ ;\ 1)$ ;
- chaque valeur de $t$ donne un point de la droite.

### Question 2 : un point est-il sur la droite ?

**L'idée.** Un point appartient à la droite s'il existe **une valeur de $t$** qui donne ses trois coordonnées à la fois.

**Pour $C(5\ ;\ 0\ ;\ 3)$.** On cherche $t$ avec la première équation :

$$5 = 1 + 2t \iff t = 2$$

Puis on **vérifie** avec les deux autres équations, pour $t = 2$ :

- $y = 2 - 2 = 0$ ✓ ;
- $z = -1 + 2 \times 2 = 3$ ✓.

Les trois coordonnées sont bonnes avec la même valeur $t = 2$ : $C$ appartient à $(AB)$.

**Pour $D(0\ ;\ 3\ ;\ 0)$.** On cherche $t$ avec la première équation :

$$0 = 1 + 2t \iff t = -\frac{1}{2}$$

Puis on vérifie avec la deuxième équation : $y = 2 - \left(-\dfrac{1}{2}\right) = \dfrac{5}{2} \neq 3$ ✗.

Les coordonnées ne correspondent pas à la même valeur de $t$ : $D$ n'appartient pas à $(AB)$.

### Question 3 : intersection de la droite et du plan

**L'idée.** Un point commun à la droite et au plan a ses coordonnées de la forme $(1 + 2t\ ;\ 2 - t\ ;\ -1 + 2t)$ **et** vérifie l'équation du plan. On remplace donc $x$, $y$, $z$ dans l'équation du plan.

**Étape 1 : remplacer.**

$$(1 + 2t) + (2 - t) + (-1 + 2t) - 4 = 0$$

**Étape 2 : développer et simplifier.**

$$1 + 2t + 2 - t - 1 + 2t - 4 = 3t - 2 = 0$$

**Étape 3 : résoudre.** $3t - 2 = 0 \iff t = \dfrac{2}{3}$.

On trouve **une seule** valeur de $t$ : la droite $(AB)$ est sécante au plan $(P)$ en un unique point.

**Étape 4 : retrouver le point.** Remplacer $t = \dfrac{2}{3}$ dans la représentation paramétrique :

$$x = 1 + \frac{4}{3} = \frac{7}{3} \qquad y = 2 - \frac{2}{3} = \frac{4}{3} \qquad z = -1 + \frac{4}{3} = \frac{1}{3}$$

Le point d'intersection est $\left(\dfrac{7}{3}\ ;\ \dfrac{4}{3}\ ;\ \dfrac{1}{3}\right)$.

**Vérification :** $\dfrac{7}{3} + \dfrac{4}{3} + \dfrac{1}{3} - 4 = \dfrac{12}{3} - 4 = 0$ ✓.

### Question 4 : projeté orthogonal et distance

**L'idée.** Le projeté orthogonal $H$ de $M$ sur $(AB)$ est le point de la droite tel que $\overrightarrow{MH}$ est **orthogonal** au vecteur directeur $\overrightarrow{AB}$. Comme $H$ est sur la droite, ses coordonnées s'écrivent avec $t$.

**Étape 1 : écrire $H$ avec le paramètre.**

$$H(1 + 2t\ ;\ 2 - t\ ;\ -1 + 2t)$$

**Étape 2 : calculer $\overrightarrow{MH}$** (arrivée moins départ, avec $M(6\ ;\ 2\ ;\ 3)$) :

$$\overrightarrow{MH}\begin{pmatrix} 1 + 2t - 6 \\ 2 - t - 2 \\ -1 + 2t - 3 \end{pmatrix} = \begin{pmatrix} 2t - 5 \\ -t \\ 2t - 4 \end{pmatrix}$$

**Étape 3 : imposer l'orthogonalité** $\overrightarrow{MH} \cdot \overrightarrow{AB} = 0$, avec $\overrightarrow{AB}\begin{pmatrix} 2 \\ -1 \\ 2 \end{pmatrix}$ :

$$2(2t - 5) + (-1)(-t) + 2(2t - 4) = 4t - 10 + t + 4t - 8 = 9t - 18 = 0$$

**Étape 4 : résoudre.** $9t - 18 = 0 \iff t = 2$.

**Étape 5 : retrouver $H$.** Pour $t = 2$ :

$$H(1 + 4\ ;\ 2 - 2\ ;\ -1 + 4) = H(5\ ;\ 0\ ;\ 3)$$

On retrouve le point $C$ de la question 2 : le projeté orthogonal de $M$ sur $(AB)$ est $C$.

**Étape 6 : calculer la distance.** C'est la longueur $MH$. Pour $t = 2$ : $\overrightarrow{MH}\begin{pmatrix} -1 \\ -2 \\ 0 \end{pmatrix}$, donc :

$$MH = \sqrt{(-1)^2 + (-2)^2 + 0^2} = \sqrt{5}$$

La distance de $M$ à la droite $(AB)$ est $\sqrt{5} \approx 2{,}24$.

**Vérification :** $\overrightarrow{MH} \cdot \overrightarrow{AB} = (-1) \times 2 + (-2) \times (-1) + 0 \times 2 = -2 + 2 + 0 = 0$ ✓.
