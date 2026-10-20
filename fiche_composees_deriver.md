# Dériver une fonction composée

Pour dériver une fonction composée, il suffit de suivre une règle en deux gestes : **dériver l'extérieur, puis multiplier par la dérivée de l'intérieur**. Cette fiche déroule la méthode sur un exemple, puis donne les formes à reconnaître.

**La formule.** Si $f = v \circ u$, c'est-à-dire $f(x) = v\big(u(x)\big)$, alors :

$$f'(x) = u'(x) \times v'\big(u(x)\big)$$

---

## 1. Grand exemple guidé

**Énoncé.** Dériver la fonction $f$ définie sur $\mathbb{R}$ par :

$$f(x) = \sqrt{x^2 + 1}$$

### Identifier la fonction intérieure et la fonction extérieure

- fonction intérieure : $u(x) = x^2 + 1$ ;
- fonction extérieure : $v(X) = \sqrt{X}$.

Comme $x^2 + 1 > 0$ pour tout réel $x$, la fonction $f$ est bien définie et dérivable sur $\mathbb{R}$.

### Dériver la fonction extérieure

La dérivée de $v(X) = \sqrt{X}$ est :

$$v'(X) = \frac{1}{2\sqrt{X}}$$

Remplacer $X$ par $u(x)$, sans toucher à l'intérieur :

$$v'\big(u(x)\big) = \frac{1}{2\sqrt{x^2 + 1}}$$

### Multiplier par la dérivée de la fonction intérieure

La dérivée de $u(x) = x^2 + 1$ est $u'(x) = 2x$. Donc :

$$f'(x) = u'(x) \times g'\big(u(x)\big) = 2x \times \frac{1}{2\sqrt{x^2 + 1}}$$

### Simplifier

Simplifier par $2$ :

$$f'(x) = \frac{2x}{2\sqrt{x^2 + 1}} = \frac{x}{\sqrt{x^2 + 1}}$$

Le dénominateur est toujours strictement positif : le signe de $f'(x)$ est celui de $x$. La fonction $f$ est donc décroissante sur $]-\infty\ ;\ 0]$ et croissante sur $[0\ ;\ +\infty[$.

### Reconnaître les principales formes à dériver

Dans chaque ligne, $u$ est une fonction dérivable.

| Forme de $f$ | Dérivée $f'$ | Condition | Exemple |
|---|---|---|---|
| $u^n$ | $n \, u' \, u^{n-1}$ | | $\left((3x-1)^4\right)' = 4 \times 3 \times (3x-1)^3 = 12(3x-1)^3$ |
| $e^{u}$ | $u' \, e^{u}$ | | $\left(e^{x^2 - 3x}\right)' = (2x - 3)\,e^{x^2 - 3x}$ |
| $\ln(u)$ | $\dfrac{u'}{u}$ | $u > 0$ | $\left(\ln(x^2+1)\right)' = \dfrac{2x}{x^2 + 1}$ |
| $\sqrt{u}$ | $\dfrac{u'}{2\sqrt{u}}$ | $u > 0$ | $\left(\sqrt{2x+1}\right)' = \dfrac{2}{2\sqrt{2x+1}} = \dfrac{1}{\sqrt{2x+1}}$ |
| $\dfrac{1}{u}$ | $-\dfrac{u'}{u^2}$ | $u \neq 0$ | $\left(\dfrac{1}{x+4}\right)' = -\dfrac{1}{(x+4)^2}$ |

Cas particulier très fréquent : quand $u(x) = ax + b$, on a $u' = a$, et la formule devient $\big(v(ax+b)\big)' = a \times v'(ax+b)$. Par exemple, $\left(e^{2x}\right)' = 2e^{2x}$.

---

## 2. Erreurs fréquentes

### Mal identifier les fonctions intérieure et extérieure et mal appliquer la formule de dérivation

Identifier d'abord $u$ et $g$, puis appliquer la formule dans l'ordre : dériver $g$, remplacer par $u(x)$, multiplier par $u'$.

Pour $f(x) = (3x - 1)^4$, la fonction intérieure est $u(x) = 3x - 1$ et la fonction extérieure est $g(X) = X^4$. Dériver comme si $3x - 1$ était $x$ donnerait $4(3x-1)^3$, ce qui est faux.

### Oublier de multiplier par la dérivée de la fonction intérieure

C'est l'erreur la plus fréquente.

$\left(e^{2x}\right)' = 2e^{2x}$, et non $e^{2x}$.

Pour $f(x) = (3x - 1)^4$ : $f'(x) = 4(3x-1)^3 \times 3 = 12(3x-1)^3$, et non $4(3x-1)^3$.

### Se tromper dans les dérivées usuelles

Réviser les dérivées des fonctions de base :

- $\left(\sqrt{x}\right)' = \dfrac{1}{2\sqrt{x}}$ ;
- $\left(\dfrac{1}{x}\right)' = -\dfrac{1}{x^2}$ ;
- $\left(\ln(x)\right)' = \dfrac{1}{x}$ ;
- $\left(e^x\right)' = e^x$.

### Faire une erreur de calcul ou de simplification dans le résultat final

Simplifier avec soin, une étape à la fois.

Pour $f(x) = \sqrt{x^2 + 1}$, on obtient $\dfrac{2x}{2\sqrt{x^2 + 1}}$. Simplifier par $2$ donne $\dfrac{x}{\sqrt{x^2 + 1}}$, et non $\dfrac{1}{\sqrt{x^2 + 1}}$ (le $x$ du numérateur reste).
