# Rappels de Première : les suites

Cette fiche reprend l'essentiel sur les suites arithmétiques et géométriques. Prendre le temps de lire chaque exemple : ils servent à retrouver les réflexes avant d'attaquer le chapitre.

---

## 1. Suites arithmétiques

### Définition

Une suite arithmétique est une suite où, pour passer d'un terme au suivant, il faut toujours additionner le même nombre. Ce nombre s'appelle la **raison**, notée $r$.

**Exemple :** $2\ ;\ 4\ ;\ 6\ ;\ 8\ ;\ 10$

Ici, pour passer d'un terme au suivant, on additionne 2. La raison de cette suite est donc $r = 2$.

### Relation entre deux termes consécutifs

Pour tout entier naturel $n$, passer d'un terme au suivant revient à ajouter la raison :

$$u_{n+1} = u_n + r$$

**Exemple :** si $u_n$ a pour raison $r = 3$ et $u_4 = 10$, alors $u_5 = 10 + 3 = 13$.

### Méthode pour déterminer la raison

Calculer la différence entre un terme et le précédent :

$$r = u_{n+1} - u_n$$

Remarque : Pour vérifier qu'une suite est bien arithmétique, vérifier qu'on additionne bien toujours par le même nombre.

**Exemple :** $5\ ;\ 2\ ;\ -1\ ;\ -4$

- $2 - 5 = -3$
- $-1 - 2 = -3$
- $-4 - (-1) = -3$

La différence est toujours la même : la suite est arithmétique de raison $r = -3$.

### Sens de variation

Comme $u_{n+1} - u_n = r$, le signe de la raison donne directement le sens de variation :

- si $r > 0$, la suite est **croissante** ;
- si $r < 0$, la suite est **décroissante** ;
- si $r = 0$, la suite est **constante**.

**Exemple :** $12\ ;\ 9\ ;\ 6\ ;\ 3$ a pour raison $-3$. Comme $-3 < 0$, la suite est décroissante.

En effet cela paraît assez logique : si on ajoute toujours **un nombre négatif** alors cela revient à toujours soutraire donc la suite est décroissante. À l'inverse, si on additionne toujours **un nombre positif** alors la suite est croissante.
### Somme des termes d'une suite arithmétique


Comment calculer $1 + 2 + 3 + 4$ sans tout additionner dans l'ordre ? Une astuce : associer le premier terme avec le dernier, puis le deuxième avec l'avant-dernier.

- $1 + 4 = 5$
- $2 + 3 = 5$

On obtient 2 paires qui valent chacune 5. La somme vaut donc $2 \times 5 = 10$.

Cela fonctionne pour toute suite arithmétique : comme on ajoute toujours le même nombre, chaque paire donne la même somme. Il suffit alors de compter les paires, soit la moitié du nombre de termes :

$$S = \frac{\text{nombre de termes}}{2} \times (\text{premier terme} + \text{dernier terme})$$

Pour compter les termes de $u_p$ à $u_n$ :

$$\text{nombre de termes} = n - p + 1$$

**Exemple :** calculer $2 + 4 + 6 + 8 + 10$.

Il y a 5 termes, le premier vaut 2 et le dernier vaut 10 :

$$S = \frac{5}{2} \times (2 + 10) = \frac{5}{2} \times 12 = 30$$

**Remarque :** il existe une autre technique pour additionner des entiers consécutifs. Pour une somme qui commence à 1 et avance de 1 en 1, $1 + 2 + 3 + \dots + n$, calculer le nombre de termes fois le nombre qui suit le dernier terme, le tout divisé par 2 :

$$1 + 2 + 3 + \dots + n = \frac{n \times (n + 1)}{2}$$

Pour $1 + 2 + 3 + 4$ : $\frac{4 \times 5}{2} = 10$. On retrouve bien le même résultat.

**Attention** : Cette technique ne marche que pour les sommes de termes consécutifs.



## 2. Suites géométriques

### Définition

Une suite géométrique est une suite où, pour passer d'un terme au suivant, il faut toujours multiplier par le même nombre. Ce nombre s'appelle la **raison**, notée $q$.

**Exemple :** $3\ ;\ 6\ ;\ 12\ ;\ 24\ ;\ 48$

Ici, on multiplie par 2 à chaque étape. La raison est $q = 2$.

### Relation entre un terme et le suivant

Pour tout entier naturel $n$ :

$$u_{n+1} = q \times u_n$$

**Exemple :** si $q = 3$ et $u_2 = 4$, alors $u_3 = 3 \times 4 = 12$.

### Déterminer la raison

Calculer le quotient d'un terme par le précédent (les termes doivent être non nuls) :

$$q = \frac{u_{n+1}}{u_n}$$

**Exemple :** $80\ ;\ 40\ ;\ 20\ ;\ 10$

- $\frac{40}{80} = \frac{1}{2}$
- $\frac{20}{40} = \frac{1}{2}$
- $\frac{10}{20} = \frac{1}{2}$

Le quotient est toujours le même : la suite est géométrique de raison $q = \frac{1}{2}$.

### Sens de variation

Le sens de variation dépend de la raison $q$ **et** du signe du premier terme. Commencer par le cas où le premier terme est **positif** :

- si $q > 1$, la suite est **croissante** (chaque terme est agrandi) ;
- si $0 < q < 1$, la suite est **décroissante** (chaque terme est rétréci) ;
- si $q = 1$, la suite est **constante**.

Remarque : il n'est pas intuitif de se dire que la suite géométrique est décroissante quand la raison est entre 0 et 1 alors que c'est positif. Pour rappel, multiplier par un nombre strictement positif et strictement inférieur à 1 revient à diviser.

*Exemple* : 0.5 x 4 = 2

Donc lorsque sa raison est strictement entre 0 et 1, la suite géométrique est décroissante.



Si le premier terme est **négatif**, les variations s'inversent : avec $q > 1$, la suite est décroissante ; avec $0 < q < 1$, elle est croissante.

Si $q < 0$, les termes changent de signe à chaque étape : la suite n'est ni croissante ni décroissante.

**Exemple :** $1\ ;\ -2\ ;\ 4\ ;\ -8$ a pour raison $q = -2$. Les signes alternent : la suite n'est pas monotone.

### Somme des termes

Pour additionner des termes consécutifs d'une suite géométrique de raison $q \neq 1$ :

$$S = \text{premier terme} \times \frac{1 - q^{\,\text{nombre de termes}}}{1 - q}$$

**Exemple :** calculer $3 + 6 + 12 + 24 + 48$.

Il y a 5 termes, le premier vaut 3 et la raison vaut 2 :

$$S = 3 \times \frac{1 - 2^5}{1 - 2} = 3 \times \frac{-31}{-1} = 3 \times 31 = 93$$

Si $q = 1$, tous les termes sont égaux : la somme vaut simplement $\text{nombre de termes} \times \text{premier terme}$.

---

## 3. Erreurs fréquentes

### Confondre raison et premier terme

La raison est le nombre qui permet de passer d'un terme au suivant, pas le point de départ.

Dans $5\ ;\ 8\ ;\ 11\ ;\ 14$, le premier terme est 5, mais la raison est $8 - 5 = 3$.

### Mélanger addition et multiplication

Ne pas appliquer la méthode de l'un des deux types à l'autre. Avant de conclure, tester la différence **et** le quotient.

Dans $3\ ;\ 6\ ;\ 12$, les différences sont $3$ puis $6$ : la suite n'est pas arithmétique. Les quotients valent $2$ et $2$ : elle est géométrique.

### Utilisation de la mauvaise formule

Identifier le type de suite **avant** de choisir la formule.

- suite arithmétique : $S = \text{nombre de termes} \times \frac{\text{premier} + \text{dernier}}{2}$
- suite géométrique : $S = \text{premier terme} \times \frac{1 - q^{\,\text{nombre de termes}}}{1 - q}$

### Erreurs dans le nombre de termes

Quand la suite commence à $u_0$, il y a un terme de plus que l'indice du dernier.

De $u_0$ à $u_{10}$, il y a $10 - 0 + 1 = 11$ termes, et non 10. De $u_3$ à $u_8$, il y a $8 - 3 + 1 = 6$ termes.

### Erreurs de signes

Soigner l'ordre de la soustraction : la raison est $u_{n+1} - u_n$, et non l'inverse.

Dans $10\ ;\ 7\ ;\ 4$, la raison est $7 - 10 = -3$, pas $3$.

Pour une raison négative, penser aux parenthèses : $(-2)^2 = 4$, alors que $-2^2 = -4$.
