# La loi binomiale

Cette fiche apprend à reconnaître une loi binomiale et à l'utiliser. Un grand exemple guidé sert de fil conducteur : le suivre étape par étape, en refaisant les calculs.

---

## Grand exemple guidé

**Énoncé.** Un joueur de basket effectue 3 lancers francs. À chaque lancer, il réussit avec une probabilité de $0{,}6$, indépendamment des autres lancers.

On s'intéresse au nombre de lancers réussis.

### Reconnaître une situation de Bernoulli

Une **épreuve de Bernoulli** est une expérience qui n'a que **deux issues** :

- le **succès** $S$, de probabilité $p$ ;
- l'**échec** $E$, de probabilité $1 - p$.

Ici, un lancer franc est une épreuve de Bernoulli : réussi ($S$) avec $p = 0{,}6$, raté ($E$) avec $1 - p = 0{,}4$.

Répéter plusieurs fois la même épreuve de façon indépendante s'appelle un **schéma de Bernoulli**. Ici, on répète $n = 3$ fois.

Vérifier les trois conditions :

- **la même épreuve est répétée** : chaque lancer est identique ;
- **chaque épreuve a deux issues** : réussi ou raté ;
- **les épreuves sont indépendantes** : c'est précisé dans l'énoncé.

### Construire le schéma

Représenter les 3 lancers dans un arbre. Chaque trajet de gauche à droite est une suite de résultats possibles. Le nombre à droite est le nombre de succès dans ce trajet.

```
Début
├── S (0,6)
│   ├── S (0,6)
│   │   ├── S (0,6)   → SSS   3 succès
│   │   └── E (0,4)   → SSE   2 succès
│   └── E (0,4)
│       ├── S (0,6)   → SES   2 succès
│       └── E (0,4)   → SEE   1 succès
└── E (0,4)
    ├── S (0,6)
    │   ├── S (0,6)   → ESS   2 succès
    │   └── E (0,4)   → ESE   1 succès
    └── E (0,4)
        ├── S (0,6)   → EES   1 succès
        └── E (0,4)   → EEE   0 succès
```

### Définir la variable aléatoire

Écrire précisément ce que compte la variable aléatoire :

> Soit $X$ la variable aléatoire égale au **nombre de lancers réussis** parmi les 3 lancers.

$X$ peut prendre les valeurs $0$, $1$, $2$ ou $3$.

### Identifier la loi binomiale

$X$ compte le nombre de succès dans un schéma de Bernoulli de $n = 3$ épreuves, avec une probabilité de succès $p = 0{,}6$. $X$ suit donc la **loi binomiale** de paramètres $n = 3$ et $p = 0{,}6$ :

$$X \sim \mathcal{B}(3\ ;\ 0{,}6)$$

Pour tout entier $k$ entre $0$ et $n$ :

$$P(X = k) = \binom{n}{k} \, p^k \, (1 - p)^{n-k}$$

D'où vient cette formule ? Sur l'arbre :

- chaque chemin avec exactement $k$ succès a pour probabilité $p^k (1 - p)^{n-k}$ (on multiplie les branches) ;
- le nombre de chemins avec exactement $k$ succès est $\dbinom{n}{k}$.

Il suffit de multiplier les deux. Pour $k = 2$ : les chemins $SSE$, $SES$ et $ESS$ sont au nombre de $\dbinom{3}{2} = 3$, et chacun a pour probabilité $0{,}6^2 \times 0{,}4$.

### Calculer des probabilités

**Probabilité d'avoir exactement 2 lancers réussis :**

$$P(X = 2) = \binom{3}{2} \times 0{,}6^2 \times 0{,}4^1 = 3 \times 0{,}36 \times 0{,}4 = 0{,}432$$

On calcule de même les autres valeurs :

| $k$ | $0$ | $1$ | $2$ | $3$ |
|---|---|---|---|---|
| $P(X = k)$ | $0{,}064$ | $0{,}288$ | $0{,}432$ | $0{,}216$ |

Vérification : $0{,}064 + 0{,}288 + 0{,}432 + 0{,}216 = 1$.

**Probabilité d'avoir au moins 1 lancer réussi.** Passer par l'événement contraire est plus rapide : « au moins 1 » est le contraire de « aucun ».

$$P(X \geq 1) = 1 - P(X = 0) = 1 - 0{,}064 = 0{,}936$$

**Probabilité d'avoir au plus 1 lancer réussi.**

$$P(X \leq 1) = P(X = 0) + P(X = 1) = 0{,}064 + 0{,}288 = 0{,}352$$

La calculatrice permet aussi de calculer ces probabilités avec sa fonction de loi binomiale.

### Calculer et interpréter l'espérance

Pour une loi binomiale :

$$E(X) = n \times p$$

$$E(X) = 3 \times 0{,}6 = 1{,}8$$

**Interprétation.** Si le joueur effectuait un très grand nombre de séries de 3 lancers, il réussirait en moyenne 1,8 lancer par série. Ce n'est pas un nombre de réussites possible lors d'une série (on réussit 0, 1, 2 ou 3 lancers), mais c'est la moyenne sur de nombreuses séries.

Sur une copie il faudrait écrire :

**Un lancer franc représente une épreuve de Bernoulli de succès $0{,}6$.**

**On répète cette épreuve de Bernoulli $3$ fois de manière indépendante.**

**La variable aléatoire $X$ compte le nombre de succès.**

**Ainsi, $X$ suit la loi binomiale $\mathcal{B}(3\,;0{,}6)$.**


---

## Erreurs fréquentes

### Ne pas vérifier les conditions d'une loi binomiale

Avant d'utiliser la loi binomiale, vérifier les trois conditions : **même épreuve répétée, deux issues, épreuves indépendantes**.

Tirer 3 boules **sans remise** dans une urne et compter les boules rouges ne donne pas une loi binomiale : la composition de l'urne change à chaque tirage, donc les tirages ne sont pas indépendants et la probabilité de succès n'est pas constante.

### Confondre $n$ et $p$

$n$ est le **nombre d'épreuves** (un entier), $p$ est la **probabilité de succès** (un nombre entre 0 et 1). Dans $\mathcal{B}(n\ ;\ p)$, $n$ vient en premier.

Dans notre exemple : $n = 3$ lancers et $p = 0{,}6$. Écrire $\mathcal{B}(0{,}6\ ;\ 3)$ est faux.

### Mal définir la variable aléatoire

Toujours préciser ce que $X$ compte, sans laisser d'ambiguïté. Écrire seulement « $X$ est le nombre de succès » ne suffit pas.

Écrire : « Soit $X$ la variable aléatoire égale au nombre de lancers réussis parmi les 3 lancers. »

### Confondre $P(X = k)$ avec $P(X \leq k)$, $P(X \geq k)$, etc.

Lire l'énoncé avec soin :

- « exactement $k$ » : $P(X = k)$ ;
- « au plus $k$ » : $P(X \leq k)$ ;
- « au moins $k$ » : $P(X \geq k)$.

Dans notre exemple :

- $P(X = 2) = 0{,}432$ ;
- $P(X \leq 2) = 0{,}064 + 0{,}288 + 0{,}432 = 0{,}784$ ;
- $P(X \geq 2) = 0{,}432 + 0{,}216 = 0{,}648$.

### Se tromper dans le coefficient binomial $\binom{n}{k}$

$\dbinom{n}{k}$ est le nombre de chemins ayant $k$ succès parmi $n$ épreuves. Ce n'est ni $n \times k$, ni $n^k$.

Par exemple $\dbinom{4}{2} = 6$, et non $4 \times 2 = 8$. On a aussi $\dbinom{n}{0} = 1$ et $\dbinom{n}{n} = 1$.

Autre oubli classique : omettre le coefficient. Calculer $0{,}6^2 \times 0{,}4 = 0{,}144$ donne la probabilité d'**un seul** chemin à 2 succès. Il en existe 3, d'où $3 \times 0{,}144 = 0{,}432$.

### Mal interpréter l'espérance

$E(X) = np$ représente le **nombre moyen de succès** sur un grand nombre de séries, pas forcément un nombre de succès possible.

Ici, $E(X) = 1{,}8$ alors que le joueur réussit $0$, $1$, $2$ ou $3$ lancers lors d'une série. 1,8 n'est jamais obtenu lors d'une série ; c'est la moyenne.
