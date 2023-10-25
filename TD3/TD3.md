# TD3

## Exercice 2

```
Appels:

foo3(3)
foo4(2)
foo3(1)
foo4(0)

Affichage :

3
1
0
2
```

```
Appels :

foo4(3)
foo3(2)
foo4(1)
foo3(0)

Affichage :

2
0
1
3
```

## Exercice 3

$$\frac{2}{5}=\frac{1}{5}+\frac{1}{6}+\frac{1}{30}=\frac{1}{5}+\frac{1}{8}+\frac{1}{20}+\frac{1}{40}$$

1. Problème : pas d'arrêt : si `a` vaut `1`, appel récursif infini

### Correction
```python
def f(a,b):
	if a == 1:
		print(f'1/{b}, end='   ')
	else:
		f(1,b)
		f(a-1,b+1)
		f(a-1,b*(b+1))
```

### Pile d'exécution
```
Appels :

f(2,5)
f(1,5)
f(1,6)
f(1,30)

Affichage :

1/5
1/6
1/30
```

## Exercice 4

```python
def powRec(a, n):
	if n==0:
		return 1
	return a*powRec(a, n-1)
```

```
Appels:

powRec(2,4) --> vaut 16
powRec(2,3) --> vaut 8
powRec(2,2) --> vaut 4
powRec(2,1) --> vaut 2
powRec(2,0) --> vaut 1
```

## Exercice 5

On suppose t trié :

```python
def dichotomie_recursive(x, t, g, d):
	if g == d:
		if t[g] == x:
			return True
		else:
			return False
	else:
		milieu = (g+d)//2
		if t[milieu] < x:
			return dichotomie_recursive(x, t, milieu+1, d)
		elif t[milieu] > x:
			return dichotomie_recursive(x, t, g, milieu-1)
		else:
			return True
```

---
## Récursion factorielle

```python
# Récursif normal
def fact(n):
	if n == 0:
		return 1
	else:
		return n*fact(n-1)

# Itératif
def fact_iter(n):
	p = 1
	for i in range(2, n+1):
		p = p*i
	return p

# Récursif terminal
def fact_aux(n, p):
	if n == 0:
		return p
	return fact_aux(n-1, n*p)
	
def fact_rt(n):
	def aux(n, p):
		if n == 0:
			return p
		return aux(n-1, n*p)
	return aux(n, 1)
```

---

## Exercice 6

```python
def mystere(tab, g, d):
	if g == d:
		return tab[g]
	else:
		milieu = (g+d)//2 - 1
		if milieu % 2 == 1:
			milieu += 1
		elif tab[milieu] != tab[milieu + 1]
			return mystere(tab, g, milieu)
		else:
			return mystere(tab, milieu + 2, d)
```