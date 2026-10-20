# Le raisonnement par récurrence

Cette fiche présente une méthode pour démontrer une inégalité vraie pour tous les entiers $n$. Le grand exemple du milieu se lit pas à pas : prendre le temps de le refaire à la main.

---

## 1. Dans quels cas utiliser une démonstration par récurrence

On utilise la récurrence quand il faut démontrer une égalité, une inéquation, une formule **pour tout entier naturel $n$**, et que l'on connaît le lien entre un terme et le suivant, par exemple $u_{n+1} = 2u_n$.

Si la suite est donnée par une formule en $n$ (comme $u_n = 2 - \frac{1}{n+1}$), on peut souvent encadrer directement. La récurrence est surtout utile pour les suites définies à partir de leur terme précédent.

### Démontrer une inégalité pour tout entier naturel

Typiquement, la récurrence sert à démontrer des inégalités comme :

- $u_n \leq 3$ pour tout $n$ ;
- $u_n \geq n$ pour tout $n$ ;
- $0 < u_n < 1$ pour tout $n$.

Le principe se visualise avec une rangée de dominos. Pour qu'ils tombent tous, il faut deux choses :

1. **Initialisation** : le premier domino tombe.
2. **Hérédité** : si un domino tombe, alors il fait tomber le suivant.
3. **Conclusion** : tous les dominos tombent.

En mathématiques : on démontre $P(0)$ c'est-à-dire on regarde si ce qu'on veut démontrer est vrai pour le premier terme, puis on démontre que $P(n)$ vraie entraîne $P(n+1)$ vraie, c'est-à-dire on démontre que notre opération qu'on suppose vraie entraîne le fait que l'opération au rang suivant l'est aussi. Enfin, on en conclut que $P(n)$ est vraie pour tout $n$.

---

## 2. Grand exemple de démonstration par récurrence

### Énoncé

Soit $(u_n)$ la suite définie par $u_0 = 1$ et, pour tout entier naturel $n$ :

$$u_{n+1} = 2u_n + 1$$

**Démontrer que, pour tout entier naturel $n$, $u_n \geq n$.**

### Avant de rédiger : poser la propriété

On écrit clairement la propriété à démontrer, avec un nom :

$$P(n) : \quad u_n \geq n$$

On écrit aussi ce que dirait cette propriété au rang suivant, car c'est elle que l'hérédité devra démontrer :

$$P(n+1) : \quad u_{n+1} \geq n + 1$$

*Pourquoi :* il faut savoir exactement où l'on va avant de calculer.

### Étape 1 : Initialisation

Vérifier que $P(0)$ est vraie, c'est-à-dire que l'inégalité est vraie pour le premier rang.

$$u_0 = 1 \quad \quad 0 \leq 1 \quad \text{donc} \quad u_0 \geq 0$$

$P(0)$ est vraie.

*Pourquoi cette étape est importante :* c'est le premier domino. Sans lui, rien ne peut tomber.

### Étape 2 : Hérédité

**a) Poser l'hypothèse.** Soit $n$ un entier naturel quelconque. Supposons que $P(n)$ est vraie, c'est-à-dire :

$$u_n \geq n \qquad \text{(hypothèse de récurrence)}$$

*Pourquoi :* on ne démontre pas cette inégalité, on l'admet **temporairement** pour construire la suite du raisonnement. Le mot « quelconque » est important : on raisonne pour un rang $n$ général.

**b) On annonce l'objectif.** Il faut montrer que $P(n+1)$ est vraie :

On reprend l'hypothèse de récurrence c'est-à-dire $P(n)$ et on remplace $n$ par $n+1$ : 

$$u_{n+1} \geq n + 1$$

**c) On calcule.** On reprend dans l'énoncé ce qu'est $u_{n+1}$ soit :

$$u_{n+1} = 2u_n + 1$$

Et notre but est de réécrire $u_{n+1}$ à partir de l'hypothèse de récurrence pour qu'on ait un encadrement de $u_{n+1}$. Si les choses sont bien faites, on devrait retomber sur ce qu'on veut démontrer.

Donc on utilise et on écrit en premeir l'hypothèse de récurrence $u_n \geq n$ soit :
$$u_n \geq n$$

On multiplie de part et d'autre par 2 soit :

$$2u_n \geq 2n$$

Comme 2 est positif le sens de l'inégalité ne change pas

On ajoute 1 :

$$2u_n + 1 \geq 2n + 1$$

On est retombé sur $2u_n+1$ qui est notre $u_n+1$.
Donc : $$u_n+1 \geq 2n+1$$

Or, $$2n+1 \geq n+1$$
Donc : $$u_n+1 \geq n+1$$

**d) On conclut.** On a obtenu $u_{n+1} \geq n + 1$ : $P(n+1)$ est vraie.

*Pourquoi :* on a montré que, **si** $P(n)$ est vraie, **alors** $P(n+1)$ est vraie. C'est le passage d'un domino au suivant.

### Étape 3 : Conclusion

$P(0)$ est vraie (initialisation) et $P(n)$ vraie entraîne $P(n+1)$ vraie (hérédité). Par le principe de récurrence, $P(n)$ est vraie pour tout entier naturel $n$.

### La rédaction complète, à retenir

Voici la version propre, telle qu'on la rédigerait sur une copie.

 Pour tout entier naturel $n$, on note $P(n)$ la propriété : $u_n \geq n$.
>
 **Initialisation.** Pour $n = 0$ : $u_0 = 1 \geq 0$. Donc $P(0)$ est vraie.
>
 **Hérédité.** Soit $n$ un entier naturel. Supposons que $P(n)$ est vraie, c'est-à-dire $u_n \geq n$. Montrons que $P(n+1)$ est vraie, c'est-à-dire $u_{n+1} \geq n + 1$.
>
D'après l'hypothèse de récurrence, $u_n \geq n$. 

Donc $2u_n \geq 2n$. 

$2u_n+1 \geq n+1$ Or $2u_n+1 = u_n+1$.

Donc $u_n+1 \geq 2n + 1$ 

Or, $2n + 1 \geq n + 1$ car $n \geq 0$. 

Ainsi $u_{n+1} \geq n + 1$ 

$P(n+1)$ est donc vraie.
>
>**Conclusion.** On a démontré que $P(0)$ est vraie et que $P(n+1)$ l'est. Par récurrence, $P(n)$ est donc vraie pour tout $n \geq 0$.


---

## 3. Erreurs fréquentes

### Oublier l'initialisation qui est très importante

L'hérédité seule ne démontre rien : sans premier domino, aucun ne tombe.

Prendre $P(n) : \; n = n + 1$. L'hérédité fonctionne : si $n = n + 1$, alors en ajoutant 1 des deux côtés, $n + 1 = n + 2$, on arrivera sur $P(n+1)$ vraie. Pourtant la propriété est fausse, si on teste l'égalité pour le premier terme on tombe sur 0 = 1 ce qui est faux. C'est l'initialisation qui échoue, et qui le révèle.

### Mal rédiger la conclusion

La conclusion doit **rappeler les deux étapes** et préciser **pour quels $n$** la propriété est vraie.

- À éviter : « Donc c'est démontré. » ou « Donc $P(n+1)$ est vraie. » Ces phrases ne disent ni pourquoi ni pour quels entiers.
- À écrire : « $P(0)$ est vraie et $P(n)$ vraie entraîne $P(n+1)$ vraie. Par récurrence, $P(n)$ est vraie pour tout entier naturel $n$. »

### Hypothèse de récurrence non utilisée

L'hypothèse de récurrence est le seul lien entre le rang $n$ et le rang $n+1$. Si elle n'apparaît nulle part dans l'hérédité, la preuve est fausse (ou la récurrence est inutile).

Dans l'exemple précédent, écrire « $u_{n+1} = 2u_n + 1 \geq n + 1$ » sans passer par $u_n \geq n$ ne justifie rien : rien n'indique que $2u_n + 1$ est grand. Relire l'hérédité et repérer la ligne où l'on utilise l'hypothèse de récurrence. Si cette ligne n'existe pas, il manque une étape.
