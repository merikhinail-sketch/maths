# Intégration par parties

Certaines intégrales de produits ne se calculent pas avec les primitives usuelles. L'intégration par parties est une méthode qui les transforme en une intégrale plus simple. Cette fiche explique son principe, la marche à suivre, puis déroule un grand exemple.

---

## 1. Comprendre l'intégration par parties

### À quoi sert cette méthode ?

Elle sert à calculer l'intégrale d'un **produit de deux fonctions** quand on ne connaît pas directement une primitive de ce produit.

**Exemple :** $\displaystyle \int_0^1 x\,e^x\,dx$. Dans le tableau des primitives usuelles, aucune ligne ne donne une primitive de $x\,e^x$. On ne trouve pas de primitive.

### Reconnaître les situations où elle est utile

Chercher un **produit** dont l'un des facteurs se simplifie quand on le dérive. Les cas les plus courants :

- polynôme $\times$ exponentielle : $x\,e^x$, $(2x+1)\,e^x$ ;
- polynôme $\times$ cosinus ou sinus : $x\cos(x)$, $x\sin(x)$ ;
- polynôme $\times$ logarithme : $x\ln(x)$, $x^2\ln(x)$.

Avant de se lancer, vérifier qu'une méthode plus simple ne suffit pas (voir les erreurs fréquentes).

### Comprendre le principe de la méthode

La méthode vient de la formule de dérivation d'un produit. Si $u$ et $v$ sont dérivables :

$$(u\,v)' = u'\,v + u\,v'$$

On isole le terme qui nous intéresse :

$$u\,v' = (u\,v)' - u'\,v$$

En intégrant entre $a$ et $b$, on obtient la **formule d'intégration par parties**. Si $u$ et $v$ sont dérivables, avec des dérivées continues, alors :

$$\int_a^b u(x)\,v'(x)\,dx = \Big[u(x)\,v(x)\Big]_a^b - \int_a^b u'(x)\,v(x)\,dx$$

L'idée : on remplace l'intégrale de départ, $\int u\,v'$, par une autre, $\int u'\,v$, **plus simple** à calculer.

---

## 2. Appliquer la méthode

**Exemple fil conducteur :** $\displaystyle I = \int_0^1 x\,e^x\,dx$.

### Choisir les fonctions $u$ et $v'$

Il faut décomposer le produit en deux facteurs : l'un sera $u$ (on le **dérivera**), l'autre sera $v'$ (on le **primitivera**).

Règle de choix :

- $u$ : le facteur qui **se simplifie** quand on le dérive (un polynôme dont le degré baisse, ou $\ln(x)$ dont la dérivée est $\dfrac{1}{x}$) ;
- $v'$ : le facteur dont on **connaît une primitive** (une exponentielle, un cosinus, un sinus, une puissance de $x$). Le but est de rendre les calculs le plus simple possible.

| Produit | Choix de $u$ | Choix de $v'$ |
|---|---|---|
| $x\,e^x$, $x\cos(x)$, $x\sin(x)$ | $u = x$ | $v' = e^x$, $\cos(x)$, $\sin(x)$ |
| $x\ln(x)$, $x^2\ln(x)$ | $u = \ln(x)$ | $v' = x$, $x^2$ |

Pour $I = \displaystyle\int_0^1 x\,e^x\,dx$ : $u(x) = x$ et $v'(x) = e^x$.

### Déterminer $u'$ et $v$

- On **dérive** $u$ : $u'(x) = 1$.
- On **primitive** $v'$ : $v(x) = e^x$. Une seule primitive suffit, sans constante.

### Appliquer la formule d'intégration par parties

$$I = \Big[x\,e^x\Big]_0^1 - \int_0^1 1 \times e^x\,dx$$

### Calculer et simplifier le résultat

- Le crochet : $\Big[x\,e^x\Big]_0^1 = 1 \times e^1 - 0 \times e^0 = e$.
- La nouvelle intégrale : $\displaystyle \int_0^1 e^x\,dx = \Big[e^x\Big]_0^1 = e - 1$.

$$I = e - (e - 1) = 1$$

On retrouve que $x \mapsto (x - 1)\,e^x$ est une primitive de $x\,e^x$ : $\Big[(x-1)e^x\Big]_0^1 = 0 - (-1) = 1$.

---

## 3. Grand exemple guidé

**Énoncé.** Calculer :

$$I = \int_1^e x\ln(x)\,dx$$

### Identifier les fonctions à choisir

L'intégrale est un produit de $x$ et de $\ln(x)$. On ne connaît pas de primitive de $\ln(x)$ dans le tableau usuel, en revanche sa dérivée est simple : $\dfrac{1}{x}$. Et on connaît une primitive de $x$.

On choisit donc :

- $u(x) = \ln(x)$ ;
- $v'(x) = x$.

### Calculer leurs dérivées et primitives nécessaires

- $u'(x) = \dfrac{1}{x}$ ;


- $v(x) = \dfrac{x^2}{2}$.



### Appliquer la formule étape par étape

$$I = \Big[u\,v\Big]_1^e - \int_1^e u'\,v\,dx = \left[\frac{x^2}{2}\ln(x)\right]_1^e - \int_1^e \frac{1}{x} \times \frac{x^2}{2}\,dx$$

### Terminer le calcul

**Le crochet.** Remplacer par les bornes :

$$\left[\frac{x^2}{2}\ln(x)\right]_1^e = \frac{e^2}{2}\ln(e) - \frac{1}{2}\ln(1) = \frac{e^2}{2} \times 1 - \frac{1}{2} \times 0 = \frac{e^2}{2}$$

**La nouvelle intégrale.** Simplifier d'abord l'expression : $\dfrac{1}{x} \times \dfrac{x^2}{2} = \dfrac{x}{2}$. Donc :

$$\int_1^e \frac{x}{2}\,dx = \left[\frac{x^2}{4}\right]_1^e = \frac{e^2}{4} - \frac{1}{4} = \frac{e^2 - 1}{4}$$

**Résultat.**

$$I = \frac{e^2}{2} - \frac{e^2 - 1}{4} = \frac{2e^2 - e^2 + 1}{4} = \frac{e^2 + 1}{4} \approx 2{,}10$$

### Vérifier le résultat

**Vérification 1 : dériver la primitive obtenue.** La méthode a fourni la primitive $G(x) = \dfrac{x^2}{2}\ln(x) - \dfrac{x^2}{4}$. Dérivons-la :

$$G'(x) = x\ln(x) + \frac{x^2}{2} \times \frac{1}{x} - \frac{x}{2} = x\ln(x) + \frac{x}{2} - \frac{x}{2} = x\ln(x)$$

On retrouve bien l'expression à intégrer.

**Vérification 2 : le signe.** Sur $[1\ ;\ e]$, $\ln(x) \geq 0$, donc $x\ln(x) \geq 0$ : l'intégrale doit être positive. C'est bien le cas.

---

## 4. Erreurs fréquentes

### Faire un mauvais choix de $u$ et $v'$

Choisir $u$ comme le facteur qui se simplifie en dérivant. Un mauvais choix complique l'intégrale au lieu de la simplifier.

Pour $\displaystyle\int_0^1 x\,e^x\,dx$ avec $u = e^x$ et $v' = x$ : on a $v = \dfrac{x^2}{2}$, et la nouvelle intégrale est $\displaystyle\int_0^1 e^x \times \dfrac{x^2}{2}\,dx$, avec une puissance de $x$ plus grande qu'au départ. Le choix $u = x$ est le bon.

### Se tromper dans le calcul de $u'$ ou de $v$

$u'$ est une **dérivée**, $v$ est une **primitive**. Ne pas les confondre.

- si $v'(x) = \sin(x)$, alors $v(x) = -\cos(x)$ (et non $\cos(x)$) ;
- si $v'(x) = e^{2x}$, alors $v(x) = \dfrac{1}{2}e^{2x}$ (le coefficient compte) ;
- si $u(x) = \ln(x)$, alors $u'(x) = \dfrac{1}{x}$.

### Oublier les bornes dans une intégrale définie

Les bornes doivent apparaître **dans le crochet** et **dans la nouvelle intégrale**.

Pour $I = \displaystyle\int_0^1 x\,e^x\,dx$, on écrit :

$$I = \Big[x\,e^x\Big]_0^1 - \int_0^1 e^x\,dx$$

et non $I = x\,e^x - \displaystyle\int e^x\,dx$ (qui ne donne pas un nombre).

### Faire une erreur de signe ou mal appliquer la formule

La formule contient un **signe moins** devant la nouvelle intégrale :

$$\int_a^b u\,v' = \Big[u\,v\Big]_a^b - \int_a^b u'\,v$$

**Exemple :** $\displaystyle \int_0^{\pi/2} x\sin(x)\,dx$, avec $u = x$ et $v' = \sin(x)$, donc $u' = 1$ et $v = -\cos(x)$.

$$\int_0^{\pi/2} x\sin(x)\,dx = \Big[-x\cos(x)\Big]_0^{\pi/2} - \int_0^{\pi/2} \big(-\cos(x)\big)\,dx = 0 + \Big[\sin(x)\Big]_0^{\pi/2} = 1$$

Une erreur de signe donnerait $-1$. Un test rapide l'exclut : la fonction $x\sin(x)$ est positive sur $\left[0\ ;\ \dfrac{\pi}{2}\right]$, donc l'intégrale doit être positive.

### Commettre une erreur de calcul

Les erreurs viennent souvent de la simplification ou de l'évaluation aux bornes.

- simplifier avec soin : $\dfrac{1}{x} \times \dfrac{x^2}{2} = \dfrac{x}{2}$, et non $\dfrac{x^2}{2x}$ laissé tel quel ou $\dfrac{x^2}{2}$ ;
- se souvenir que $\ln(1) = 0$ et $\ln(e) = 1$ quand on remplace par les bornes.

### Utiliser l'intégration par parties alors qu'une méthode plus simple suffit

Avant d'intégrer par parties, chercher une primitive directe.

**Exemple :** $\displaystyle \int_0^1 2x\,e^{x^2}\,dx$. C'est un produit, mais il est de la forme $u'\,e^{u}$ avec $u(x) = x^2$ : une primitive est $e^{x^2}$.

$$\int_0^1 2x\,e^{x^2}\,dx = \Big[e^{x^2}\Big]_0^1 = e - 1$$

L'intégration par parties est inutile ici.
