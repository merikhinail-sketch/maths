# Variables aléatoires

Cette fiche explique comment transformer une expérience aléatoire en nombres, puis comment résumer ces nombres avec trois indicateurs : l'espérance, la variance et l'écart-type. Un même jeu sert d'exemple tout du long.

**Le jeu :** on lance un dé équilibré à 6 faces. On gagne :

- 4 € si on obtient 6 ;
- 1 € si on obtient 4 ou 5 ;
- on perd 1 € (gain de $-1$) si on obtient 1, 2 ou 3.

---

## 1. Variable aléatoire

### Définition

Une **variable aléatoire** $X$ est une fonction qui associe un nombre réel à chaque issue, chaque possibilité d'une expérience aléatoire.

Dans notre jeu, $X$ désigne le gain en euros. Elle transforme chaque résultat du dé en un nombre.

### Associer à chaque issue une valeur

Pour chaque issue possible, indiquer la valeur prise par $X$ :

| Issue (résultat du dé) | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|
| Valeur de $X$ |    $-1$ | $-1$ | $-1$ | $1$ | $1$ | $4$ |

Plusieurs issues peuvent donner la même valeur : ici, les issues 1, 2 et 3 donnent toutes $-1$.

L'écriture $(X = 1)$ désigne l'événement « $X$ prend la valeur 1 », c'est-à-dire l'ensemble des issues qui donnent 1 : ici $\{4\ ;\ 5\}$.

---

## 2. Loi de probabilité

### Déterminer la loi d'une variable aléatoire

La **loi de probabilité** de $X$ donne, pour chaque valeur possible $x_i$, la probabilité $P(X = x_i)$.

Méthode en trois temps :

1. **Lister les valeurs** prises par $X$ : ici $-1$, $1$ et $4$.
2. **Pour chaque valeur**, repérer les issues qui y mènent.
3. **Additionner** les probabilités de ces issues.

Chaque face du dé a une probabilité de $\dfrac{1}{6}$, donc :

- $P(X = -1) = P(\{1\ ;\ 2\ ;\ 3\}) = \dfrac{3}{6} = \dfrac{1}{2}$
- $P(X = 1) = P(\{4\ ;\ 5\}) = \dfrac{2}{6} = \dfrac{1}{3}$
- $P(X = 4) = P(\{6\}) = \dfrac{1}{6}$

On présente la loi dans un tableau :

| $x_i$ | $-1$ | $1$ | $4$ |
|---|---|---|---|
| $P(X = x_i)$ | $\dfrac{1}{2}$ | $\dfrac{1}{3}$ | $\dfrac{1}{6}$ |

**Vérification indispensable :** la somme des probabilités doit valoir 1.

$$\frac{1}{2} + \frac{1}{3} + \frac{1}{6} = \frac{3}{6} + \frac{2}{6} + \frac{1}{6} = 1$$

### Représenter les probabilités

La loi se représente par un **diagramme en bâtons** :

- placer les valeurs $x_i$ sur l'axe horizontal ;
- au-dessus de chaque valeur, tracer un bâton dont la hauteur est $P(X = x_i)$.

Pour notre jeu : trois bâtons, en $-1$ (hauteur $\frac{1}{2}$), en $1$ (hauteur $\frac{1}{3}$) et en $4$ (hauteur $\frac{1}{6}$). Plus le bâton est haut, plus la valeur est probable.

---

## 3. Espérance, variance et écart-type

### Calculer ces indicateurs

**Espérance.** Multiplier chaque valeur par sa probabilité, puis additionner :

$$E(X) = \sum x_i \times P(X = x_i)$$

$$E(X) = (-1) \times \frac{1}{2} + 1 \times \frac{1}{3} + 4 \times \frac{1}{6} = -\frac{1}{2} + \frac{1}{3} + \frac{2}{3} = \frac{1}{2}$$

**Variance.** La variance mesure à quel point les gains s'éloignent de la moyenne, ici $E(X) = 0{,}5$. Le calcul se fait en trois étapes.

**Étape 1 : Regarder de combien chaque gain s'éloigne de la moyenne, puis mettre cet écart au carré.** Le carré évite que les écarts négatifs et positifs s'annulent.

- Gain $-1$ : écart de $-1 - 0{,}5 = -1{,}5$, au carré : $2{,}25$.
- Gain $1$ : écart de $1 - 0{,}5 = 0{,}5$, au carré : $0{,}25$.
- Gain $4$ : écart de $4 - 0{,}5 = 3{,}5$, au carré : $12{,}25$.

**Étape 2 : Multiplier chaque carré par la probabilité du gain**, comme pour l'espérance.

- $2{,}25 \times \dfrac{1}{2} = 1{,}125$
- $0{,}25 \times \dfrac{1}{3} \approx 0{,}083$
- $12{,}25 \times \dfrac{1}{6} \approx 2{,}042$

**Étape 3 : Additionner.**

$$V(X) = 1{,}125 + 0{,}083 + 2{,}042 = 3{,}25$$

En résumé : $V(X) = \sum P(X = x_i) \times \left(x_i - E(X)\right)^2$.

**Écart-type.** La variance est en « euros au carré », ce qui ne parle pas beaucoup. Pour revenir à des euros, prendre la racine carrée :

$$\sigma(X) = \sqrt{V(X)} = \sqrt{3{,}25} \approx 1{,}80$$

### Interpréter les résultats

- **L'espérance** est la valeur moyenne de $X$ si l'on répète l'expérience un très grand nombre de fois. Ici, $E(X) = 0{,}5$ : en jouant un grand nombre de parties, on gagne en moyenne 0,50 € par partie. Le jeu est favorable au joueur.
- **L'écart-type** mesure la dispersion des valeurs autour de l'espérance, avec la même unité que $X$ (ici des euros). Plus il est grand, plus les gains varient d'une partie à l'autre. Ici, $\sigma \approx 1{,}80$ € : un gain typique s'écarte d'environ 1,80 € du gain moyen.
- **La variance** donne la même information, mais en euros au carré : elle sert surtout de calcul intermédiaire.

---

## 4. Erreurs fréquentes

### Confondre une valeur de $X$ avec sa probabilité

Une valeur de $X$ est un nombre pris par la variable ; sa probabilité est un nombre entre 0 et 1.

Dans notre jeu, la valeur $4$ est un gain ; sa probabilité est $P(X = 4) = \dfrac{1}{6}$. Ne pas écrire $P(X = 4) = 4$.

### Oublier que la somme des probabilités vaut 1

Après avoir construit la loi, additionner toutes les probabilités. Si le total n'est pas 1, une valeur ou un calcul est faux.

Un tableau qui donne $0{,}2$, $0{,}5$ et $0{,}2$ a pour total $0{,}9$ : il manque une valeur ou une probabilité.

### Mal calculer l'espérance

Ne pas oublier de **multiplier chaque valeur par sa probabilité** avant d'additionner.

Additionner seulement les valeurs, $-1 + 1 + 4 = 4$, est faux. Le bon calcul est $(-1) \times \dfrac{1}{2} + 1 \times \dfrac{1}{3} + 4 \times \dfrac{1}{6} = \dfrac{1}{2}$.

### Confondre variance et écart-type

Ce sont deux indicateurs différents, liés par une racine carrée.

Dans notre jeu, $V(X) = 3{,}25$ et $\sigma(X) \approx 1{,}80$.

### Oublier de prendre la racine carrée pour passer de la variance à l'écart-type

Si le calcul s'arrête à $3{,}25$, c'est la variance que l'on a obtenue, pas l'écart-type. L'écart-type est $\sqrt{3{,}25} \approx 1{,}80$.

### Mal interpréter l'espérance

L'espérance est une moyenne : ce n'est pas forcément une valeur que la variable peut réellement prendre.

Ici, $E(X) = 0{,}5$, alors que les gains possibles sont seulement $-1$, $1$ et $4$. On ne gagne jamais 0,50 € lors d'une partie ; c'est la moyenne de nombreuses parties.
