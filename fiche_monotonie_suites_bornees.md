# Monotonie et suites bornées


## 1. Monotonie d'une suite

### Définition monotonie

Étudier la monotonie d'une suite, c'est étudier ses variations : les termes augmentent-ils, diminuent-ils, ou ni l'un ni l'autre ?

Pour cela, on compare chaque terme $u_n$ avec le suivant $u_{n+1}$. Cette comparaison doit être vraie **pour tout entier naturel $n$**, et pas seulement pour les premiers termes.

Méthode générale : étudier le signe de la différence $u_{n+1} - u_n$.

### Suite croissante

Une suite $(u_n)$ est **croissante** si, pour tout entier naturel $n$ :

$$u_{n+1} \geq u_n$$

Elle est **strictement croissante** si, pour tout entier naturel $n$ :

$$u_{n+1} > u_n$$

Une suite constante est croissante (les termes ne diminuent jamais), mais pas strictement croissante.

**Exemple :** $u_n = n^2 + 1$.

$$u_{n+1} - u_n = (n+1)^2 + 1 - (n^2 + 1) = 2n + 1$$

Comme $2n + 1 > 0$ pour tout $n \geq 0$, la suite est strictement croissante.

### Suite décroissante

Une suite $(u_n)$ est **décroissante** si, pour tout entier naturel $n$ :

$$u_{n+1} \leq u_n$$

Elle est **strictement décroissante** si, pour tout entier naturel $n$ :

$$u_{n+1} < u_n$$

**Exemple :** $u_n = 10 - n^2$.

$$u_{n+1} - u_n = 10 - (n+1)^2 - (10 - n^2) = -(2n + 1)$$

Comme $-(2n+1) < 0$ pour tout $n \geq 0$, la suite est strictement décroissante.

### Suite monotone

Une suite est **monotone** lorsqu'elle est croissante, ou lorsqu'elle est décroissante. Dans les deux cas, elle va toujours dans le même sens.

Une suite qui monte parfois et descend parfois n'est pas monotone.

**Exemple :** $u_n = (-1)^n$ donne $1\ ;\ -1\ ;\ 1\ ;\ -1\ ;\ \dots$ Elle alterne : elle n'est ni croissante, ni décroissante, donc pas monotone.

---

## 2. Suites bornées

### Suite majorée

Une suite $(u_n)$ est **majorée** s'il existe un réel $M$ tel que, pour tout entier naturel $n$ :

$$u_n \leq M$$

Autrement dit, $M$ est un plafond : aucun terme ne passe au-dessus. Le nombre $M$ s'appelle un **majorant**. Il n'est pas unique : si 2 est un majorant, 3 en est un aussi.

**Exemple :** $u_n = 2 - \dfrac{1}{n+1}$ est majorée par 2.

### Suite minorée

Une suite $(u_n)$ est **minorée** s'il existe un réel $m$ tel que, pour tout entier naturel $n$ :

$$u_n \geq m$$

Autrement dit, $m$ est un plancher : aucun terme ne descend en dessous. Le nombre $m$ s'appelle un **minorant**.

**Exemple :** $u_n = n^2$ est minorée par 0.

### Suite bornée

Une suite est **bornée** lorsqu'elle est à la fois majorée et minorée : tous ses termes restent entre un plancher et un plafond.

$$m \leq u_n \leq M$$

**Exemple :** $u_n = (-1)^n$ ne prend que les valeurs $-1$ et $1$. Elle est minorée par $-1$ et majorée par $1$, donc bornée.

### Méthodes pour démontrer majorée/minorée

**Méthode 1 : encadrer à partir de la formule.**

Quand la suite est donnée par une formule, partir de ce que l'on sait sur $n$ et construire l'encadrement de $u_n$ pas à pas.

**Exemple :** montrer que $u_n = 2 - \dfrac{1}{n+1}$ est bornée.

Pour tout entier naturel $n$, on a $n + 1 \geq 1$, donc :

$$0 < \frac{1}{n+1} \leq 1$$

En multipliant par $-1$, l'ordre s'inverse :

$$-1 \leq -\frac{1}{n+1} < 0$$

En ajoutant 2 :

$$1 \leq u_n < 2$$

La suite est minorée par 1 et majorée par 2 : elle est bornée.

**Méthode 2 : raisonner par récurrence.**

Quand la suite est définie par une relation de la forme $u_{n+1} = f(u_n)$, procéder en trois étapes :

1. **Initialisation** : vérifier l'inégalité pour le premier terme.
2. **Hérédité** : supposer l'inégalité vraie pour $u_n$, puis en déduire qu'elle est vraie pour $u_{n+1}$.
3. **Conclusion** : l'inégalité est vraie pour tout $n$.

**Exemple :** $u_0 = 0$ et $u_{n+1} = \dfrac{u_n + 3}{2}$. Montrer que $u_n \leq 3$ pour tout $n$.

- Initialisation : $u_0 = 0 \leq 3$.
- Hérédité : supposer $u_n \leq 3$. Alors $u_n + 3 \leq 6$, donc $\dfrac{u_n + 3}{2} \leq 3$, c'est-à-dire $u_{n+1} \leq 3$.
- Conclusion : $u_n \leq 3$ pour tout entier naturel $n$. La suite est majorée par 3.

---

## 3. Lien entre monotonie et bornes

### Une suite croissante et majorée

Imagine une suite dont les termes ne font que monter, mais qui ne peut jamais dépasser un plafond $M$. Elle ne peut donc pas « partir vers l'infini » : ses termes montent de plus en plus lentement et se rapprochent d'une valeur. La fiche suivante donnera un nom à ce comportement : la **convergence**.

**Exemple :** $u_n = 2 - \dfrac{1}{n+1}$ donne $1\ ;\ 1{,}5\ ;\ 1{,}67\ ;\ 1{,}75\ ;\ \dots$ Elle est croissante et majorée par 2 : ses termes se rapprochent de 2.

La valeur dont la suite se rapproche n'est pas forcément le majorant $M$ choisi : la suite précédente est aussi majorée par 5, mais elle se rapproche de 2.

Remarque utile : une suite croissante est toujours minorée par son premier terme $u_0$. Pour une suite croissante, seule la majoration reste à démontrer.

### Une suite décroissante et minorée

Même idée dans l'autre sens : une suite dont les termes ne font que descendre, sans jamais passer sous un plancher $m$, se rapproche elle aussi d'une valeur.

**Exemple :** $u_n = \dfrac{1}{n+1}$ donne $1\ ;\ 0{,}5\ ;\ 0{,}33\ ;\ 0{,}25\ ;\ \dots$ Elle est décroissante et minorée par 0 : ses termes se rapprochent de 0.

De même, une suite décroissante est toujours majorée par son premier terme $u_0$.

### Pourquoi ces conditions sont importantes

Les deux conditions sont nécessaires : si l'une manque, la conclusion tombe.

- **Croissante, mais pas majorée** : $u_n = n$ donne $0\ ;\ 1\ ;\ 2\ ;\ 3\ ;\ \dots$ Rien ne l'arrête, elle ne se rapproche d'aucun nombre.
- **Majorée, mais pas monotone** : $u_n = (-1)^n$ est majorée par 1, mais elle alterne entre $1$ et $-1$ et ne se rapproche d'aucun nombre.

Le même raisonnement vaut pour les suites décroissantes : $u_n = -n$ est décroissante mais pas minorée, et elle n'a pas de valeur vers laquelle se rapprocher.

---

## 4. Erreurs fréquentes

### Confondre croissante et strictement croissante

Dans une suite croissante, deux termes consécutifs peuvent être égaux ($u_{n+1} = u_n$). Dans une suite strictement croissante, chaque terme est strictement plus grand que le précédent.

La suite constante $4\ ;\ 4\ ;\ 4\ ;\ \dots$ est croissante, mais pas strictement croissante.

### Montrer seulement que $u_{n+1} \geq u_n$ pour quelques valeurs et conclure pour toute la suite

Calculer les premiers termes ne prouve rien : la suite peut changer de comportement plus loin.

Avec $u_n = n(5 - n)$, les premiers termes sont $u_0 = 0$, $u_1 = 4$, $u_2 = 6$, $u_3 = 6$ : on pourrait croire la suite croissante. Pourtant $u_4 = 4$ : elle redescend.

Pour conclure, étudier le signe de $u_{n+1} - u_n$ **pour tout $n$**.

### Confondre majorée et minorée

Retenir : **majorée**, c'est un plafond ($u_n \leq M$) ; **minorée**, c'est un plancher ($u_n \geq m$).

La suite $u_n = n$ est minorée par 0, mais elle n'est pas majorée.

### Croire qu'une suite bornée est forcément monotone

Une suite peut rester coincée entre deux valeurs sans être monotone.

La suite $u_n = (-1)^n$ est bornée (entre $-1$ et $1$), mais elle alterne : elle n'est pas monotone.

### Croire qu'une suite monotone est forcément bornée

Une suite peut aller toujours dans le même sens sans jamais être arrêtée.

La suite $u_n = n$ est croissante, mais elle n'est pas majorée, donc pas bornée.
