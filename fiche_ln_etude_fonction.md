# Étude de fonction logarithme

Cette fiche déroule une étude de fonction complète avec un logarithme : domaine, dérivée, signe, limites, tableau de variations, puis nombre de solutions d'une équation. Suivre chaque étape en refaisant les calculs.

---

## 1. Grand exemple guidé

**Énoncé.** Soit $f$ la fonction définie sur $]0\ ;\ +\infty[$ par :

$$f(x) = \left(\ln(x)\right)^2 - 1$$

1. Calculer la dérivée de $f$ et étudier son signe.
2. Dresser le tableau de variations de $f$, en calculant les limites aux bornes.
3. Déterminer le nombre de solutions de l'équation $f(x) = 0$, puis les donner.

### Étape 1 : vérifier le domaine de définition

La fonction $\ln$ n'est définie que pour $x > 0$. L'énoncé donne bien $]0\ ;\ +\infty[$ comme domaine. L'étude se fait sur cet intervalle, et seulement sur celui-là.

### Étape 2 : calculer la dérivée

Rappels : $\ln'(x) = \dfrac{1}{x}$ et $\left(u^2\right)' = 2u\,u'$. Ici $u = \ln(x)$, donc $u' = \dfrac{1}{x}$.

$$f'(x) = 2\ln(x) \times \frac{1}{x} = \frac{2\ln(x)}{x}$$

### Étape 3 : étudier le signe de la dérivée

Pour $x > 0$, le dénominateur $x$ est strictement positif. Le signe de $f'(x)$ est donc celui de $\ln(x)$ :

- $\ln(x) < 0$ pour $0 < x < 1$, donc $f'(x) < 0$ ;
- $\ln(1) = 0$, donc $f'(1) = 0$ ;
- $\ln(x) > 0$ pour $x > 1$, donc $f'(x) > 0$.

(On utilise ici que $\ln$ est strictement croissante avec $\ln(1) = 0$.)

### Étape 4 : calculer les limites

**En $0^+$ :** $\ln(x) \to -\infty$, donc $\left(\ln(x)\right)^2 \to +\infty$.

$$\lim_{x \to 0^+} f(x) = +\infty$$

**En $+\infty$ :** $\ln(x) \to +\infty$, donc $\left(\ln(x)\right)^2 \to +\infty$.

$$\lim_{x \to +\infty} f(x) = +\infty$$

### Étape 5 : dresser le tableau de variations

Calculer la valeur au point où la dérivée s'annule : $f(1) = \left(\ln(1)\right)^2 - 1 = 0 - 1 = -1$.

| $x$ | $0$ | | $1$ | | $+\infty$ |
|---|---|---|---|---|---|
| Signe de $f'(x)$ | | $-$ | $0$ | $+$ | |
| Variations de $f$ | $+\infty$ | $\searrow$ | $-1$ | $\nearrow$ | $+\infty$ |

**Lecture :** $f$ est strictement décroissante sur $]0\ ;\ 1]$ et strictement croissante sur $[1\ ;\ +\infty[$. Elle admet un **minimum égal à $-1$, atteint en $x = 1$**.

### Étape 6 : nombre de solutions de $f(x) = 0$

Étudier chaque intervalle de monotonie séparément.

**Sur $]0\ ;\ 1]$ :** $f$ est continue et strictement décroissante. Elle prend ses valeurs dans $[-1\ ;\ +\infty[$. Comme $0 \in [-1\ ;\ +\infty[$, le théorème de la bijection donne **une unique solution** sur cet intervalle.

**Sur $[1\ ;\ +\infty[$ :** $f$ est continue et strictement croissante. Elle prend ses valeurs dans $[-1\ ;\ +\infty[$. Comme $0 \in [-1\ ;\ +\infty[$, il y a de nouveau **une unique solution**.

Ces deux solutions sont distinctes (l'une est dans $]0\ ;\ 1[$, l'autre dans $]1\ ;\ +\infty[$). L'équation $f(x) = 0$ admet **exactement deux solutions**.

**Les trouver :**

$$f(x) = 0 \iff \left(\ln(x)\right)^2 = 1 \iff \ln(x) = 1 \ \text{ ou } \ \ln(x) = -1 \iff x = e \ \text{ ou } \ x = \frac{1}{e}$$

On retrouve deux solutions, $x = \dfrac{1}{e}$ (dans $]0\ ;\ 1[$) et $x = e$ (dans $]1\ ;\ +\infty[$), ce qui confirme l'étude des variations.

---

## 2. Erreurs fréquentes

### Oublier le domaine de définition de la fonction et donc étudier la fonction sur un mauvais intervalle

Toujours commencer par le domaine. Ici, $\ln(x)$ n'existe que pour $x > 0$.

Étudier $f$ sur $\mathbb{R}$, ou calculer $f(-1)$, n'a aucun sens : $\ln(-1)$ n'existe pas.

### Se tromper dans le calcul de la dérivée et donc en déduire de mauvaises variations

Pour dériver $\left(\ln(x)\right)^2$, utiliser $\left(u^2\right)' = 2u\,u'$ avec $u = \ln(x)$ : on obtient $\dfrac{2\ln(x)}{x}$.

Oublier le facteur $\dfrac{1}{x}$ (qui est la dérivée de $\ln(x)$) donnerait $2\ln(x)$, ce qui est faux.

### Confondre le signe de $f'(x)$ avec les variations de $f$

Le signe de $f'$ indique **comment $f$ varie**, pas si $f$ est positive ou négative.

$f'(x) < 0$ sur $]0\ ;\ 1[$ signifie que $f$ **décroît** sur cet intervalle. Cela ne dit pas que $f(x)$ est négatif.

### Mal calculer les limites impliquant $\ln(x)$

Penser au comportement de $\ln(x)$ : $\ln(x) \to -\infty$ en $0^+$ et $\ln(x) \to +\infty$ en $+\infty$.

Ne pas oublier ensuite l'effet de l'opération : $\left(\ln(x)\right)^2 \to +\infty$ en $0^+$, car le carré d'un nombre qui tend vers $-\infty$ tend vers $+\infty$.

### Lire incorrectement un tableau de variations, notamment pour déterminer les extrêmes

Distinguer **la valeur de l'extremum** et **le point où il est atteint**.

Ici, le minimum de $f$ vaut $-1$, et il est atteint en $x = 1$. Écrire « le minimum est $1$ » ou « le minimum est atteint en $-1$ » est faux.

### Conclure sur le nombre de solutions sans justifier avec les variations et les limites

Justifier sur chaque intervalle de monotonie : la fonction est continue, strictement monotone, et la valeur cherchée est comprise entre les valeurs (ou les limites) aux bornes. C'est l'application du théorème de la bijection.

Une phrase comme « il y a deux solutions car la courbe a l'air de couper deux fois l'axe » n'est pas une justification.
