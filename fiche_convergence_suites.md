# Convergence des suites

Cette fiche donne un nom précis à ce que l'on a observé jusqu'ici : certaines suites se rapprochent d'une valeur, d'autres non. Chaque notion est illustrée par un exemple simple.

---

## 1. Comprendre la convergence

### Idée intuitive de convergence

Une suite **converge** lorsque ses termes se rapprochent d'un nombre fixe, de plus en plus près, à mesure que $n$ grandit.

**Exemple :** $u_n = \dfrac{1}{n+1}$ donne $1\ ;\ 0{,}5\ ;\ 0{,}33\ ;\ 0{,}25\ ;\ 0{,}2\ ;\ \dots$ Les termes se rapprochent de 0 : la suite converge vers 0.

Les termes n'ont pas besoin d'être toujours du même côté du nombre visé. Voici une suite qui s'en rapproche en alternant :

**Exemple :** $u_n = 3 + \dfrac{(-1)^n}{n+1}$ donne $4\ ;\ 2{,}5\ ;\ 3{,}33\ ;\ 2{,}75\ ;\ 3{,}2\ ;\ \dots$ Les termes passent tantôt au-dessus, tantôt au-dessous de 3, mais s'en rapprochent : la suite converge vers 3.

### Définition de la limite d'une suite

Une suite converge vers un réel $L$ si ses termes se rapprochent de plus en plus de $L$. À partir d’un certain rang, ils restent aussi proches de $L$ qu’on le souhaite.

Le réel $L$ s'appelle la **limite** de la suite. Lorsqu'elle existe, cette limite est unique.

En pratique : choisir un intervalle aussi petit que l'on veut autour de $L$. À partir d'un certain rang, tous les termes y restent.

**Exemple :** $u_n = \dfrac{1}{n+1}$ et $L = 0$. Prendre l'intervalle $]-0{,}01\ ;\ 0{,}01[$.

Un terme est dans cet intervalle lorsque $\dfrac{1}{n+1} < 0{,}01$, c'est-à-dire lorsque $n + 1 > 100$, soit $n \geq 100$. À partir du rang 100, tous les termes sont dans l'intervalle. Et cela marche aussi avec un intervalle encore plus petit : il faut seulement aller plus loin dans la suite.

### Notation $u_n \to L$

Pour dire que la suite $(u_n)$ converge vers $L$, écrire :

$$u_n \to L \quad \text{ou} \quad \lim_{n \to +\infty} u_n = L$$

Se lit : « $u_n$ tend vers $L$ quand $n$ tend vers l'infini ».

**Exemple :** $\displaystyle \lim_{n \to +\infty} \frac{1}{n+1} = 0$.

### Interprétation graphique

Représenter la suite par les points $(n\,;\,u_n)$. Dire que $u_n \to L$ signifie que ces points se rapprochent de la droite horizontale d'équation $y = L$.

Pour une bande aussi fine que l'on veut autour de cette droite, tous les points sont dans la bande à partir d'un certain rang. Seuls les premiers points peuvent en sortir.

- Pour $u_n = \dfrac{1}{n+1}$ : les points descendent et s'écrasent contre la droite $y = 0$.
- Pour $u_n = 3 + \dfrac{(-1)^n}{n+1}$ : les points sautent de part et d'autre de la droite $y = 3$, en s'en approchant à chaque saut.

### Différence entre convergence et divergence

Une suite est **convergente** si elle a une limite finie $L$. Dans tous les autres cas, elle est **divergente**.

Une suite divergente peut se comporter de deux façons :

- **Ses termes deviennent de plus en plus grands** (ou de plus en plus petits) et dépassent n'importe quel nombre : on dit qu'elle tend vers $+\infty$ (ou $-\infty$). Exemple : $u_n = n$ donne $0\ ;\ 1\ ;\ 2\ ;\ 3\ ;\ \dots$
- **Ses termes ne se stabilisent pas** : ils ne se rapprochent d'aucun nombre. Exemple : $u_n = (-1)^n$ alterne sans cesse entre $1$ et $-1$.

---

## 2. Convergence dans la monotonie et bornes

### Théorèmes de convergence associés

Dans la fiche précédente, on a vu qu'une suite croissante et majorée ne peut pas « partir vers l'infini ». Voici l'énoncé précis.

**Théorème 1.** Toute suite **croissante et majorée** est convergente.

**Théorème 2.** Toute suite **décroissante et minorée** est convergente.

Ces théorèmes garantissent que la limite **existe**. Ils ne donnent **pas sa valeur**.

Pour les utiliser, vérifier les deux conditions : la suite est monotone dans le bon sens **et** elle est bornée du bon côté (majorée si elle est croissante, minorée si elle est décroissante).

**Exemple :** $u_0 = 0$ et $u_{n+1} = \dfrac{u_n + 3}{2}$.

- Elle est majorée par 3
- Elle est croissante : $u_{n+1} - u_n = \dfrac{u_n + 3}{2} - u_n = \dfrac{3 - u_n}{2}$, et comme $u_n \leq 3$, cette différence est positive.

La suite est croissante et majorée : d'après le théorème 1, elle converge.

---

## 3. Erreurs fréquentes

### Confondre suite bornée et suite convergente

Toute suite convergente est bornée : à partir d'un certain rang, ses termes restent près de la limite. Mais la réciproque est fausse.

La suite $u_n = (-1)^n$ est bornée (entre $-1$ et $1$), mais elle ne converge pas.

### Confondre convergence et monotonie

La monotonie décrit le **sens** dans lequel va la suite. La convergence décrit ce qu'il se passe **à l'infini**. Ce sont deux notions différentes.

- $u_n = n$ est croissante, mais elle diverge.
- $u_n = \dfrac{1}{n+1}$ est décroissante, et elle converge.

### Croire qu'une suite qui n'est pas monotone ne peut pas converger

Une suite peut changer de sens sans arrêt et converger quand même.

La suite $u_n = 3 + \dfrac{(-1)^n}{n+1}$ n'est pas monotone, mais elle converge vers 3.

### Utiliser un théorème sans vérifier ses conditions

Avant d'appliquer un théorème, vérifier **toutes** ses conditions, dans le bon sens.

- $u_n = (-1)^n$ est majorée, mais elle n'est pas croissante : le théorème 1 ne s'applique pas.
- $u_n = -n$ est décroissante, mais elle n'est pas minorée : le théorème 2 ne s'applique pas. Et en effet, elle diverge. Attention : elle est bien majorée (par $u_0 = 0$), mais pour une suite décroissante, c'est la minoration qu'il faut.

### Confondre la limite avec un terme $u_n$

La limite $L$ est un nombre fixe, vers lequel les termes se rapprochent. Ce n'est pas un terme de la suite, et la suite ne l'atteint pas forcément.

La suite $u_n = \dfrac{1}{n+1}$ converge vers 0, mais aucun de ses termes ne vaut 0. Et le terme $u_{100} = \dfrac{1}{101}$ n'est pas la limite : il en est seulement proche.
