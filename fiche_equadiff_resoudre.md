# Résoudre une équation différentielle

Cette fiche apprend à résoudre les deux types d'équations différentielles du programme : $y' = ay$ et $y' = ay + b$. Pour chacune, on trouve **toutes** les solutions.

---

## 1. Équations différentielles de la forme $y' = ay$

### Reconnaître une équation de cette forme

Une équation de la forme $y' = ay$ ne contient que $y'$ et un multiple de $y$ : le nombre $a$ est une **constante réelle**, qui ne dépend pas de $x$.

Ces équations différentielles sont-elles de la forme $y' = ay$ ?

- $y' = 3y$ : oui, avec $a = 3$ ;
- $y' = -0{,}5\,y$ : oui, avec $a = -0{,}5$ ;
- $y' = y$ : oui, avec $a = 1$ ;
- $y' = 3y + 1$ : non, il y a un terme constant en plus (c'est la forme de la partie 2).

### Comprendre pourquoi les fonctions exponentielles apparaissent

Résoudre $y' = ay$, c'est chercher une fonction dont la dérivée est **proportionnelle à elle-même**.

Les fonctions exponentielles ont précisément cette propriété :

$$\left(e^{ax}\right)' = a\,e^{ax}$$

Une fonction polynôme, par exemple, perd un degré quand on la dérive : elle ne peut pas rester proportionnelle à elle-même. C'est pourquoi les exponentielles sont les bonnes candidates.

### Déterminer la forme générale des solutions

**Propriété.** Les solutions de l'équation $y' = ay$ sont les fonctions de la forme:

$$y(x) = C\,e^{ax}, \quad C \in \mathbb{R}$$


**Exemples :**

- $y' = 3y$ : 

Les solutions $y(x)$ sont de la forme $Ce^{3x}$. 

- $y' = -0{,}5\,y$ :

Les solutions $y(x)$ sont de la forme $Ce^{-0{,}5x}$.

### Vérifier qu'une expression obtenue est bien solution

Reprendre la méthode en trois temps de la fiche précédente.

**Exemple :** vérifier que $y(x) = e^{3x}$ est solution de $y' = 3y$.

- Dérivée : $y'(x) = 3e^{3x}$.
- Autre côté : $3y(x) = 3e^{3x}$.
- Les deux sont égaux pour tout $x$ : la fonction est bien solution, quelle que soit la valeur de $C$.

### Comprendre le rôle de la constante $C$

La constante $C$ est un **réel quelconque** : chaque valeur donne une solution différente.

- $C = 1$ donne $e^{3x}$ ;
- $C = 5$ donne $5e^{3x}$ ;
- $C = 0$ donne la fonction nulle.

Tant qu'on n'a pas d'information supplémentaire, $C$ reste libre. C'est une **condition initiale** qui permet de fixer sa valeur.

---

## 2. Équations différentielles de la forme $y' = ay + b$

On suppose $a \neq 0$ et $b$ réel, tous deux constants.

### Reconnaître une équation de cette forme

L'équation contient $y'$, un multiple de $y$, **et un terme constant** $b$.

Les équations différentielles suivant sont-elles de la forme $y' = ay+b$ ?   

- $y' = 2y + 6$ : oui, avec $a = 2$ et $b = 6$ ;
- $y' = -0{,}1\,y + 2$ : oui, avec $a = -0{,}1$ et $b = 2$ ;
- $y' = 4y - 8$ : oui, avec $a = 4$ et $b = -8$ (le signe fait partie de $b$).

### Trouver une constante qui donne une solution

On cherche d'abord une solution **constante**, c'est-à-dire une fonction $y(x) = c$ où $c$ est un nombre.

Une fonction constante a une dérivée nulle : $y' = 0$. En remplaçant dans l'équation :

$$0 = a \times c + b \quad \Longrightarrow \quad c = -\frac{b}{a}$$

**Exemple :** pour $y' = 2y + 6$, on a $c = -\dfrac{6}{2} = -3$.

Vérification : $y(x) = -3$ donne $y' = 0$ et $2y + 6 = 2 \times (-3) + 6 = 0$. Les deux côtés sont égaux.

### Déterminer la forme générale des solutions

**Propriété.** Pour $a \neq 0$, les solutions de $y' = ay + b$ sont les fonctions :

$$y(x) = C\,e^{ax} - \frac{b}{a}, \quad C \in \mathbb{R}$$

**Exemple :** pour $y' = 2y + 6$, les solutions sont $y(x) = Ce^{2x} - 3$.

### Comprendre le lien avec l'équation $y' = ay$

La forme générale se lit en deux morceaux :

$$y(x) = \underbrace{C\,e^{ax}}_{\text{solutions de } y' = ay} \;\; \underbrace{-\;\frac{b}{a}}_{\text{la constante trouvée}}$$

D'où vient ce résultat ? Notons $c = -\dfrac{b}{a}$ la constante précédente, et posons $z = y - c$. Alors :

$$z' = y' = ay + b = a(y - c) + ac + b = a z$$

car $ac + b = 0$. La fonction $z$ vérifie donc $z' = az$, c'est-à-dire $z(x) = Ce^{ax}$. Ainsi $y = z + c = Ce^{ax} + c$.

### Vérifier la solution obtenue

**Exemple :** vérifier que $y(x) = e^{2x} - 3$ est solution de $y' = 2y + 6$.

- Dérivée : $y'(x) = 2e^{2x}$.
- Autre côté : $2y(x) + 6 = 2\left(e^{2x} - 3\right) + 6 = 2e^{2x} - 6 + 6 = 2e^{2x}$.
- Les deux sont égaux pour tout $x$ : la fonction est bien solution.

---

## 3. Grand exemple guidé

**Énoncé.** Une boisson chaude est posée dans une pièce à 20 °C. Sa température $T(t)$, en °C, au bout de $t$ minutes vérifie :

$$T'(t) = -0{,}1\,T(t) + 2$$

Déterminer toutes les fonctions $T$ solutions de cette équation.

### Reconnaître le type d'équation

L'équation contient $T'$, un multiple de $T$, et un terme constant. C'est de la forme $y' = ay + b$, avec $y = T$ et la variable $t$ :

$$a = -0{,}1 \qquad b = 2$$

### Choisir la méthode adaptée

Pour une équation $y' = ay + b$ :

1. chercher la constante qui est solution ;
2. ajouter $Ce^{at}$ pour obtenir toutes les solutions.

### Déterminer la forme des solutions

D'après la méthode, les solutions s'écrivent :

$$T(t) = C\,e^{-0{,}1t} + c$$

où $c$ est la constante solution de l'équation.

### Effectuer les calculs

Calculer la constante : $c = -\dfrac{b}{a} = -\dfrac{2}{-0{,}1} = 20$.

Les solutions sont donc :

$$T(t) = C\,e^{-0{,}1t} + 20, \quad C \in \mathbb{R}$$

### Vérifier le résultat

- Dérivée : $T'(t) = -0{,}1\,Ce^{-0{,}1t}$.
- Autre côté : $-0{,}1\,T(t) + 2 = -0{,}1\left(Ce^{-0{,}1t} + 20\right) + 2 = -0{,}1\,Ce^{-0{,}1t} - 2 + 2 = -0{,}1\,Ce^{-0{,}1t}$.

Les deux côtés sont égaux : la fonction est bien solution.

### Comparer avec la situation de départ

Quand $t$ devient grand, $e^{-0{,}1t}$ se rapproche de 0, donc $T(t)$ se rapproche de **20**, quelle que soit la valeur de $C$. La boisson finit par prendre la température de la pièce : c'est cohérent avec la situation.

La constante $C$ dépend de la température de départ :

- si $C > 0$, la boisson est plus chaude que la pièce et elle refroidit ;
- si $C < 0$, la boisson est plus froide que la pièce et elle se réchauffe.

La température de départ permettra de fixer $C$ : c'est l'objet de la fiche suivante.

---

## 4. Erreurs fréquentes

### Confondre les formes $y' = ay$ et $y' = ay + b$

Regarder s'il y a un terme constant. Les solutions n'ont pas la même forme :

- $y' = ay$ : $y(x) = Ce^{ax}$ ;
- $y' = ay + b$ : $y(x) = Ce^{ax} - \dfrac{b}{a}$.

### Oublier le terme constant $b$ dans la résolution de $y' = ay + b$

Pour $y' = 2y + 6$, écrire $y(x) = Ce^{2x}$ est faux. Le test de vérification le montre : $y' = 2Ce^{2x}$, mais $2y + 6 = 2Ce^{2x} + 6$, et ces deux expressions ne sont pas égales.

La bonne réponse est $y(x) = Ce^{2x} - 3$.

### Se tromper dans la forme générale des solutions

Deux erreurs de signe sont fréquentes :

- **le signe de l'exposant** : pour $y' = -3y$, la solution est $Ce^{-3x}$, pas $Ce^{3x}$ ;
- **le signe de la constante** : pour $y' = -0{,}1\,y + 2$, la constante est $-\dfrac{b}{a} = -\dfrac{2}{-0{,}1} = +20$, pas $-20$.

### Oublier la constante $C$ lorsqu'on cherche l'ensemble des solutions

Écrire $y(x) = e^{2x}$ ne donne **qu'une** solution. Pour l'ensemble des solutions de $y' = 2y$, écrire $y(x) = Ce^{2x}$ avec $C \in \mathbb{R}$.

### Faire une erreur de calcul dans la détermination de la solution

Le calcul de $-\dfrac{b}{a}$ demande de la rigueur, surtout avec des signes négatifs.

Pour $y' = 4y - 8$, on a $b = -8$ : la constante est $-\dfrac{-8}{4} = 2$, et non $-2$. 

Vérification : $y = 2$ donne $y' = 0$ et $4 \times 2 - 8 = 0$.

### Ne pas vérifier que la fonction obtenue satisfait bien l'équation différentielle

Prendre 30 secondes pour vérifier : dériver, remplacer $y$ dans l'équation, comparer. Cette vérification détecte la plupart des erreurs de signe et les oublis de constante.
