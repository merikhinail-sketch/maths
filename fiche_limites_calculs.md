# Calculs de limites

Cette fiche donne les outils pour calculer une limite : les opérations sur les limites, les limites usuelles, les méthodes pour lever une forme indéterminée, et le théorème des gendarmes.

---

## 1. Opérations sur les limites

Dans les tableaux suivants, $L$ et $L'$ sont des réels. Les limites peuvent être prises en $a$, en $+\infty$ ou en $-\infty$.

### Somme et différence

| Limite de $f$ | Limite de $g$ | Limite de $f + g$ |
|---|---|---|
| $L$ | $L'$ | $L + L'$ |
| $L$ | $+\infty$ | $+\infty$ |
| $L$ | $-\infty$ | $-\infty$ |
| $+\infty$ | $+\infty$ | $+\infty$ |
| $-\infty$ | $-\infty$ | $-\infty$ |
| $+\infty$ | $-\infty$ | **forme indéterminée** |

Pour une différence $f - g$, écrire $f + (-g)$.

### Produit

| Limite de $f$ | Limite de $g$ | Limite de $f \times g$ |
|---|---|---|
| $L$ | $L'$ | $L \times L'$ |
| $L > 0$ | $+\infty$ | $+\infty$ |
| $L < 0$ | $+\infty$ | $-\infty$ |
| $+\infty$ | $+\infty$ | $+\infty$ |
| $+\infty$ | $-\infty$ | $-\infty$ |
| $0$ | $\pm\infty$ | **forme indéterminée** |

### Quotient

| Limite de $f$ | Limite de $g$ | Limite de $\dfrac{f}{g}$ |
|---|---|---|
| $L$ | $L' \neq 0$ | $\dfrac{L}{L'}$ |
| $L$ | $\pm\infty$ | $0$ |
| $\pm\infty$ | $L' > 0$ | $\pm\infty$ (même signe) |
| $L \neq 0$ | $0^+$ | $+\infty$ si $L > 0$, $-\infty$ si $L < 0$ |
| $L \neq 0$ | $0^-$ | $-\infty$ si $L > 0$, $+\infty$ si $L < 0$ |
| $\pm\infty$ | $\pm\infty$ | **forme indéterminée** |
| $0$ | $0$ | **forme indéterminée** |

Pour un quotient dont le dénominateur tend vers $0$, **préciser le signe** du dénominateur ($0^+$ ou $0^-$).

### Puissances

Pour un entier $n \geq 1$ :

- si $\displaystyle \lim f = L$, alors $\displaystyle \lim f^n = L^n$ ;
- si $f \to +\infty$, alors $f^n \to +\infty$ ;
- si $f \to -\infty$, alors $f^n \to +\infty$ quand $n$ est pair et $f^n \to -\infty$ quand $n$ est impair.

### Rédaction

Citer l'opération utilisée, puis donner la limite.

**Exemple :** déterminer $\displaystyle \lim_{x \to +\infty} \left(x^2 + \frac{1}{x}\right)$.

> On a $\displaystyle \lim_{x \to +\infty} x^2 = +\infty$ et $\displaystyle \lim_{x \to +\infty} \frac{1}{x} = 0$. Par somme, $\displaystyle \lim_{x \to +\infty} \left(x^2 + \frac{1}{x}\right) = +\infty$.

---

## 2. Limites usuelles

### Puissances de $x$

Pour un entier $n \geq 1$ :

- $\displaystyle \lim_{x \to +\infty} x^n = +\infty$ ;
- $\displaystyle \lim_{x \to -\infty} x^n = +\infty$ si $n$ est pair, $-\infty$ si $n$ est impair ;
- $\displaystyle \lim_{x \to +\infty} \frac{1}{x^n} = 0$ et $\displaystyle \lim_{x \to -\infty} \frac{1}{x^n} = 0$.

### $\dfrac{1}{x}$, racine de $x$, exponentielles, logarithmes

| Fonction | En $+\infty$ | En $-\infty$ | En $0$ |
|---|---|---|---|
| $\dfrac{1}{x}$ | $0$ | $0$ | $+\infty$ en $0^+$ ; $-\infty$ en $0^-$ |
| $\dfrac{1}{x^2}$ | $0$ | $0$ | $+\infty$ en $0^+$ et en $0^-$ |
| $\sqrt{x}$ | $+\infty$ | non définie | $0$ en $0^+$ |
| $e^{x}$ | $+\infty$ | $0$ | $1$ |
| $\ln(x)$ | $+\infty$ | non définie | $-\infty$ en $0^+$ |

### Croissances comparées

Quand nous rencontrons des formes indéterminées mais qu'on ne peut pas factoriser l'expression on doit faire la limite par **croissance comparée**.

Ces quatre limites, à connaître, comparent la « vitesse » de l'exponentielle, de $\ln$ et de $x$ :

$$\lim_{x \to +\infty} \frac{e^x}{x} = +\infty \qquad \lim_{x \to +\infty} \frac{\ln(x)}{x} = 0 \qquad \lim_{x \to 0^+} x\ln(x) = 0 \qquad \lim_{x \to -\infty} x\,e^{x} = 0$$

L'idée : l'exponentielle augmente plus vite vers l'infini que $x$, et $x$ augmente plus vite vers l'infini que $\ln(x)$.

---

## 3. Formes indéterminées

Les quatre formes indéterminées sont :

$$\frac{0}{0} \qquad \frac{\pm\infty}{\pm\infty} \qquad 0 \times \infty \qquad +\infty - \infty$$

Il faut les transformer pour obtenir une forme où l'on peut conclure.

### Méthodes pour les faire disparaître

**Méthode 1 : factoriser par le terme dominant (polynômes et fractions rationnelles en $\pm\infty$).**

Le terme dominant est celui de plus haut degré. Le factoriser fait apparaître des termes dont la limite est connue.

*Exemple :* $\displaystyle \lim_{x \to +\infty} \left(x^2 - 3x\right)$ est de la forme $+\infty - \infty$.

$$x^2 - 3x = x^2\left(1 - \frac{3}{x}\right)$$

Or $x^2 \to +\infty$ et $1 - \dfrac{3}{x} \to 1$. Par produit, la limite est $+\infty$.

*Exemple :* $\displaystyle \lim_{x \to +\infty} \frac{2x^2 + x}{x^2 - 1}$ est de la forme $\dfrac{+\infty}{+\infty}$.

$$\frac{2x^2 + x}{x^2 - 1} = \frac{x^2\left(2 + \dfrac{1}{x}\right)}{x^2\left(1 - \dfrac{1}{x^2}\right)} = \frac{2 + \dfrac{1}{x}}{1 - \dfrac{1}{x^2}} \longrightarrow \frac{2}{1} = 2$$

**Méthode 2 : factoriser et simplifier (forme $\dfrac{0}{0}$ en un point).**

*Exemple :* $\displaystyle \lim_{x \to 1} \frac{x^2 - 1}{x - 1}$ est de la forme $\dfrac{0}{0}$.

$$\frac{x^2 - 1}{x - 1} = \frac{(x-1)(x+1)}{x-1} = x + 1 \longrightarrow 2$$

**Méthode 3 : multiplier par la quantité conjuguée (différence de racines).**

*Exemple :* $\displaystyle \lim_{x \to +\infty} \left(\sqrt{x+1} - \sqrt{x}\right)$ est de la forme $+\infty - \infty$.

$$\sqrt{x+1} - \sqrt{x} = \frac{(x+1) - x}{\sqrt{x+1} + \sqrt{x}} = \frac{1}{\sqrt{x+1} + \sqrt{x}} \longrightarrow 0$$

**Méthode 4 : factoriser par l'exponentielle ou utiliser les croissances comparées.**

*Exemple :* $\displaystyle \lim_{x \to +\infty} \left(e^x - x\right)$ est de la forme $+\infty - \infty$.

$$e^x - x = e^x\left(1 - \frac{x}{e^x}\right)$$

Par croissances comparées, $\dfrac{e^x}{x} \to +\infty$, donc $\dfrac{x}{e^x} \to 0$ et $1 - \dfrac{x}{e^x} \to 1$. Avec $e^x \to +\infty$, la limite est $+\infty$.

---

## 4. Théorème des gendarmes

### Principe de l'encadrement

**Théorème.** Soient $f$, $g$ et $h$ trois fonctions telles que, pour $x$ assez proche de $a$ (ou assez grand), $g(x) \leq f(x) \leq h(x)$. Si $g$ et $h$ ont **la même limite $L$**, alors $f$ a aussi pour limite $L$.

L'idée : $f$ est coincée entre deux fonctions qui se rejoignent en $L$. Elle n'a pas d'autre choix que d'aller en $L$.

### Reconnaître une situation où il peut être utilisé

Le théorème est utile quand $f$ contient un terme **borné** qui n'a pas de limite, comme $\sin(x)$ ou $\cos(x)$, souvent divisé par une expression qui tend vers $\pm\infty$.

Il sert à trouver une limite **finie**. Pour une limite infinie, on utilise plutôt une comparaison : par exemple, $x + \sin(x) \geq x - 1$ et $x - 1 \to +\infty$, donc $x + \sin(x) \to +\infty$.

### Construire l'encadrement

Partir de l'inégalité connue ($-1 \leq \sin(x) \leq 1$ ou $-1 \leq \cos(x) \leq 1$), puis multiplier ou diviser par une expression **strictement positive** (pour ne pas changer le sens des inégalités).

### Déterminer la limite grâce aux deux bornes

Calculer les limites des deux bornes. Si elles sont égales, conclure avec le théorème.

**Exemple :** déterminer $\displaystyle \lim_{x \to +\infty} \frac{\sin(x)}{x}$.

Pour $x > 0$, on a $-1 \leq \sin(x) \leq 1$. En divisant par $x > 0$ :

$$-\frac{1}{x} \leq \frac{\sin(x)}{x} \leq \frac{1}{x}$$

Or $-\dfrac{1}{x} \to 0$ et $\dfrac{1}{x} \to 0$. D'après le théorème des gendarmes, $\displaystyle \lim_{x \to +\infty} \frac{\sin(x)}{x} = 0$.

**Autre exemple :** déterminer $\displaystyle \lim_{x \to +\infty} \frac{\cos(x)}{x^2 + 1}$.

Pour tout réel $x$, $-1 \leq \cos(x) \leq 1$. Comme $x^2 + 1 > 0$ :

$$-\frac{1}{x^2 + 1} \leq \frac{\cos(x)}{x^2 + 1} \leq \frac{1}{x^2 + 1}$$

Les deux bornes tendent vers $0$ en $+\infty$. Donc la limite est $0$.

---

## 5. Erreurs fréquentes

### Ne pas lever la forme indéterminée

Une forme indéterminée n'a pas de valeur automatique. Écrire « $+\infty - \infty = 0$ » est faux : selon les fonctions, le résultat peut être $0$, un réel, $+\infty$ ou $-\infty$.

Pour $x^2 - 3x$ en $+\infty$, la forme est $+\infty - \infty$, et la limite est $+\infty$ (méthode 1).

### Faire des opérations illégales

Ne pas manipuler $\infty$ comme un nombre ordinaire.

- $\dfrac{\infty}{\infty} = 1$ est faux ;
- $0 \times \infty = 0$ est faux ;
- $\dfrac{1}{0} = +\infty$ est faux sans préciser le signe du dénominateur ($0^+$ ou $0^-$).

### Mauvaise factorisation

Vérifier qu'en redéveloppant on retrouve l'expression de départ.

$x^2 - 3x = x^2\left(1 - \dfrac{3}{x}\right)$ : en redéveloppant, $x^2 \times 1 - x^2 \times \dfrac{3}{x} = x^2 - 3x$. Mais écrire $x^2(1 - 3x)$ est faux : cela redonne $x^2 - 3x^3$.
