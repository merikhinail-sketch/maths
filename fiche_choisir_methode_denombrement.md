# Quelle méthode de dénombrement utiliser ?

Face à un exercice de dénombrement, la difficulté est souvent de savoir **quoi calculer**. Cette fiche donne trois questions à se poser pour choisir la bonne méthode à coup sûr.

---

## 1. Comprendre ce qu'on cherche et questions à se poser

### Les 4 situations à reconnaître

Dans une question de dénombrement, on cherche toujours l'une de ces quatre choses :

1. **Un $k$-uplet avec répétition** : une liste ordonnée de $k$ éléments, où un même élément peut apparaître plusieurs fois.
2. **Un $k$-uplet d'éléments distincts** : une liste ordonnée de $k$ éléments, tous différents.
3. **Une permutation** : un rangement de **tous** les éléments d'un ensemble dans un certain ordre.
4. **Une combinaison** : un groupe de $k$ éléments choisis parmi $n$, **sans ordre**.

### Les questions à se poser

Se poser les trois questions suivantes, dans cet ordre.

**Question 1 : l'ordre compte-t-il ?**

Test simple : échanger deux éléments change-t-il le résultat ?

- **Non**, l'ordre ne compte pas (on forme un groupe, un comité, une main de cartes) : c'est une **combinaison**.
- **Oui**, l'ordre compte (code, classement, rangement) : passer à la question 2.

**Question 2 : utilise-t-on tous les éléments ?**

- **Oui**, on range tous les éléments : c'est une **permutation**.
- **Non**, on n'en choisit que $k$ parmi $n$ : passer à la question 3.

**Question 3 : un même élément peut-il être choisi plusieurs fois ?**

- **Oui**, les répétitions sont possibles : c'est un **$k$-uplet avec répétition**.
- **Non**, tous les éléments sont différents : c'est un **$k$-uplet d'éléments distincts**.

### Résumé : la méthode à utiliser

| Situation | Calcul |
|---|---|
| $k$-uplet avec répétition | $n^k$ |
| $k$-uplet d'éléments distincts | $n \times (n-1) \times \dots \times (n-k+1)$ |
| Permutation | $n!$ |
| Combinaison | $\dbinom{n}{k} = \dfrac{n!}{k!\,(n-k)!}$ |

### Un exemple pour chaque situation

**Exemple 1 : $k$-uplet avec répétition.** Combien de codes à 4 chiffres peut-on former, les chiffres pouvant se répéter ?

L'ordre compte (un code), on ne range pas tout, et les répétitions sont permises :

$$10^4 = 10\,000$$

**Exemple 2 : $k$-uplet d'éléments distincts.** Huit coureurs participent à une course. Combien y a-t-il de podiums possibles (1er, 2e, 3e) ?

L'ordre compte (le 1er n'est pas le 3e), on n'en choisit que 3 sur 8, et un coureur ne peut pas occuper deux places :

$$8 \times 7 \times 6 = 336$$

**Exemple 3 : permutation.** De combien de façons peut-on ranger 5 livres différents sur une étagère ?

L'ordre compte et tous les livres sont utilisés :

$$5! = 120$$

**Exemple 4 : combinaison.** Dans une classe de 10 élèves, combien de comités de 3 élèves peut-on former ?

Un comité est un groupe : l'ordre ne compte pas.

$$\binom{10}{3} = \frac{10!}{3!\,7!} = \frac{10 \times 9 \times 8}{3 \times 2 \times 1} = 120$$

**Attention aux énoncés qui se ressemblent.** Choisir 2 élèves parmi 10 :

- comme **président et secrétaire** : l'ordre compte (échanger les deux change le résultat), c'est un $2$-uplet d'éléments distincts : $10 \times 9 = 90$ ;
- comme **deux délégués** : l'ordre ne compte pas, c'est une combinaison : $\dbinom{10}{2} = 45$.
