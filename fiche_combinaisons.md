# Les combinaisons

Cette fiche apprend à compter les groupes : des situations où l'on choisit des éléments **sans se soucier de l'ordre**. Tout repose sur une idée simple, détaillée dans la partie 1.

---

## 1. Reconnaître une combinaison

### Identifier une situation où l'on choisit $k$ éléments parmi $n$

Une **combinaison** de $k$ éléments parmi $n$ est un **groupe** de $k$ éléments choisis dans un ensemble de $n$ éléments, sans ordre et sans répétition.

Repérer les situations typiques : former un comité, choisir une équipe, tirer plusieurs boules **en même temps**, recevoir une main de cartes.

**Exemple :** choisir 3 élèves parmi 10 pour former un comité.

Test à faire à chaque fois : échanger deux éléments change-t-il le résultat ? Pour un comité, choisir Alice puis Bob ou Bob puis Alice donne le même comité : l'ordre ne compte pas. C'est donc une combinaison.

### Comprendre pourquoi l'ordre ne crée pas de nouveau choix

On prend 4 élèves, $A$, $B$, $C$ et $D$, et forme des groupes de 3.

Si l'ordre comptait, on aurait des listes ordonnées. Compter ces listes, comme dans la fiche sur les $k$-uplets :

$$4 \times 3 \times 2 = 24 \text{ listes}$$

Mais regardons le groupe $\{A,\ B,\ C\}$. Il donne $3! = 6$ listes différentes :

$$ABC,\ ACB,\ BAC,\ BCA,\ CAB,\ CBA$$

Ces 6 listes représentent **un seul et même groupe**. Il en va de même pour chaque groupe : chaque groupe est compté $3! = 6$ fois dans les 24 listes.

Le nombre de groupes est donc :

$$\frac{24}{6} = 4$$

Les 4 groupes sont $\{A, B, C\}$, $\{A, B, D\}$, $\{A, C, D\}$ et $\{B, C, D\}$.

À retenir : changer l'ordre ne crée pas de nouveau groupe, il faut donc **diviser** pour ne pas compter plusieurs fois le même groupe.

---

## 2. Propriétés et calcul

### Notation $\binom{n}{k}$

Le nombre de combinaisons de $k$ éléments parmi $n$ se note :

$$\binom{n}{k}$$

Se lit « **$k$ parmi $n$** ». Dans l'exemple précédent, $\dbinom{4}{3} = 4$.

### Propriétés

Quelques valeurs à connaître :

- $\dbinom{n}{0} = 1$ : il n'y a qu'une seule façon de ne rien choisir ;
- $\dbinom{n}{n} = 1$ : il n'y a qu'une seule façon de tout choisir ;
- $\dbinom{n}{1} = n$ : choisir 1 élément parmi $n$, il y a $n$ choix.

**Symétrie.** Pour tout entier $k$ entre $0$ et $n$ :

$$\binom{n}{k} = \binom{n}{n-k}$$

Choisir $k$ éléments revient à choisir les $n - k$ éléments que l'on laisse de côté. Cette propriété permet de simplifier : $\dbinom{10}{7} = \dbinom{10}{3}$.

**Relation de Pascal** : Pour $0 \leq k \leq n - 1$ :

$$\binom{n}{k} + \binom{n}{k+1} = \binom{n+1}{k+1}$$

Vérification : $\dbinom{4}{1} + \dbinom{4}{2} = 4 + 6 = 10 = \dbinom{5}{2}$.

### Utiliser la méthode
Remarque : $$\binom{10}{3} = \frac{10 \times 9 \times 8 \times 7 \dots \times 2 \times 1}{3! \times 7!}$$
7! = 7 x 6 x 5 x 4 x 3 x 2 x 1

On peut donc simplifier par 7!
Donc :  $$\binom{10}{3} = \frac{10 \times 9 \times 8}{3!}$$


Pour calculer $\dbinom{n}{k}$, on reprend le raisonnement de la partie 1 en deux temps :

1. **Compter les listes** de $k$ éléments distincts, en remplissant les places une par une : $n \times (n-1) \times \dots \times (n-k+1)$, soit $k$ facteurs.
2. **Diviser par $k!$**, car chaque groupe a été compté $k!$ fois (une fois pour chaque ordre possible).

$$\binom{n}{k} = \frac{n \times (n-1) \times \dots \times (n-k+1)}{k!}$$

Cette formule s'écrit aussi avec des factorielles :

$$\binom{n}{k} = \frac{n!}{k!\,(n-k)!}$$

**Exemple :** combien de comités de 3 élèves peut-on former parmi 10 ?

$$\binom{10}{3} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = \frac{720}{6} = 120$$

Il y a 120 comités possibles.

**Autre exemple :** combien de façons de choisir 2 boules parmi 5, en les tirant en même temps ?

$$\binom{5}{2} = \frac{5 \times 4}{2 \times 1} = 10$$

La calculatrice possède aussi une touche pour calculer directement $\dbinom{n}{k}$.
