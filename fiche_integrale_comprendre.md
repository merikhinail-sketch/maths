# Comprendre l'intégrale

L'intégrale d'une fonction entre deux bornes est un nombre qui mesure une « aire » sous la courbe, comptée avec un signe. Elle se calcule avec une primitive. Cette fiche donne la définition, son interprétation, et les propriétés de base.

---

## 1. Définition

### Définition de l'intégrale

Soit $f$ une fonction continue sur un intervalle $I$, et soient $a$ et $b$ deux réels de $I$. Soit $F$ une primitive de $f$ sur $I$. L'**intégrale de $f$ entre $a$ et $b$** est le nombre :

$$\int_a^b f(x)\,dx = F(b) - F(a)$$

On utilise souvent la notation $\left[F(x)\right]_a^b$ pour $F(b) - F(a)$.

- $a$ et $b$ sont les **bornes** de l'intégrale ;
- la lettre $x$ est une variable « muette » : $\displaystyle \int_a^b f(x)\,dx = \int_a^b f(t)\,dt$.

**Exemple :** calculer $\displaystyle \int_0^2 x\,dx$.

Une primitive de $x$ est $F(x) = \dfrac{x^2}{2}$. Donc :

$$\int_0^2 x\,dx = \left[\frac{x^2}{2}\right]_0^2 = \frac{2^2}{2} - \frac{0^2}{2} = 2 - 0 = 2$$

### Lien avec une primitive

Le résultat ne dépend **pas** de la primitive choisie. Prendre $F + C$ à la place de $F$ ne change rien, car la constante s'annule :

$$\big(F(b) + C\big) - \big(F(a) + C\big) = F(b) - F(a)$$

Dans l'exemple précédent, avec $F(x) = \dfrac{x^2}{2} + 7$ : $\left(2 + 7\right) - \left(0 + 7\right) = 2$. On trouve le même résultat.

On choisit donc toujours la primitive la plus simple, **sans constante**.

### Interprétation comme aire algébrique

Une **unité d'aire** (u.a.) est l'aire du rectangle de côtés $1$ en abscisse et $1$ en ordonnée.

**Si $f$ est positive** sur $[a\ ;\ b]$ (avec $a \leq b$), l'intégrale $\displaystyle \int_a^b f(x)\,dx$ est l'**aire** du domaine délimité par la courbe de $f$, l'axe des abscisses et les droites $x = a$ et $x = b$.

Vérification avec l'exemple : $\displaystyle \int_0^2 x\,dx = 2$. Le domaine sous la droite $y = x$ entre $0$ et $2$ est un triangle de base $2$ et de hauteur $2$, d'aire $\dfrac{2 \times 2}{2} = 2$ u.a.

**Si $f$ change de signe**, l'intégrale est une **aire algébrique** : les aires situées au-dessus de l'axe des abscisses comptent $+$, celles situées au-dessous comptent $-$.

**Exemple :** $\displaystyle \int_0^2 (x - 1)\,dx = \left[\frac{x^2}{2} - x\right]_0^2 = (2 - 2) - 0 = 0$.

La droite $y = x - 1$ passe sous l'axe sur $[0\ ;\ 1]$ (triangle d'aire $\dfrac{1}{2}$, compté $-\dfrac{1}{2}$) et au-dessus sur $[1\ ;\ 2]$ (triangle d'aire $\dfrac{1}{2}$, compté $+\dfrac{1}{2}$). Les deux se compensent : l'intégrale vaut $0$.

**Si $f$ est négative** sur $[a\ ;\ b]$, l'intégrale est **négative** : c'est l'opposé de l'aire géométrique.

**Exemple :** $\displaystyle \int_0^2 (x - 3)\,dx = \left[\frac{x^2}{2} - 3x\right]_0^2 = (2 - 6) - 0 = -4$.

---

## 2. Propriétés

Dans toutes les propriétés, $f$ et $g$ sont continues sur un intervalle $I$, et $a$, $b$, $c$ sont des réels de $I$.

### Linéarité

L'intégrale d'une somme est la somme des intégrales, et une constante multiplicative sort de l'intégrale :

$$\int_a^b \big(f(x) + g(x)\big)\,dx = \int_a^b f(x)\,dx + \int_a^b g(x)\,dx$$

$$\int_a^b k\,f(x)\,dx = k \int_a^b f(x)\,dx$$

**Exemple :** $\displaystyle \int_0^1 \left(3x^2 + 2\right)dx = 3\int_0^1 x^2\,dx + \int_0^1 2\,dx = 3 \times \frac{1}{3} + 2 = 3$.

Vérification directe : $\left[x^3 + 2x\right]_0^1 = (1 + 2) - 0 = 3$.

### Relation de Chasles

On peut découper l'intervalle d'intégration en deux, en passant par un réel intermédiaire $c$ :

$$\int_a^c f(x)\,dx + \int_c^b f(x)\,dx = \int_a^b f(x)\,dx$$

**Exemple :** avec $f(x) = x$ :

- $\displaystyle \int_0^2 x\,dx = 2$ ;
- $\displaystyle \int_2^3 x\,dx = \left[\frac{x^2}{2}\right]_2^3 = \frac{9}{2} - 2 = \frac{5}{2}$ ;
- $\displaystyle \int_0^3 x\,dx = \left[\frac{x^2}{2}\right]_0^3 = \frac{9}{2}$.

On vérifie : $2 + \dfrac{5}{2} = \dfrac{9}{2}$.

### Changement de sens des bornes

Échanger les bornes change le **signe** de l'intégrale :

$$\int_b^a f(x)\,dx = -\int_a^b f(x)\,dx$$

En particulier, $\displaystyle \int_a^a f(x)\,dx = 0$.

**Exemple :** $\displaystyle \int_2^0 x\,dx = \left[\frac{x^2}{2}\right]_2^0 = 0 - 2 = -2$, c'est l'opposé de $\displaystyle \int_0^2 x\,dx = 2$.
