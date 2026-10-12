# Le théorème des valeurs intermédiaires et de la bijection

Cette fiche apprend à démontrer qu'une équation $f(x) = k$ a **une solution unique**, puis à l'encadrer. Un grand exemple guidé suit toute la démarche, de la rédaction jusqu'à la calculatrice.

---

## 1. Monotonie et bijection

### Lien entre stricte monotonie et unicité

Si une fonction est **strictement monotone** sur un intervalle $I$, alors l'équation $f(x) = k$ a **au plus une solution** dans $I$.

### Comprendre pourquoi une fonction strictement monotone prend chaque valeur au plus une fois

Prenons $f$ strictement croissante sur $I$. Si $x_1 < x_2$, alors $f(x_1) < f(x_2)$, donc $f(x_1) \neq f(x_2)$.

Deux réels différents ont donc toujours des images différentes. Il est impossible que deux valeurs de $x$ aient la même image $k$ : la valeur $k$ est atteinte au plus une fois. Le raisonnement est le même pour une fonction strictement décroissante.

**Exemple :** la fonction $x \mapsto x^2$ n'est pas strictement monotone sur $[-2\ ;\ 2]$, et l'équation $x^2 = 4$ y a deux solutions, $-2$ et $2$. Sur $[0\ ;\ 2]$, elle est strictement croissante, et l'équation $x^2 = 4$ n'a qu'une solution : $2$.

### Lien avec l'existence et l'unicité d'une solution

La stricte monotonie donne l'**unicité** (au plus une solution). Elle ne garantit pas l'**existence** : il faut aussi que la fonction n'ait pas de « saut ».

**Exemple :** $g(x) = x$ si $x < 1$ et $g(x) = x + 2$ si $x \geq 1$. Sur $[0\ ;\ 2]$, $g$ est strictement croissante, mais l'équation $g(x) = 2$ n'a aucune solution : les valeurs prises sont dans $[0\ ;\ 1[$ puis dans $[3\ ;\ 4]$, et 2 est « sauté ».

C'est la **continuité** qui évite les sauts. Le théorème des valeurs intermédiaires dit : si $f$ est continue sur $[a\ ;\ b]$, alors $f$ prend toutes les valeurs comprises entre $f(a)$ et $f(b)$.

---

## 2. Théorème de la bijection

### Conditions du théorème

Pour appliquer le théorème, vérifier trois conditions :

1. $f$ est **continue** sur l'intervalle $[a\ ;\ b]$ ;
2. $f$ est **strictement monotone** sur $[a\ ;\ b]$ ;
3. le réel $k$ est **compris entre $f(a)$ et $f(b)$**.

### Continuité et stricte monotonie sur un intervalle

Chacune des deux conditions joue un rôle précis :

- la **continuité** garantit l'**existence** d'une solution (pas de saut) ;
- la **stricte monotonie** garantit l'**unicité** (chaque valeur au plus une fois).

Il faut les deux : si l'une manque, la conclusion peut tomber.

### Conclusion sur l'existence et l'unicité d'une solution

**Théorème.** Si $f$ est continue et strictement monotone sur $[a\ ;\ b]$, alors pour tout réel $k$ compris entre $f(a)$ et $f(b)$, l'équation $f(x) = k$ admet **une unique solution** dans $[a\ ;\ b]$.

On dit que $f$ réalise une **bijection** de $[a\ ;\ b]$ sur l'intervalle des valeurs prises : à chaque valeur $k$ correspond un seul $x$.

Le théorème s'étend aux intervalles ouverts ou infinis : on remplace alors $f(a)$ et $f(b)$ par les limites de $f$ aux bornes de l'intervalle.

---

## 3. Déterminer et encadrer une solution

**Énoncé.** Montrer que l'équation $x^3 = 1 - x$ admet une unique solution $\alpha$ dans $[0\ ;\ 1]$, puis en donner un encadrement d'amplitude $10^{-2}$.

### Transformer une équation pour utiliser le théorème

Le théorème s'applique à une équation de la forme $f(x) = k$. Il faut donc mettre l'équation sous cette forme :

$$x^3 = 1 - x \quad \Longleftrightarrow \quad x^3 + x = 1$$

Poser $f(x) = x^3 + x$ et $k = 1$. Résoudre l'équation de départ revient à résoudre $f(x) = 1$.

### Vérifier les conditions

- **Continuité :** $f$ est une fonction polynôme, donc continue sur $\mathbb{R}$, donc sur $[0\ ;\ 1]$.
- **Stricte monotonie :** $f'(x) = 3x^2 + 1$. Pour tout réel $x$, $f'(x) > 0$, donc $f$ est strictement croissante sur $[0\ ;\ 1]$.
- **Valeur comprise entre les images des bornes :** $f(0) = 0$ et $f(1) = 2$. Comme $0 \leq 1 \leq 2$, le réel $1$ est compris entre $f(0)$ et $f(1)$.

### Établir l'existence et l'unicité

Rédiger la conclusion en citant le théorème :

> La fonction $f$ est continue et strictement croissante sur $[0\ ;\ 1]$, avec $f(0) = 0$ et $f(1) = 2$. Or $1 \in [0\ ;\ 2]$. D'après le théorème de la bijection, l'équation $f(x) = 1$ admet une unique solution $\alpha$ dans $[0\ ;\ 1]$.

### Encadrer la solution

Calculer des valeurs de $f$ avec un pas de $0{,}1$ :

- $f(0{,}6) = 0{,}6^3 + 0{,}6 = 0{,}816$, donc $f(0{,}6) < 1$ ;
- $f(0{,}7) = 0{,}7^3 + 0{,}7 = 1{,}043$, donc $f(0{,}7) > 1$.

On a donc $f(0{,}6) < f(\alpha) < f(0{,}7)$. Comme $f$ est strictement croissante, l'ordre est conservé :

$$0{,}6 < \alpha < 0{,}7$$

Resserrer avec un pas de $0{,}01$ entre ces deux bornes :

- $f(0{,}68) \approx 0{,}9944 < 1$ ;
- $f(0{,}69) \approx 1{,}0185 > 1$.

Donc :

$$0{,}68 < \alpha < 0{,}69$$

C'est un encadrement d'amplitude $10^{-2}$, comme demandé.

### Affiner l'encadrement et obtenir une valeur approchée

Pour une précision plus grande, refaire la même démarche avec un pas de $0{,}001$ entre $0{,}68$ et $0{,}69$ :

- $f(0{,}682) \approx 0{,}9992 < 1$ ;
- $f(0{,}683) \approx 1{,}0016 > 1$.

Donc :

$$0{,}682 < \alpha < 0{,}683$$

Une valeur approchée de $\alpha$ à $10^{-3}$ près est $0{,}682$.

---

## 4. Utilisation de la calculatrice

### Déterminer une valeur approchée

Utiliser le **tableau de valeurs** de la calculatrice :

1. saisir la fonction $f$ ;
2. choisir un début et un pas (par exemple départ $0$, pas $0{,}1$) ;
3. repérer les deux lignes consécutives entre lesquelles $f(x)$ passe de « en dessous de $k$ » à « au dessus de $k$ » ;
4. recommencer avec un pas plus petit entre ces deux valeurs.

On peut aussi tracer la courbe de $f$ et la droite $y = k$, puis utiliser la fonction « intersection ».

### Vérifier un encadrement

Pour confirmer un encadrement $m < \alpha < M$, calculer $f(m)$ et $f(M)$ et vérifier que $k$ se trouve entre les deux.

**Exemple :** vérifier que $0{,}682 < \alpha < 0{,}683$. La calculatrice donne $f(0{,}682) \approx 0{,}9992$ et $f(0{,}683) \approx 1{,}0016$. Comme $0{,}9992 < 1 < 1{,}0016$ et que $f$ est strictement croissante, l'encadrement est correct.

### Respecter la précision demandée

Lire attentivement la formulation de l'énoncé :

- « **encadrer à $10^{-2}$ près** » : donner deux bornes dont l'écart vaut $0{,}01$, par exemple $0{,}68 < \alpha < 0{,}69$ ;
- « **donner la valeur arrondie au centième** » : il faut connaître assez de décimales pour arrondir sans se tromper.

Dans notre exemple, l'encadrement $0{,}68 < \alpha < 0{,}69$ ne suffit pas pour savoir si l'arrondi au centième est $0{,}68$ ou $0{,}69$. L'encadrement plus fin $0{,}682 < \alpha < 0{,}683$ montre que l'arrondi au centième est $0{,}68$.
