# Rappels de Première : probabilités conditionnelles

Cette fiche rassemble les rappels de Première utiles pour les probabilités conditionnelles en Terminale. Un même exemple sert de fil conducteur du début à la fin.

**Situation :** dans un groupe de 100 élèves, 60 sont des filles et 40 sont des garçons. Parmi les filles, 18 pratiquent la natation. Parmi les garçons, 20 pratiquent la natation.

On choisit un élève au hasard et on note :

- $F$ : « l'élève est une fille » ;
- $G$ : « l'élève est un garçon » ;
- $N$ : « l'élève pratique la natation ».

---

## 1. Probabilité conditionnelle

### Comprendre ce que signifie $P_A(B)$

$P_A(B)$ se lit « probabilité de $B$ sachant $A$ ». C'est la probabilité que $B$ se réalise **quand on sait déjà que $A$ est réalisé**.

On ne regarde plus tous les cas possibles, mais seulement ceux où $A$ est réalisé : l'ensemble des possibilités se restreint à $A$.

**Exemple :** $P_F(N)$ est la probabilité qu'un élève pratique la natation, sachant que c'est une fille. On ne regarde que les 60 filles : 18 d'entre elles font de la natation.

$$P_F(N) = \frac{18}{60} = 0{,}3$$

Autrement dit, 30 % des filles pratiquent la natation.

### Calculer une probabilité conditionnelle

Pour deux événements $A$ et $B$ avec $P(A) \neq 0$ :

$$P_A(B) = \frac{P(A \cap B)}{P(A)}$$

Cette formule se retourne en :

$$P(A \cap B) = P(A) \times P_A(B)$$

**Exemple :** $P(F) = 0{,}6$ et $P(F \cap N) = \dfrac{18}{100} = 0{,}18$. Donc :

$$P_F(N) = \frac{0{,}18}{0{,}6} = 0{,}3$$

On retrouve bien le résultat précédent.

### Reconnaître une situation conditionnelle

Repérer les expressions qui indiquent une condition : « sachant que », « parmi », « si l'on sait que », « dans le cas où ».

Comparer ces trois questions, qui semblent proches mais ne demandent pas la même chose :

- « Quelle est la probabilité qu'un élève soit une fille **et** pratique la natation ? » C'est une intersection : $P(F \cap N) = 0{,}18$.
- « Quelle est la probabilité qu'un élève pratique la natation, **sachant que** c'est une fille ? » C'est une probabilité conditionnelle : $P_F(N) = 0{,}3$.
- « Un élève pratique la natation. Quelle est la probabilité que ce soit une fille ? » La condition est « il pratique la natation » : $P_N(F) = \dfrac{18}{38} \approx 0{,}47$.

Astuce : l'événement que l'on **sait déjà réalisé** est celui qui se place en indice.

---

## 2. Arbres de probabilités

### Construire un arbre

Un arbre représente une expérience en plusieurs étapes. Chaque étape donne un niveau de branches. Sur chaque branche, écrire la probabilité correspondante.

```
Début
├── F (0,6)
│   ├── N (0,3)
│   └── non N (0,7)
└── G (0,4)
    ├── N (0,5)
    └── non N (0,5)
```

Règle : au départ d'un même nœud, la somme des probabilités des branches vaut 1.

### Lire les probabilités sur les branches

- Une branche du **premier niveau** porte une probabilité simple : par exemple $P(F) = 0{,}6$.
- Une branche du **deuxième niveau** porte une probabilité conditionnelle : elle suppose que l'on est déjà passé par la branche précédente. Par exemple, la branche $F \to N$ porte $P_F(N) = 0{,}3$.

### Calculer une probabilité en suivant un chemin

Pour trouver la probabilité d'un chemin, **on multiplie** les probabilités des branches qu'il traverse. C'est la formule $P(A \cap B) = P(A) \times P_A(B)$ lue sur l'arbre.

**Exemple :** le chemin $F \to N$ donne

$$P(F \cap N) = 0{,}6 \times 0{,}3 = 0{,}18$$

et le chemin $G \to N$ donne

$$P(G \cap N) = 0{,}4 \times 0{,}5 = 0{,}2$$

---

## 3. Indépendance

### Reconnaître deux événements indépendants

Deux événements $A$ et $B$ sont **indépendants** si :

$$P(A \cap B) = P(A) \times P(B)$$

L'idée : savoir que $A$ est réalisé ne change rien à la probabilité de $B$.

Pour le vérifier, calculer les deux côtés de l'égalité et les comparer.

**Exemple (événements non indépendants) :** $F$ et $N$ dans notre groupe.

- $P(F) \times P(N) = 0{,}6 \times 0{,}38 = 0{,}228$
- $P(F \cap N) = 0{,}18$

Les deux valeurs sont différentes : $F$ et $N$ ne sont pas indépendants.

**Exemple (événements indépendants) :** on lance une pièce équilibrée et un dé équilibré. $A$ : « pile », $B$ : « obtenir 6 ».

- $P(A \cap B) = \dfrac{1}{12}$
- $P(A) \times P(B) = \dfrac{1}{2} \times \dfrac{1}{6} = \dfrac{1}{12}$

Les deux valeurs sont égales : $A$ et $B$ sont indépendants.

### Lien avec les probabilités conditionnelles

Si $P(A) \neq 0$, dire que $A$ et $B$ sont indépendants revient à dire que :

$$P_A(B) = P(B)$$

La condition « $A$ est réalisé » ne modifie pas la probabilité de $B$.

**Exemple :** $P_F(N) = 0{,}3$ alors que $P(N) = 0{,}38$. Les deux sont différents : on retrouve que $F$ et $N$ ne sont pas indépendants.

Sur un arbre, cela se voit quand les branches du deuxième niveau portent les mêmes probabilités quel que soit le chemin emprunté.

---

## 4. Probabilités totales

### Utiliser un arbre pour calculer une probabilité globale

Pour calculer la probabilité globale d'un événement, on repère  **tous les chemins** de l'arbre qui y mènent, puis procéder en deux temps :

1. **Multiplier** les probabilités le long de chaque chemin ;
2. **Additionner** les résultats de tous ces chemins.

**Exemple :** calculer $P(N)$. Deux chemins mènent à $N$ : $F \to N$ et $G \to N$.

$$P(N) = P(F \cap N) + P(G \cap N) = 0{,}18 + 0{,}2 = 0{,}38$$

C'est la **formule des probabilités totales**. Ici, $F$ et $G$ partagent l'ensemble des élèves en deux groupes sans chevauchement :

$$P(N) = P(F) \times P_F(N) + P(G) \times P_G(N)$$

Avec plus de deux branches au premier niveau, le principe reste le même : additionner les chemins qui mènent à l'événement.

---

## 5. Quelques erreurs fréquentes

### Confondre $P_A(B)$ et $P_B(A)$

Ces deux probabilités répondent à des questions différentes.

Dans notre groupe, $P_F(N) = 0{,}3$ (parmi les filles, la part qui fait de la natation) alors que $P_N(F) \approx 0{,}47$ (parmi les nageurs, la part de filles).

### Confondre $P_A(B)$ et $P(A \cap B)$

La probabilité conditionnelle se calcule sur $A$ seulement ; l'intersection se calcule sur l'ensemble de la population.

Ici, $P_F(N) = 0{,}3$ mais $P(F \cap N) = 0{,}18$. La différence vient du dénominateur : $P(F)$ pour l'une, 1 pour l'autre.

### Additionner au lieu de multiplier le long d'un chemin

Le long d'un chemin, **multiplier**. Entre plusieurs chemins qui mènent au même événement, **additionner**.

Pour le chemin $F \to N$ : $0{,}6 \times 0{,}3 = 0{,}18$, et non $0{,}6 + 0{,}3 = 0{,}9$.

### Oublier un chemin dans le calcul d'une probabilité globale

Pour obtenir $P(N)$, il faut tous les chemins qui mènent à $N$.

Ne compter que le chemin $F \to N$ donne $0{,}18$, alors que le résultat est $0{,}38$ : le chemin $G \to N$ a été oublié.

### Confondre événements indépendants et événements incompatibles

Deux événements sont **incompatibles** lorsqu'ils ne peuvent pas se réaliser en même temps : $P(A \cap B) = 0$. Ce n'est pas du tout la même notion que l'indépendance.

Ici, $F$ et $G$ sont incompatibles (aucun élève n'est à la fois une fille et un garçon), donc $P(F \cap G) = 0$. Mais $P(F) \times P(G) = 0{,}24 \neq 0$ : ils ne sont pas indépendants.
