# Asymptotes

Une asymptote est une droite dont la courbe d'une fonction se rapproche de plus en plus. Cette fiche montre comment les repérer et les déterminer à partir des limites.

---

## 1. Asymptote verticale et horizontale

### Asymptote verticale

**Comprendre.** Une asymptote verticale est une droite verticale dont la courbe se rapproche en montant ou en descendant indéfiniment.

**Lien avec une limite.** Si, quand $x$ se rapproche d'une valeur $a$, $f(x)$ tend vers $+\infty$ ou $-\infty$ (à gauche, à droite, ou des deux côtés), alors la droite d'équation $x = a$ est une **asymptote verticale**.

$$\lim_{x \to a^+} f(x) = \pm\infty \quad \text{ou} \quad \lim_{x \to a^-} f(x) = \pm\infty$$

**Équation.** $x = a$.

**Exemple :** $f(x) = \dfrac{1}{x - 2}$.

- à droite : $\displaystyle \lim_{x \to 2^+} f(x) = +\infty$ ;
- à gauche : $\displaystyle \lim_{x \to 2^-} f(x) = -\infty$.

La droite d'équation $x = 2$ une est asymptote verticale à la courbe.

### Asymptote horizontale

**Comprendre.** Une asymptote horizontale est une droite horizontale dont la courbe se rapproche quand $x$ devient très grand (ou très négatif).

**Lien avec une limite.** Si $\displaystyle \lim_{x \to +\infty} f(x) = L$ (réel), alors la droite d'équation $y = L$ est une **asymptote horizontale** en $+\infty$. Même chose en $-\infty$.

**Équation.** $y = L$.

**Exemple :** $f(x) = \dfrac{1}{x - 2}$. On a $\displaystyle \lim_{x \to +\infty} f(x) = 0$ et $\displaystyle \lim_{x \to -\infty} f(x) = 0$. La droite $y = 0$ (l'axe des abscisses) est asymptote horizontale en $+\infty$ et en $-\infty$.

**Exemple avec les deux types :** $f(x) = \dfrac{2x + 1}{x - 2}$.

- en $\pm\infty$ : $f(x) = \dfrac{x\left(2 + \dfrac{1}{x}\right)}{x\left(1 - \dfrac{2}{x}\right)} \to 2$, donc $y = 2$ est asymptote horizontale ;
- en $2^+$ : le numérateur tend vers $5 > 0$ et le dénominateur vers $0^+$, donc $f(x) \to +\infty$ ; la droite $x = 2$ est asymptote verticale.

---

## 2. Asymptote oblique

### Reconnaître une asymptote oblique

Une asymptote oblique est une droite **ni verticale ni horizontale**, d'équation $y = ax + b$ avec $a \neq 0$, dont la courbe se rapproche quand $x \to +\infty$ (ou $-\infty$).

### Le lien avec une expression du type $f(x) - (ax + b) \to 0$

La droite $y = ax + b$ est asymptote oblique à la courbe de $f$ en $+\infty$ si :

$$\lim_{x \to +\infty} \left[f(x) - (ax + b)\right] = 0$$

Autrement dit, l'écart vertical entre la courbe et la droite devient aussi petit que l'on veut.

### Déterminer l'équation $y = ax + b$

**Cas 1 : la fonction est déjà écrite sous la forme $ax + b + g(x)$ avec $g(x) \to 0$.** L'asymptote se lit directement : $y = ax + b$.

*Exemple :* $f(x) = \dfrac{x^2 + x + 1}{x} = x + 1 + \dfrac{1}{x}$. Comme $\dfrac{1}{x} \to 0$, la droite $y = x + 1$ est asymptote oblique en $+\infty$ et en $-\infty$.

**Cas 2 : sinon, trouver $a$ puis $b$ avec des limites.**

### Le lien avec les limites permettant de trouver $a$ et $b$

1. Calculer le coefficient directeur : $\displaystyle a = \lim_{x \to +\infty} \frac{f(x)}{x}$. Il doit être un réel non nul.
2. Calculer l'ordonnée à l'origine : $\displaystyle b = \lim_{x \to +\infty} \left[f(x) - ax\right]$. Elle doit être un réel.

*Exemple :* $f(x) = \sqrt{x^2 + x}$ en $+\infty$.

- $\dfrac{f(x)}{x} = \sqrt{\dfrac{x^2 + x}{x^2}} = \sqrt{1 + \dfrac{1}{x}}$ (pour $x > 0$), qui tend vers $1$. Donc $a = 1$.
- $f(x) - x = \sqrt{x^2 + x} - x$. C'est une forme $+\infty - \infty$, que l'on lève avec la quantité conjuguée :

$$\sqrt{x^2 + x} - x = \frac{x}{\sqrt{x^2 + x} + x} = \frac{1}{\sqrt{1 + \dfrac{1}{x}} + 1} \longrightarrow \frac{1}{2}$$

Donc $b = \dfrac{1}{2}$.

La droite $y = x + \dfrac{1}{2}$ est asymptote oblique en $+\infty$. (En $-\infty$, le même type de calcul donne une autre droite, $y = -x - \dfrac{1}{2}$.)

---

## 3. Déterminer une asymptote à partir d'une fonction

Voici la démarche complète sur un exemple.

**Énoncé.** Étudier les asymptotes de la courbe de $f(x) = \dfrac{x^2 + x + 1}{x - 1}$.

### Partir de la fonction et analyser ses limites

**Domaine :** le dénominateur s'annule en $1$. La fonction est définie sur $\mathbb{R} \setminus \{1\}$.

**Limites aux bornes du domaine :**

- en $1^+$ : le numérateur tend vers $3 > 0$ et le dénominateur vers $0^+$, donc $\displaystyle \lim_{x \to 1^+} f(x) = +\infty$ ;
- en $1^-$ : le numérateur tend vers $3 > 0$ et le dénominateur vers $0^-$, donc $\displaystyle \lim_{x \to 1^-} f(x) = -\infty$ ;
- en $\pm\infty$ : $f(x) = \dfrac{x^2\left(1 + \dfrac{1}{x} + \dfrac{1}{x^2}\right)}{x\left(1 - \dfrac{1}{x}\right)} = x \times \dfrac{1 + \dfrac{1}{x} + \dfrac{1}{x^2}}{1 - \dfrac{1}{x}}$, qui tend vers $+\infty$ en $+\infty$ et $-\infty$ en $-\infty$. Il n'y a pas d'asymptote horizontale.

### Identifier quelle asymptote correspond au comportement observé

- La limite infinie en $1$ donne une **asymptote verticale**.
- Comme $f(x) \to \pm\infty$ en $\pm\infty$, une asymptote oblique est possible. Pour la chercher, effectuer la division de $x^2 + x + 1$ par $x - 1$ :

$$x^2 + x + 1 = (x - 1)(x + 2) + 3 \quad \Longrightarrow \quad f(x) = x + 2 + \frac{3}{x - 1}$$

Comme $\dfrac{3}{x - 1} \to 0$ en $+\infty$ et en $-\infty$, on a $f(x) - (x + 2) \to 0$ : il y a une **asymptote oblique**.

### Déterminer son équation

- asymptote verticale : $x = 1$ ;
- asymptote oblique (en $+\infty$ et en $-\infty$) : $y = x + 2$.

### Éventuellement interpréter graphiquement le résultat

La courbe se rapproche de la droite verticale $x = 1$ en montant (à droite) et en descendant (à gauche), et se rapproche de la droite $y = x + 2$ aux deux extrémités.

Pour savoir de quel côté de la droite oblique se trouve la courbe, étudier le signe de $f(x) - (x + 2) = \dfrac{3}{x - 1}$ :

- pour $x > 1$, cette différence est positive : la courbe est **au-dessus** de la droite ;
- pour $x < 1$, elle est négative : la courbe est **au-dessous**.

---

## 4. Erreurs fréquentes

### Confondre asymptote verticale et horizontale

Une asymptote **verticale** a pour équation $x = a$ et vient d'une limite **en un point $a$** égale à $\pm\infty$. Une asymptote **horizontale** a pour équation $y = L$ et vient d'une limite **en $\pm\infty$** égale à un réel $L$.

Pour $f(x) = \dfrac{1}{x - 2}$ : $x = 2$ est asymptote verticale, $y = 0$ est asymptote horizontale.

### Déduire une asymptote verticale d'une simple valeur interdite

Une valeur interdite n'implique pas une asymptote : il faut **calculer la limite**.

Pour $f(x) = \dfrac{x^2 - 1}{x - 1}$, la valeur $1$ est interdite. Mais $f(x) = x + 1$ pour $x \neq 1$, donc $\displaystyle \lim_{x \to 1} f(x) = 2$, qui est un réel : il n'y a **pas** d'asymptote verticale, seulement un « trou » dans la courbe.

### Oublier qu'une fonction peut avoir deux comportements différents en $+\infty$ et en $-\infty$

Étudier chaque extrémité séparément.

Pour $f(x) = e^x$ : en $-\infty$, $f(x) \to 0$ donc $y = 0$ est asymptote horizontale ; en $+\infty$, $f(x) \to +\infty$, et il n'y a pas d'asymptote.

### Confondre « la courbe se rapproche de la droite » avec « elle ne peut jamais la couper »

Une asymptote décrit le comportement **à l'infini** (ou près d'un point), pas l'impossibilité de croiser la droite.

Pour $f(x) = 1 + \dfrac{\sin(x)}{x}$, la droite $y = 1$ est asymptote horizontale en $+\infty$, car $\dfrac{\sin(x)}{x} \to 0$. Pourtant la courbe coupe cette droite chaque fois que $\sin(x) = 0$, c'est-à-dire en $x = \pi$, $2\pi$, $3\pi$, etc.
