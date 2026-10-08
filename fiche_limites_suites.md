# Limites de suites

Cette fiche permet de déterminer la limite d'une suite : savoir ce qu'il se passe quand $n$ devient très grand, et le calculer sans deviner.

---

## 1. Définition

### Notion de limite d'une suite

Chercher la limite d'une suite $(u_n)$, c'est se demander ce que deviennent ses termes lorsque $n$ devient de plus en plus grand : ils peuvent se rapprocher d'un nombre, devenir immenses, ou ne pas se stabiliser.

Cette limite, lorsqu'elle existe, se note :

$$\lim_{n \to +\infty} u_n$$

### Limite finie et infinie

**Limite finie.** La suite $(u_n)$ a pour limite le réel $L$ si quand n augmente $(u_n)$ se rapproche de plus en plus de $L$. On écrit $u_n \to L$ : la suite **converge**.

**Limite $+\infty$.** La suite $(u_n)$ **tend vers $+\infty$** si tout intervalle de la forme $]A\ ;\ +\infty[$ contient tous les termes à partir d'un certain rang. Autrement dit, quel que soit le nombre $A$ choisi, aussi grand soit-il, les termes finissent tous par le dépasser.

**Exemple :** $u_n = n^2$ et $A = 10\,000$. On a $n^2 > 10\,000$ dès que $n \geq 101$. À partir du rang 101, tous les termes dépassent 10 000. Et cela marche pour n'importe quel $A$ : il faut seulement aller plus loin dans la suite.

**Limite $-\infty$.** La suite $(u_n)$ **tend vers $-\infty$** si tout intervalle de la forme $]-\infty\ ;\ A[$ contient tous les termes à partir d'un certain rang : les termes finissent tous sous n'importe quel nombre.

**Exemple :** $u_n = -n$ tend vers $-\infty$.

**À retenir :**

- limite finie : la suite converge ;
- limite infinie, ou pas de limite du tout (comme $(-1)^n$) : la suite diverge.

---

## 2. Limites usuelles

### Suites de référence à connaître

Ces limites servent de base à tous les calculs suivants. Il faut les connaître sans hésiter.

| Suite | Limite |
|---|---|
| $n$ | $+\infty$ |
| $n^2$ | $+\infty$ |
| $n^k$ (avec $k$ entier, $k \geq 1$) | $+\infty$ |
| $\sqrt{n}$ | $+\infty$ |
| $\dfrac{1}{n}$ | $0$ |
| $\dfrac{1}{n^2}$ | $0$ |
| $\dfrac{1}{n^k}$ (avec $k$ entier, $k \geq 1$) | $0$ |
| $\dfrac{1}{\sqrt{n}}$ | $0$ |

L'idée à garder en tête : une puissance de $n$ devient immense, et son inverse devient minuscule.

### Puissances et expressions classiques

Pour la suite géométrique $q^n$, la limite dépend de la valeur de $q$ :

| Valeur de $q$ | Limite de $q^n$ | Exemple |
|---|---|---|
| $q > 1$ | $+\infty$ | $2^n$ |
| $q = 1$ | $1$ | $1^n = 1$ |
| $-1 < q < 1$ | $0$ | $\left(\dfrac{1}{2}\right)^n$, $(-0{,}5)^n$ |
| $q \leq -1$ | pas de limite | $(-1)^n$, $(-2)^n$ |

Pour $q \leq -1$, la suite alterne entre des valeurs positives et négatives sans jamais se stabiliser : elle n'a pas de limite.

---

## 3. Formes indéterminées

Pour calculer une limite, on utilise d'abord les règles de calcul sur les limites. Elles sont assez naturelles :

- si $u_n \to L$ et $v_n \to L'$, alors $u_n + v_n \to L + L'$, $u_n \times v_n \to L \times L'$ et, si $L' \neq 0$, $\dfrac{u_n}{v_n} \to \dfrac{L}{L'}$ ;
- $+\infty + (+\infty) = +\infty$ et $+\infty \times (+\infty) = +\infty$ ;
- un nombre divisé par une quantité qui tend vers $\pm\infty$ donne $0$.

Dans certains cas, ces règles ne permettent pas de conclure : on parle de **forme indéterminée**.

### 0/0 ; +∞/+∞ ; 0 × +∞ ; +∞ − ∞

Ces quatre formes sont indéterminées :

$$\frac{0}{0} \qquad \frac{+\infty}{+\infty} \qquad 0 \times (+\infty) \qquad +\infty - \infty$$

« Indéterminée » ne veut pas dire « pas de limite ». Cela veut dire que le résultat dépend des suites en jeu, et qu'il faut transformer l'expression pour conclure.

**Exemple avec $+\infty - \infty$ :** trois suites de ce type, trois résultats différents.

- $n - n = 0$, qui tend vers $0$ ;
- $n^2 - n$, qui tend vers $+\infty$ ;
- $n - n^2$, qui tend vers $-\infty$.

### Méthodes pour les traiter

**Méthode 1 : factoriser par le terme dominant.**

Le terme dominant est celui qui « pèse le plus » quand $n$ est grand (la plus grande puissance de $n$). Le factoriser fait apparaître des termes dont la limite est connue. Cette méthode règle $+\infty - \infty$ et $\dfrac{+\infty}{+\infty}$.

*Exemple ($+\infty - \infty$) :* $u_n = n^2 - n$.

$$u_n = n^2\left(1 - \frac{1}{n}\right)$$

Or $n^2 \to +\infty$ et $1 - \dfrac{1}{n} \to 1$. Par produit, $u_n \to +\infty$.

*Exemple ($\dfrac{+\infty}{+\infty}$) :* $u_n = \dfrac{2n + 1}{n + 3}$.

Factoriser le numérateur et le dénominateur par $n$, puis simplifier :

$$u_n = \frac{n\left(2 + \dfrac{1}{n}\right)}{n\left(1 + \dfrac{3}{n}\right)} = \frac{2 + \dfrac{1}{n}}{1 + \dfrac{3}{n}}$$

Le numérateur tend vers $2$, le dénominateur vers $1$. Par quotient, $u_n \to 2$.

**Méthode 2 : simplifier ou se ramener à un seul quotient.**

Cette méthode règle $0 \times (+\infty)$ et $\dfrac{0}{0}$.

*Exemple ($0 \times (+\infty)$) :* $u_n = n \times \dfrac{1}{n^2}$.

$$u_n = \frac{n}{n^2} = \frac{1}{n} \to 0$$

*Exemple ($\dfrac{0}{0}$) :* $u_n = \dfrac{\dfrac{1}{n}}{\dfrac{1}{n^2}}$.

$$u_n = \frac{1}{n} \times n^2 = n \to +\infty$$

**Méthode 3 : multiplier par la quantité conjuguée.**

Quand l'expression contient une différence de racines carrées ($+\infty - \infty$), multiplier et diviser par la somme des deux racines. L'identité $(a - b)(a + b) = a^2 - b^2$ fait disparaître les racines.

*Exemple :* $u_n = \sqrt{n + 1} - \sqrt{n}$.

$$u_n = \frac{\left(\sqrt{n+1} - \sqrt{n}\right)\left(\sqrt{n+1} + \sqrt{n}\right)}{\sqrt{n+1} + \sqrt{n}} = \frac{(n+1) - n}{\sqrt{n+1} + \sqrt{n}} = \frac{1}{\sqrt{n+1} + \sqrt{n}}$$

Le dénominateur tend vers $+\infty$. Donc $u_n \to 0$.

---

## 4. Comparaison

### Théorème des gendarmes

Soient $(u_n)$, $(v_n)$ et $(w_n)$ trois suites telles que, à partir d'un certain rang :

$$u_n \leq v_n \leq w_n$$

Si $(u_n)$ et $(w_n)$ convergent **vers la même limite $L$**, alors $(v_n)$ converge aussi vers $L$.

L'idée : la suite $(v_n)$ est coincée entre deux suites qui se rejoignent en $L$. Elle n'a pas d'autre choix que d'aller en $L$ elle aussi.

### Comparaison de suites

Soient $(u_n)$ et $(v_n)$ deux suites telles que, à partir d'un certain rang :

- si $u_n \geq v_n$ et $v_n \to +\infty$, alors $u_n \to +\infty$ ;
- si $u_n \leq v_n$ et $v_n \to -\infty$, alors $u_n \to -\infty$.

L'idée : une suite qui reste au-dessus d'une suite qui part vers $+\infty$ part elle aussi vers $+\infty$. Ce théorème ne sert que pour les limites **infinies**.

### Utilisation pour déterminer une limite

Quand le calcul direct est impossible (par exemple à cause d'un $(-1)^n$ ou d'un cosinus), procéder en trois temps :

1. **Choisir le théorème** : gendarmes pour une limite finie attendue, comparaison pour une limite infinie.
2. **Encadrer ou minorer** la suite à l'aide d'une inégalité connue, comme $-1 \leq (-1)^n \leq 1$.
3. **Conclure** en citant le théorème et les limites des suites de comparaison.

**Exemple (gendarmes) :** déterminer la limite de $v_n = \dfrac{(-1)^n}{n}$ pour $n \geq 1$.

Pour tout entier $n \geq 1$, on a $-1 \leq (-1)^n \leq 1$. En divisant par $n$ qui est positif :

$$-\frac{1}{n} \leq \frac{(-1)^n}{n} \leq \frac{1}{n}$$

Or $-\dfrac{1}{n} \to 0$ et $\dfrac{1}{n} \to 0$. D'après le théorème des gendarmes, $v_n \to 0$.

**Exemple (comparaison) :** déterminer la limite de $u_n = n + (-1)^n$.

Pour tout $n$, on a $(-1)^n \geq -1$, donc :

$$u_n \geq n - 1$$

Or $n - 1 \to +\infty$. D'après le théorème de comparaison, $u_n \to +\infty$.
