# Limite d'une fonction

La limite d'une fonction décrit ce que deviennent ses valeurs $f(x)$ quand $x$ s'approche d'un point, ou devient très grand. Cette fiche donne le sens de cette notion.

---

## 1. Limite en un point

### Définition et signification : faire tendre $x$

Dire que $\displaystyle \lim_{x \to a} f(x) = L$ signifie que, lorsque $x$ prend des valeurs de plus en plus proches de $a$, les valeurs $f(x)$ deviennent aussi proches que l'on veut de $L$.

Faire tendre $x$ vers $a$, c'est donc laisser $x$ se rapprocher de $a$ sans se préoccuper de ce qui se passe **en** $a$.

**Exemple :** $f(x) = x^2$ quand $x$ tend vers $2$.

| $x$ | $1{,}9$ | $1{,}99$ | $1{,}999$ | $2{,}001$ | $2{,}01$ | $2{,}1$ |
|---|---|---|---|---|---|---|
| $f(x)$ | $3{,}61$ | $3{,}9601$ | $3{,}996001$ | $4{,}004001$ | $4{,}0401$ | $4{,}41$ |

Les valeurs de $f(x)$ se rapprochent de $4$, des deux côtés. Donc $\displaystyle \lim_{x \to 2} x^2 = 4$.

La limite peut aussi être **infinie** : $\displaystyle \lim_{x \to 0} \frac{1}{x^2} = +\infty$ signifie que $\dfrac{1}{x^2}$ devient aussi grand que l'on veut quand $x$ est proche de $0$.

### Comment interpréter une limite

Sur la courbe de $f$ :

- **limite finie $L$ en $a$** : quand on se rapproche de l'abscisse $a$, la courbe se rapproche de la hauteur $L$ ;
- **limite infinie en $a$** : quand on se rapproche de l'abscisse $a$, la courbe monte (ou descend) indéfiniment ; on retrouvera cette situation avec les asymptotes verticales.

### Différence entre $f(a)$ et $\displaystyle \lim_{x \to a} f(x)$

$f(a)$ est la valeur de la fonction **au point** $a$. La limite décrit le comportement de la fonction **autour de** $a$. Ce sont deux choses différentes, qui peuvent être égales (fonction continue) ou non.

**Exemple : la fonction n'existe pas en $a$.** $f(x) = \dfrac{x^2 - 1}{x - 1}$ en $a = 1$.

$f(1)$ n'existe pas (division par $0$). Pourtant, pour $x \neq 1$ :

Si on remplace x par 1 on obtient $"\dfrac{0}{0}"$, c'est une forme indéterminée. On ne peut pas trouver la limite juste en remplaçant x par 1.
On doit donc trouver une factorisation pour lever la forme indéterminée.

On remarque au numérateur la forme $a^2 - b^2$ qui s'écrit sous la forme $(a+b)(a-b)$

Donc : 

$x^2 -1 = (x-1)(x+1)$

Donc :
$$f(x) = \frac{(x-1)(x+1)}{x-1} = x + 1 \quad \Longrightarrow \quad \lim_{x \to 1} f(x) = 2$$





Quand $\displaystyle \lim_{x \to a} f(x) = f(a)$, on retrouve la **continuité** de $f$ en $a$.

---

## 2. Limites à gauche et à droite

### Limite à droite

La **limite à droite** de $f$ en $a$ s'intéresse aux valeurs de $x$ **juste au-dessus de $a$** ($x > a$). Elle se note :

$$\lim_{x \to a^+} f(x) \qquad \text{ou} \qquad \lim_{\substack{x \to a \\ x > a}} f(x)$$

### Limite à gauche

La **limite à gauche** de $f$ en $a$ s'intéresse aux valeurs de $x$ **juste au-dessous de $a$** ($x < a$). Elle se note :

$$\lim_{x \to a^-} f(x) \qquad \text{ou} \qquad \lim_{\substack{x \to a \\ x < a}} f(x)$$

### Lien avec la limite en $a$

Si $f$ est définie autour de $a$, la limite de $f$ en $a$ existe **si et seulement si** les limites à gauche et à droite existent et sont **égales**.

**Exemple (les deux côtés coïncident) :** $f(x) = x^2 + 1$ si $x < 2$, et 

$f(x) = 3x - 1$ si $x \geq 2$.

- à gauche : $\displaystyle \lim_{x \to 2^-} f(x) = 2^2 + 1 = 5$ ;
- à droite : $\displaystyle \lim_{x \to 2^+} f(x) = 3 \times 2 - 1 = 5$.

Les deux limites sont égales : $\displaystyle \lim_{x \to 2} f(x) = 5$.

**Exemple (les deux côtés diffèrent) :** $f(x) = \dfrac{1}{x}$ en $a = 0$.

- à droite : pour $x > 0$ proche de $0$, $\dfrac{1}{x}$ est très grand et positif, donc $\displaystyle \lim_{x \to 0^+} \frac{1}{x} = +\infty$ ;
- à gauche : pour $x < 0$ proche de $0$, $\dfrac{1}{x}$ est très grand et négatif, donc $\displaystyle \lim_{x \to 0^-} \frac{1}{x} = -\infty$.

Les limites à gauche et à droite sont différentes : $\dfrac{1}{x}$ **n'a pas de limite en $0$**.

---

## 3. Limites à l'infini

### En $+\infty$ et en $-\infty$

Étudier la limite en $+\infty$, c'est regarder ce que devient $f(x)$ quand $x$ devient de plus en plus grand. Étudier la limite en $-\infty$, c'est regarder ce que devient $f(x)$ quand $x$ devient de plus en plus négatif.

- **Limite finie** : $\displaystyle \lim_{x \to +\infty} f(x) = L$ signifie que $f(x)$ se rapproche de $L$ quand $x$ devient très grand.
- **Limite infinie** : $\displaystyle \lim_{x \to +\infty} f(x) = +\infty$ signifie que $f(x)$ devient aussi grand que l'on veut.

**Exemples :**

- $\displaystyle \lim_{x \to +\infty} \frac{1}{x} = 0$ et $\displaystyle \lim_{x \to -\infty} \frac{1}{x} = 0$ ;

- $\displaystyle \lim_{x \to +\infty} x^2 = +\infty$ et $\displaystyle \lim_{x \to -\infty} x^2 = +\infty$ ;

- $\displaystyle \lim_{x \to -\infty} x^3 = -\infty$ ;
- $\displaystyle \lim_{x \to +\infty} e^x = +\infty$ mais $\displaystyle \lim_{x \to -\infty} e^x = 0$ : le comportement n'est pas toujours le même aux deux bouts.

Certaines fonctions n'ont **pas de limite** en $+\infty$ : par exemple $\cos(x)$ oscille indéfiniment entre $-1$ et $1$ sans se stabiliser.

---

## 4. Erreurs fréquentes

### Confondre $f(a)$ et $\displaystyle \lim_{x \to a} f(x)$

La limite décrit ce qui se passe **autour** de $a$, pas la valeur **en** $a$.

Pour $g(x) = x^2$ si $x \neq 2$ et $g(2) = 7$, on a $g(2) = 7$ mais $\displaystyle \lim_{x \to 2} g(x) = 4$. Pour $f(x) = \dfrac{x^2-1}{x-1}$, $f(1)$ n'existe pas mais la limite en $1$ vaut $2$.

### Confondre limite à droite et limite à gauche

Ne pas oublier de préciser de quel côté on se rapproche : $x \to a^+$ (valeurs plus grandes que $a$) ou $x \to a^-$ (valeurs plus petites que $a$).

$\displaystyle \lim_{x \to 0^+} \frac{1}{x} = +\infty$ alors que $\displaystyle \lim_{x \to 0^-} \frac{1}{x} = -\infty$. Écrire simplement $\displaystyle \lim_{x \to 0} \frac{1}{x} = +\infty$ est faux.
