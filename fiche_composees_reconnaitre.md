# Reconnaître une fonction composée

## 1. Comprendre l'idée de composition

### Fonction intérieure / fonction extérieure

Composer deux fonctions, c'est les enchaîner : on applique d'abord une fonction $u$, puis une fonction $g$ au résultat.

$$x \;\xrightarrow{\ u\ }\; u(x) \;\xrightarrow{\ v\ }\; v\big(u(x)\big)$$

La fonction obtenue se note $v \circ u$ (« $v$ rond $u$ ») :

$$(v \circ u)(x) = v\big(u(x)\big)$$

- $u$ est la **fonction intérieure** : elle est appliquée en premier ;
- $v$ est la **fonction extérieure** : elle est appliquée en dernier.

**Exemple :** $f(x) = \sqrt{x^2 + 1}$. Pour calculer $f(2)$, on calcule d'abord $2^2 + 1 = 5$, puis on prend la racine carrée : $\sqrt{5}$.

- fonction intérieure : $u(x) = x^2 + 1$ ;
- fonction extérieure : $v(X) = \sqrt{X}$.

L'ordre compte : avec les mêmes fonctions dans l'autre sens, $(u \circ v)(x) = \left(\sqrt{x}\right)^2 + 1 = x + 1$ (pour $x \geq 0$). Ce n'est pas la même fonction.

### Reconnaître une fonction composée dans une expression

Pour repérer une composition, se demander : **« Quelle fonction est appliquée en dernier, et à quoi ? »**

Signe typique : une fonction usuelle (racine carrée, exponentielle, logarithme, puissance, inverse) « enveloppe » une expression qui contient $x$.

En pratique, imaginer le calcul de $f(x)$ pour une valeur précise de $x$ : la première étape donne $u(x)$, la dernière applique $g$.

### Quelques cas simples

| Expression $f(x)$ | Fonction intérieure $u(x)$ | Fonction extérieure $g(X)$ |
|---|---|---|
| $\sqrt{2x + 1}$ | $2x + 1$ | $\sqrt{X}$ |
| $e^{3x}$ | $3x$ | $e^{X}$ |
| $(x^2 + 1)^3$ | $x^2 + 1$ | $X^3$ |
| $\dfrac{1}{x + 4}$ | $x + 4$ | $\dfrac{1}{X}$ |
| $\ln\left(x^2 + 1\right)$ | $x^2 + 1$ | $\ln(X)$ |

---

## 2. Écrire une fonction sous forme composée

### Identifier les deux fonctions

Procéder en trois temps :

1. **Calculer $f$ pour une valeur** (par exemple $x = 2$) et noter l'ordre des opérations.
2. **La première étape** donne la fonction intérieure $u$.
3. **La dernière étape** donne la fonction extérieure $v$.

Pour la fonction extérieure, utiliser une autre lettre que $x$ (par exemple $X$) afin de ne pas confondre les deux fonctions.

### Décomposer une expression

Écrire $f = v \circ u$ puis **vérifier** que $v\big(u(x)\big)$ redonne bien $f(x)$.

**Exemple 1 :** $f(x) = e^{x^2 - 3x}$.

- $u(x) = x^2 - 3x$ ;
- $g(X) = e^{X}$ ;
- Vérification : $v\big(u(x)\big) = e^{x^2 - 3x} = f(x)$.

**Exemple 2 :** $f(x) = \dfrac{1}{x^2 + 1}$.

- $u(x) = x^2 + 1$ ;
- $v(X) = \dfrac{1}{X}$ ;
- Vérification : $g\big(u(x)\big) = \dfrac{1}{x^2 + 1} = f(x)$.

**Exemple 3 :** $f(x) = e^{\sqrt{x}}$.

- $u(x) = \sqrt{x}$ ;
- $v(X) = e^{X}$ ;
- Vérification : $g\big(u(x)\big) = e^{\sqrt{x}} = f(x)$.

---

## 3. Erreurs fréquentes

### Mal identifier les fonctions intérieure et extérieure, et donc mal écrire la composition

La fonction intérieure est celle qui est appliquée **en premier**.

Pour $f(x) = e^{3x}$ : $u(x) = 3x$ et $v(X) = e^{X}$. Inverser les rôles donnerait $3e^x$, qui n'est pas $e^{3x}$. Toujours vérifier avec $v\big(u(x)\big)$.

### Ne pas reconnaître une fonction composée présentée sous une forme moins évidente

Une composition peut se cacher.

- $f(x) = \dfrac{1}{2x + 3}$ est composée : $u(x) = 2x + 3$ suivie de $v(X) = \dfrac{1}{X}$ ;
- $f(x) = (x^2 + 1)^3$ est composée : $u(x) = x^2 + 1$ suivie de $v(X) = X^3$ ;
- $f(x) = e^{-x}$ est composée : $u(x) = -x$ suivie de $v(X) = e^{X}$.

### Croire que toute expression avec plusieurs opérations est une fonction composée

Une **composition** applique une fonction **au résultat** d'une autre. Une somme ou un produit de fonctions n'est pas une composition.

- $x^2 + 3x$ : somme de deux fonctions ;
- $x\,e^{x}$ : produit de deux fonctions ;
- $(x+1)(x-2)$ : produit de deux fonctions.

Ces expressions ont plusieurs opérations, mais aucune fonction n'y est appliquée au résultat d'une autre.
