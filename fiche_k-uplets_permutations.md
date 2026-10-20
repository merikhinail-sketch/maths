# K-uplets et permutations

Cette fiche apprend à compter des listes où l'**ordre** compte : un code à chiffres, un classement, un rangement. L'outil est le principe multiplicatif, appliqué place par place.

---

## 1. k-uplets

### Définition et comprendre ce que c'est

Un **k-uplet** est une liste de $k$ éléments, rangés **dans un ordre précis**. On l'écrit $(x_1\ ;\ x_2\ ;\ \dots\ ;\ x_k)$.

L'ordre compte : changer l'ordre donne un autre k-uplet.

**Exemple :** un code à 4 chiffres est un 4-uplet. Les codes $(1\ ;\ 2\ ;\ 3\ ;\ 4)$ et $(4\ ;\ 3\ ;\ 2\ ;\ 1)$ utilisent les mêmes chiffres, mais ce sont deux codes différents.

### Méthode : remplir les places une par une

Pour compter les k-uplets, imaginer $k$ places à remplir, de gauche à droite. Pour chaque place, se demander : **combien de choix ai-je ?** Puis multiplier tous ces nombres (principe multiplicatif).

**Exemple :** combien de codes à 4 chiffres, tous différents, peut-on former avec les chiffres de 0 à 9 ?

- 1re place : on peut choisir parmi les 10 chiffres, donc **10** possibilités ;
- 2e place : un chiffre est déjà utilisé, il en reste **9** ;
- 3e place : deux chiffres sont déjà utilisés, il en reste **8** ;
- 4e place : trois chiffres sont déjà utilisés, il en reste **7**.

Il reste à tout multiplier :

$$10 \times 9 \times 8 \times 7 = 5\,040$$

Il y a 5 040 codes possibles.

**Et si les chiffres pouvaient se répéter ?** Plus aucun chiffre n'est « utilisé » : chaque place offre alors toujours 10 choix.

$$10 \times 10 \times 10 \times 10 = 10^4 = 10\,000$$

Le point à regarder à chaque fois : un élément déjà placé peut-il être réutilisé ou non ?

---

## 2. Permutations

### Comprendre la différence avec un $k$-uplet

Dans un $k$-uplet, on choisit $k$ éléments **parmi $n$** : certains éléments restent de côté.

Dans une **permutation**, on utilise **tous** les éléments : on se contente de les ranger dans un ordre. Une permutation de $n$ éléments est donc une façon de les mettre tous en ligne.

### La formule : le nombre de permutations

Le raisonnement est le même que précédemment, place par place. Pour ranger $n$ éléments :

- 1re place : $n$ choix ;
- 2e place : $n - 1$ choix ;
- ...
- dernière place : 1 seul choix.

Le nombre de permutations de $n$ éléments est donc :

$$n! = n \times (n-1) \times (n-2) \times \dots \times 2 \times 1$$

Se lit « $n$ factorielle ».

### Exemple

De combien de façons peut-on ranger 4 livres différents sur une étagère ?

$$4! = 4 \times 3 \times 2 \times 1 = 24$$

Il y a 24 rangements possibles.

**Pour bien voir la différence :**

- Ranger **les 5 livres** d'une série sur l'étagère : c'est une permutation, $5! = 120$ ;
- Ranger **3 livres distincts parmi les 5** : c'est un $3$-uplet d'éléments distincts, $5 \times 4 \times 3 = 60$.
