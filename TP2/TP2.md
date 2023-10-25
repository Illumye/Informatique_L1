# TP2

## Ex 1

```python
from array import *

def recherche(t: array, n: int, val: int):
    for i in range(n):
        if t[i] == val:
            return True
    return False
```

Dans le meilleur des cas : $1$ comparaison

Dans le pire des cas : $n$ comparaisons

## Ex 2

1. La différence est que la recherche fait une comparaison supplémentaire : elle compare deux valeurs et vérifie si elle est plus grand ou plus petite
2.  Faire un tableau de valeurs de 1 à 100 : si trop grand --> on supprime le nombre proposé puis ceux plus grand jusqu'à 100
    si trop petit --> on supprime le nombre proposé puis ceux plus petit jusqu'à 1
3. La valeur à trouver
4. Les valeurs "supprimées" trop grandes ou trop petites
5. Elle peut utiliser la dichotomie
6. $O(\log_{2}n)$

## Ex 3
```python
def dichotomie(t: array, n: int, val: int):
	debut = 0
	fin = n - 1
	while debut <= fin:
		m = (debut+fin) // 2
		if t[m] == val:
			return m
		elif t[m] < val:
			debut = m + 1
		else:
			fin = m - 1
	return -1
```
1. Programme python
2. La taille du tableau est divisée par deux à chaque comparaisons jusqu'à $2^{0}$

## Ex 4
```python
def dichotomie_f(f, a, b, epsilon):
	
```

$f(a)>0$ et $f(b)<0$

On teste $m=\frac{a+b}{2}$
- regarder le signe de $f(m)$
- si $f(m)>0$, je sais que la racine cherchée est entre $m$ et $b$
- si $f(m)<0$, la racine est racine est entre $a$ et $m$