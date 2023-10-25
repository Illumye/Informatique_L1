# TD1

[Exercices](./TD1.pdf)

[Cours](./Tableaux.ipynb)

## Ex 1

```python
def startWithArray(t, n):
	m = t[3]
	for i in range(n-1, 0, -1):
		if t[i] < m:
        	m = t[i]
	return m
```

| Lignes | m | n | i | t[i] | t[i] < m |
| :----: | - | - | - | :--: | :------: |
| 1      |   | 6 |   |      |          |
| 2      | 1 |   |   |      |          |
| 3.1    |   |   | 5 |  2   |          |
| 4.1    |   |   |   |      |  False   |
| 3.2    |   |   | 4 |  10  |          |
| 4.2    |   |   |   |      |  False   |
| 3.3    |   |   | 3 |  1   |          |
| 4.3    |   |   |   |      |  False   |
| 3.4    |   |   | 2 |  7   |          |
| 4.4    |   |   |   |      |  False   |
| 3.5    |   |   | 1 |  5   |          |
| 4.5    |   |   |   |      |  False   |

- $n-1$ tours de boucle donc $2n-1$ comparaisons (car boucle for = $n$) 
- $1+n-1+n = 2n$ affectations (car boucle for = $n$)

## Ex 2

```python
from array import *

def insert(t: array, n: int, elt, k: int) -> int:
	if k >= m:
		t[n] = elt
	else:
		for i in range(n, k, -1):
			t[i] = t[i-1]
		t[k] = elt
	return n + 1
```

## Ex 3

```python
def delete(t: array, n: int, k: int) -> int:
	for i in range(k, n-1):
		t[i] = t[i+1]
	return n - 1
```

## Ex 4

```python
def amplitude(t: array, n: int):
	mini = t[0]
	maxi = t[0]
	for i in range(1, n):
		if t[i] < mini:
			mini = t[i]
		elif t[i] > maxi:
			maxi = t[i]
	return maxi - mini
```

## Ex 5

```python
def max2(t: array, n: int):
	if t[0] > t[1]:
		max1 = t[0]
		max2 = t[1]
	else:
		max1 = t[1]
		max2 = t[0]
	for i in range(2, n):
		if t[i] > max1:
			max2 = max1
			max1 = t[i]
		elif t[i] > max2:
			max2 = t[i]
	return max2
```

## Ex 6

```python
def deleteFirstInstance(t: array, n: int, elt):
	for i in range(0, n):
		if t[i] == elt:
			return delete(t, n, i)
	return n
```

## Ex 7

```python
def deleteInstances(t: array, n: int, elt) -> int:
    occ = 0
    for i in range(n):
        if t[i] == elt:
            occ += 1
        else:
            t[i-occ] = t[i]
    return n - occ
```

## Ex 9

```python
def myFunction(t, n, x):
    stop = False
    while n > 0 and not stop:
        numberOfElement = deleteFirstInstance(t, n, x)
        if numberOfElement == n:
            stop = True
        else:
            n = numberOfElement
    return n

t = array('i', [2, -7, 4, 5, 12, 10, 4, 2, 4, -18])
```


