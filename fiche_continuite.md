# La continuité

Une fonction continue est une fonction dont la courbe se trace « d'un seul trait ». Cette fiche donne la définition précise, puis les réflexes pour justifier rapidement qu'une fonction est continue.

---

## 1. Continuité

### Définition de la continuité

Soit $f$ une fonction définie en un réel $a$ et autour de $a$. On dit que $f$ est **continue en $a$** si :

$$\lim_{x \to a} f(x) = f(a)$$

Autrement dit : quand $x$ se rapproche de $a$, la valeur $f(x)$ se rapproche de $f(a)$. Il n'y a pas de « saut » en $a$.

**Exemple :** $f(x) = x^2$ en $a = 2$. Quand $x$ se rapproche de 2, $x^2$ se rapproche de 4, et $f(2) = 4$. La fonction est continue en 2.

### Interprétation graphique

Graphiquement, $f$ est continue en $a$ si la courbe peut se tracer **sans lever le crayon** autour de l'abscisse $a$.

La courbe n'est pas continue en $a$ lorsqu'elle présente :

- **un saut** : la courbe s'arrête à une ordonnée et reprend à une autre ordonnée  ;
- **un point détaché** : le point d'abscisse $a$ ne se trouve pas dans le prolongement du reste de la courbe.

**Exemple :** la fonction $g$ définie par $g(x) = x$ si $x < 1$ et $g(x) = x + 2$ si $x \geq 1$. Pour $x$ strictement inférieur à 1, la courbe est proche de l'ordonnée 1, mais en $x = 1$ elle est à l'ordonnée 3. Il faut lever le crayon : $g$ n'est pas continue en 1.

---

## 2. Continuité sur un intervalle

### Définition d'une fonction continue sur un intervalle

Une fonction $f$ est **continue sur un intervalle $I$** si elle est continue en tout point de $I$.

### Continuité en tout point de l'intervalle

Pour que $f$ soit continue sur $I$, la condition doit être vraie **pour chaque réel $a$ de $I$**, et pas seulement en quelques points.

Graphiquement, cela veut dire que la courbe de $f$ se trace sans lever le crayon **sur toute la partie de $I$**.

### Identifier graphiquement ou à partir d'une expression si une fonction est continue sur un intervalle

**Graphiquement :** parcourir la courbe de gauche à droite sur l'intervalle et repérer les sauts ou les points détachés. S'il y en a un, la fonction n'est pas continue sur l'intervalle.

**À partir d'une expression :**

- si la fonction est construite avec des fonctions usuelles (parties 3 et 4), on conclut avec les résultats du cours ;
- si la fonction est **définie par morceaux**, la continuité est à vérifier au point de raccord. Comparer trois nombres : la limite quand $x$ s'approche de $a$ **par la gauche** (notée $\lim\limits_{x \to a^-}$), la limite **par la droite** (notée $\lim\limits_{x \to a^+}$), et $f(a)$. La fonction est continue en $a$ si ces trois nombres sont égaux.

**Exemple (fonction continue) :** $f(x) = x^2 + 1$ si $x < 2$ et $f(x) = 3x - 1$ si $x \geq 2$.

- Par la gauche : $\lim\limits_{x \to 2^-} f(x) = 2^2 + 1 = 5$.
- Par la droite : $\lim\limits_{x \to 2^+} f(x) = 3 \times 2 - 1 = 5$.
- Valeur : $f(2) = 5$.

Les trois nombres sont égaux : $f$ est continue en 2.

**Exemple (fonction non continue) :** la fonction $g$ de la partie 1.

- Par la gauche : $\lim\limits_{x \to 1^-} g(x) = 1$.
- Par la droite : $\lim\limits_{x \to 1^+} g(x) = 3$.

Les limites sont différentes : $g$ n'est pas continue en 1.

---

## 3. Fonctions usuelles continues

### Fonctions polynômes

Toute fonction polynôme est continue sur $\mathbb{R}$.

**Exemple :** $f(x) = 3x^2 - 5x + 1$ est continue sur $\mathbb{R}$.

### Fonctions rationnelles sur leur domaine de définition

Une fonction rationnelle est un quotient de deux polynômes. Elle est continue sur **chaque intervalle de son domaine de définition**, c'est-à-dire partout où le dénominateur ne s'annule pas.

**Exemple :** $f(x) = \dfrac{1}{x}$ est continue sur $]-\infty\ ;\ 0[$ et sur $]0\ ;\ +\infty[$. Elle n'est pas définie en 0, donc on ne peut pas parler de continuité sur un intervalle qui contient 0.

### Fonctions usuelles 

| Fonction | Continue sur |
|---|---|
| racine carrée $\sqrt{x}$ | $[0\ ;\ +\infty[$ |
| exponentielle $e^x$ | $\mathbb{R}$ |
| logarithme népérien $\ln(x)$ | $]0\ ;\ +\infty[$ |
| sinus $\sin(x)$ et cosinus $\cos(x)$ | $\mathbb{R}$ |
| valeur absolue $\lvert x \rvert$ | $\mathbb{R}$ |

### Utiliser ces résultats pour justifier rapidement la continuité d'une fonction

Pour justifier qu'une fonction est continue, citer la famille à laquelle elle appartient.

> « La fonction $f$ est une fonction polynôme, donc elle est continue sur $\mathbb{R}$. »

> « La fonction $\exp$ est continue sur $\mathbb{R}$. »

Autre raccourci utile : toute fonction **dérivable** sur un intervalle est continue sur cet intervalle. La réciproque est fausse : la valeur absolue est continue en 0 mais n'y est pas dérivable.

---

## 4. Opérations sur la fonction continue

### Somme, différence et produit

Si $f$ et $g$ sont continues sur un intervalle $I$, alors $f + g$, $f - g$ et $f \times g$ sont continues sur $I$.

**Exemple :** $h(x) = e^x + 3x^2$ est la somme de $e^x$ (continue sur $\mathbb{R}$) et d'un polynôme (continu sur $\mathbb{R}$). Donc $h$ est continue sur $\mathbb{R}$.

### Quotient lorsque le dénominateur ne s'annule pas

Si $f$ et $g$ sont continues sur $I$ et si $g$ **ne s'annule pas** sur $I$, alors $\dfrac{f}{g}$ est continue sur $I$.

**Exemple :** $h(x) = \dfrac{x^2 + 1}{x - 2}$. Le numérateur et le dénominateur sont des polynômes, donc continus. Le dénominateur s'annule en 2. Donc $h$ est continue sur $]-\infty\ ;\ 2[$ et sur $]2\ ;\ +\infty[$.


### Déduire la continuité d'une fonction à partir de fonctions déjà connues comme continues

Procéder en quatre temps :

1. **Décomposer** la fonction en fonctions usuelles reliées par des opérations.
2. **Citer** la continuité de chaque brique.
3. **Vérifier** les conditions éventuelles (dénominateur non nul, valeurs de la fonction intérieure dans le domaine de la fonction extérieure).
4. **Conclure** sur l'intervalle voulu.

**Exemple :** montrer que $f(x) = \dfrac{e^x}{x^2 + 1}$ est continue sur $\mathbb{R}$.

- Le numérateur $e^x$ est continu sur $\mathbb{R}$.
- Le dénominateur $x^2 + 1$ est un polynôme, donc continu sur $\mathbb{R}$.
- Pour tout réel $x$, $x^2 + 1 > 0$, donc le dénominateur ne s'annule jamais.

Le quotient est continu sur $\mathbb{R}$.
