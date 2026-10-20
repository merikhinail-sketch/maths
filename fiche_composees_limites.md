# Limites d'une fonction composée

Pour calculer la limite d'une fonction composée, on calcule d'abord la limite de la fonction intérieure, puis celle de la fonction extérieure. Cette fiche déroule la méthode sur un exemple, avec plusieurs variantes de difficulté croissante, et montre aussi les cas où elle ne permet pas de conclure.

**La propriété.** Soit $f = g \circ u$. Si :

- $\displaystyle \lim_{x \to a} u(x) = b$ ;
- $\displaystyle \lim_{X \to b} g(X) = L$ ;

alors :

$$\lim_{x \to a} g\big(u(x)\big) = L$$

Les nombres $a$, $b$ et $L$ peuvent être des réels, ou $+\infty$ ou $-\infty$.

---

## 1. Grand exemple guidé

### Limites usuelles à savoir

Ces limites servent d'outils à chaque étape de la méthode.

| Fonction | Limites usuelles |
|---|---|
| $x^n$ (avec $n \geq 1$ entier) | $+\infty$ en $+\infty$ |
| $\dfrac{1}{x}$ | $0$ en $+\infty$ et en $-\infty$ |
| $\sqrt{x}$ | $+\infty$ en $+\infty$ |
| $e^{x}$ | $+\infty$ en $+\infty$ ; $0$ en $-\infty$ |
| $\ln(x)$ | $+\infty$ en $+\infty$ ; $-\infty$ en $0^+$ |

### Exemple de base

**Énoncé.** Déterminer $\displaystyle \lim_{x \to +\infty} e^{-x}$.

**Étape 1 : identifier la fonction intérieure et la fonction extérieure.**

$f = g \circ u$ avec $u(x) = -x$ et $g(X) = e^{X}$.

**Étape 2 : déterminer la limite de la fonction intérieure.**

$$\lim_{x \to +\infty} u(x) = \lim_{x \to +\infty} (-x) = -\infty$$

Donc $b = -\infty$.

**Étape 3 : déterminer la limite de la fonction extérieure.**

$$\lim_{X \to -\infty} e^{X} = 0$$

Donc $L = 0$.

**Étape 4 : appliquer la propriété de composition.**

Comme $u(x) \to -\infty$ et $g(X) \to 0$ quand $X \to -\infty$, la propriété donne $g\big(u(x)\big) \to 0$.

**Étape 5 : conclure.**

$$\lim_{x \to +\infty} e^{-x} = 0$$

**Rédaction type :**

> On a $\displaystyle \lim_{x \to +\infty} (-x) = -\infty$ et $\displaystyle \lim_{X \to -\infty} e^{X} = 0$. Par composition, $\displaystyle \lim_{x \to +\infty} e^{-x} = 0$.

### Variante 1 : deux limites infinies

**Énoncé.** Déterminer $\displaystyle \lim_{x \to +\infty} \sqrt{x^2 + 1}$.

- Intérieure : $u(x) = x^2 + 1$, avec $\displaystyle \lim_{x \to +\infty} (x^2 + 1) = +\infty$.
- Extérieure : $g(X) = \sqrt{X}$, avec $\displaystyle \lim_{X \to +\infty} \sqrt{X} = +\infty$.
- Par composition : $\displaystyle \lim_{x \to +\infty} \sqrt{x^2 + 1} = +\infty$.

### Variante 2 : une fonction intérieure à étudier

**Énoncé.** Déterminer $\displaystyle \lim_{x \to +\infty} e^{x^2 - 3x}$.

- Intérieure : $u(x) = x^2 - 3x$. Factoriser pour calculer sa limite :

$$x^2 - 3x = x(x - 3)$$

Quand $x \to +\infty$, $x \to +\infty$ et $x - 3 \to +\infty$. Par produit, $u(x) \to +\infty$.
- Extérieure : $g(X) = e^{X}$, avec $\displaystyle \lim_{X \to +\infty} e^{X} = +\infty$.
- Par composition : $\displaystyle \lim_{x \to +\infty} e^{x^2 - 3x} = +\infty$.

### Variante 3 : une limite en un point, avec le signe à surveiller

**Énoncé.** Déterminer $\displaystyle \lim_{x \to 0} \ln\left(x^2\right)$.

- Intérieure : $u(x) = x^2$. Quand $x \to 0$, $x^2 \to 0$, et $x^2 > 0$ (pour $x \neq 0$). On écrit $u(x) \to 0^+$.
- Extérieure : $g(X) = \ln(X)$, avec $\displaystyle \lim_{X \to 0^+} \ln(X) = -\infty$.
- Par composition : $\displaystyle \lim_{x \to 0} \ln\left(x^2\right) = -\infty$.

Ici, **préciser $0^+$ est indispensable** : la limite usuelle de $\ln$ est donnée en $0^+$, et $\ln$ n'est pas définie pour des valeurs négatives.

### Variante 4 : quand la composition ne permet pas de conclure directement

**Énoncé.** Déterminer $\displaystyle \lim_{x \to 1} \frac{1}{x - 1}$.

- Intérieure : $u(x) = x - 1$, avec $u(x) \to 0$.
- Extérieure : $g(X) = \dfrac{1}{X}$. Mais $g$ **n'a pas de limite en $0$** : elle tend vers $+\infty$ à droite de $0$ et vers $-\infty$ à gauche.

La composition seule ne conclut pas : il faut regarder le **signe** de $u(x)$.

- Pour $x \to 1^+$ : $x - 1 \to 0^+$, donc $\dfrac{1}{x-1} \to +\infty$.
- Pour $x \to 1^-$ : $x - 1 \to 0^-$, donc $\dfrac{1}{x-1} \to -\infty$.

Les limites à droite et à gauche sont différentes : la fonction **n'a pas de limite en 1**.

### Variante 5 : quand la composition donne une forme indéterminée

**Énoncé.** Déterminer $\displaystyle \lim_{x \to +\infty} \left(\sqrt{x^2 + x} - x\right)$.

La composition donne la limite de $\sqrt{x^2 + x}$ : $u(x) = x^2 + x \to +\infty$ et $\sqrt{X} \to +\infty$, donc $\sqrt{x^2 + x} \to +\infty$.

Mais la fonction à étudier est $\sqrt{x^2 + x} - x$, de la forme $+\infty - \infty$ : c'est une **forme indéterminée**. La composition ne permet pas de conclure.

Lever l'indétermination avec la quantité conjuguée (pour $x > 0$) :

$$\sqrt{x^2 + x} - x = \frac{\left(x^2 + x\right) - x^2}{\sqrt{x^2 + x} + x} = \frac{x}{\sqrt{x^2 + x} + x}$$

Comme $\sqrt{x^2 + x} = x\sqrt{1 + \dfrac{1}{x}}$ pour $x > 0$, on simplifie par $x$ :

$$\sqrt{x^2 + x} - x = \frac{1}{\sqrt{1 + \dfrac{1}{x}} + 1}$$

Quand $x \to +\infty$, $\dfrac{1}{x} \to 0$, donc $\sqrt{1 + \dfrac{1}{x}} \to 1$ (par composition). Ainsi :

$$\lim_{x \to +\infty} \left(\sqrt{x^2 + x} - x\right) = \frac{1}{1 + 1} = \frac{1}{2}$$

---

## 2. Erreurs fréquentes

### Mal identifier les fonctions intérieure et extérieure

Se demander laquelle est appliquée en premier. Pour $e^{-x}$, l'intérieure est $-x$ et l'extérieure est $e^{X}$.

Prendre $e^{x}$ comme intérieure et $-X$ comme extérieure donnerait $-e^{x}$, qui n'est pas $e^{-x}$.

### Appliquer la composition sans vérifier les conditions nécessaires

Pour utiliser la propriété, il faut que **les deux limites existent** et que le **signe** soit bien précisé quand la fonction extérieure en dépend.

Écrire « $x - 1 \to 0$, donc $\dfrac{1}{x-1} \to \dfrac{1}{0} = +\infty$ » est faux : $\dfrac{1}{X}$ n'a pas de limite en $0$, et la fonction $\dfrac{1}{x-1}$ n'a pas de limite en $1$ (variante 4).

### Confondre la limite de l'intérieur avec celle de la composition

La limite de $u$ n'est pas la limite de $g \circ u$ : c'est celle de $g$, calculée **en** cette limite.

Pour $e^{-x}$ quand $x \to +\infty$, l'intérieur tend vers $-\infty$ mais la composition tend vers $0$, pas vers $-\infty$.

### Utiliser la composition alors qu'on obtient une forme indéterminée

La composition donne la limite d'**un bloc**. Si l'expression complète est ensuite une forme indéterminée ($+\infty - \infty$, $\dfrac{\infty}{\infty}$, $0 \times \infty$, $\dfrac{0}{0}$), il faut transformer l'expression.

Dans la variante 5, la composition donne $\sqrt{x^2 + x} \to +\infty$, mais cela ne suffit pas pour $\sqrt{x^2 + x} - x$. La limite vaut $\dfrac{1}{2}$, et non $+\infty$ ou $0$.
