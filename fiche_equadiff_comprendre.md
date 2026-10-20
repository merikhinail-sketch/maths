# Comprendre ce qu'est une équation différentielle

Cette fiche explique ce qu'est une équation différentielle, ce que signifie « en être solution », et comment la relier à une situation concrète.

---

## 1. Définition

### Équation dont l'inconnue est une fonction

Dans une équation ordinaire, comme $2x + 1 = 5$, l'inconnue est un **nombre** : on cherche la valeur de $x$.

Dans une **équation différentielle**, l'inconnue est une **fonction**, notée en général $y$. L'équation relie cette fonction à sa dérivée $y'$.

**Exemple :**

$$y' = 2y$$

Résoudre cette équation, c'est trouver **toutes les fonctions $y$** dont la dérivée est égale au double de la fonction elle-même.

### Rôle de la fonction et de sa dérivée

Dans l'équation $y' = 2y$ :

- $y$ est la fonction inconnue : elle donne une valeur en chaque point $x$ ;
- $y'$ est sa dérivée : elle donne la vitesse à laquelle $y$ varie, c'est-à-dire la pente de la courbe en chaque point.

L'équation impose donc un lien entre la valeur de la fonction et sa vitesse de variation autrement dit entre la fonction et sa dérivée, **en chaque point $x$**. Pour $y' = 2y$ : en chaque point, la pente de la courbe vaut le double de la valeur de la fonction.

### Reconnaître une équation différentielle

Une équation différentielle est une égalité qui lie une fonction $y$ et sa dérivée $y'$. 

- $y' = 3y - 1$ : équation différentielle (elle contient $y$ et $y'$) ;
- $y' = -0{,}5\,y$ : équation différentielle ;
- $2x + 1 = 5$ : ce n'est pas une équation différentielle, l'inconnue est un nombre ;
- $y^2 = 4$ : ce n'est pas une équation différentielle, car $y$ n'est pas lié à sa dérivée $y'$.


## 2. Notion de solution et vérification

### Définition d'une solution

Une fonction $f$ dérivable est **solution** d'une équation différentielle lorsque, en remplaçant $y$ par $f$ et $y'$ par $f'$, l'égalité est vraie **pour tout $x$**.

### Vérifier qu'une fonction est solution

Procéder en trois temps :

1. **Calculer la dérivée** $f'$ de la fonction proposée.
2. **Calculer l'autre côté de l'équation** en remplaçant $y$ par $f$.
3. **Comparer** : les deux résultats doivent être égaux pour tout $x$.

**Exemple :** la fonction $f(x) = e^{2x}$ est-elle solution de $y' = 2y$ ?

On remplace $y$ par $f(x)$ et $y'$ par $f'(x)$:

- Dérivée : $f'(x) = 2e^{2x}$.
- Autre côté : $2f(x) = 2e^{2x}$.
- Comparaison : $f'(x) = 2f(x)$ pour tout $x$. La fonction $f$ est solution.

**Contre-exemple :** $g(x) = x^2$ est-elle solution de $y' = 2y$ ?

- Dérivée : $g'(x) = 2x$.
- Autre côté : $2g(x) = 2x^2$.

Or  $\forall x \in \mathbb{R}$, $2x \neq 2x^2$, la fonction $g$ n'est donc pas solution.

### Comprendre qu'il peut exister plusieurs solutions

Une équation différentielle n'a pas une seule solution, mais **plusieurs**. Pour $y' = 2y$ :

- $f(x) = e^{2x}$ est solution (vu plus haut) ;
- $f(x) = 3e^{2x}$ est aussi solution : $f'(x) = 6e^{2x} = 2 \times 3e^{2x} = 2f(x)$ ;
- $f(x) = -e^{2x}$ aussi ;
- la fonction nulle $f(x) = 0$ aussi : $0 = 2 \times 0$.

### Distinguer solution particulière et famille de solutions

- Une **solution particulière** est **une fonction** solution de l'équation. Exemple : $e^{2x}$.
- Une **famille de solutions** est un ensemble de fonctions décrit par une seule expression, avec une constante $C$ qui peut prendre toutes les valeurs. Exemple : $y(x) = Ce^{2x}$, avec $C$ réel.

Chaque valeur de $C$ donne une solution particulière : $C = 1$ donne $e^{2x}$, $C = 3$ donne $3e^{2x}$, et ainsi de suite.

---

## 3. Interprétation dans un problème

### Ce que représente la fonction

Dans un problème, la fonction $y$ représente souvent une **quantité qui évolue au cours du temps** : le nombre de bactéries, la température d'un objet, la quantité de médicament dans le sang, un capital placé.

On la note alors $y(t)$, où $t$ est le temps.

### Ce que représente sa dérivée

La dérivée $y'(t)$ représente la **vitesse de variation** de la quantité à l'instant $t$ :

- $y'(t) > 0$ : la quantité **augmente** ;
- $y'(t) < 0$ : la quantité **diminue** ;
- plus la valeur absolue $y'(t)$ est grand, plus la quantité varie **vite**.

### Relier l'équation différentielle à l'évolution d'une quantité

L'équation différentielle traduit une règle : **comment la vitesse de variation dépend de la quantité elle-même**.

**Exemple :** le nombre de bactéries $y(t)$, en milliers, au bout de $t$ heures vérifie :

$$y'(t) = 0{,}5\,y(t)$$

Lecture : la vitesse est proportionnelle au nombre de bactéries. Plus il y a de bactéries, plus la population augmente vite.

**Autre exemple :** la quantité $y(t)$ d'un médicament dans le sang vérifie :

$$y'(t) = -0{,}2\,y(t)$$
Comme $y(t) > 0$, on a $y'(t) < 0$ : la quantité diminue. Plus la quantité de médicament présente dans le sang est importante, plus le médicament est éliminé rapidement.


---

## 4. Erreurs fréquentes

### Confondre la fonction et sa dérivée dans l'équation différentielle

$y$ et $y'$ ne jouent pas le même rôle : l'équation $y' = 2y$ **ne signifie pas** $y = 2y$

Lors d'une vérification, on remplace $y'$ par la **dérivée** $f'$ et $y$ par la **fonction** $f$.

### Ne pas vérifier correctement qu'une fonction est solution

Ne pas oublier de **calculer la dérivée**. Comparer $f(x)$ et $2f(x)$ dans notre exemple ne vérifie rien : il faut comparer $f'(x)$ et $2f(x)$.

Pour $f(x) = e^{2x}$ : calculer $f'(x) = 2e^{2x}$, puis le comparer à $2f(x) = 2e^{2x}$.


### Confondre une solution particulière avec l'ensemble des solutions

Trouver une fonction qui marche ne veut pas dire avoir tout résolu.

Avoir vérifié que $e^{2x}$ est solution de $y' = 2y$ ne donne **qu'une** solution : l'ensemble des solutions est la famille $Ce^{2x}$, avec $C$ réel.

### Mal interpréter ce que représentent la fonction et sa dérivée dans un problème

Ne pas confondre la **quantité** $y(t)$ avec sa **vitesse de variation** $y'(t)$.

Dire « $y'(2) = 3$ » signifie qu'à l'instant $t = 2$, la quantité **augmente de 3 unités par unité de temps**. Cela ne veut pas dire que la quantité vaut 3.
