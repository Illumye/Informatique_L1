from array import *

## Ex 1
def recherche(t: array, n: int, val: int):
    for i in range(n):
        if t[i] == val:
            return True
    return False

def dichotomie(t: array, n: int, val: int):
	debut = 0
	fin = n
	while debut <= fin:
		m = (debut+fin) // 2
		if t[m] == val:
			return m
		elif t[m] < val:
			debut = m + 1
		else:
			fin = m - 1
	return -1

t = array('I', [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
print(dichotomie(t, 10, 4))
print(dichotomie(t, 10, 1))
print(dichotomie(t, 10, -1))
print(dichotomie(t, 10, 9))
print(dichotomie(t, 10, 0))

def rotationAdroite(t: array, n: int):
    if len(t) >= 2:
        final = t[n-1]
        for i in range(n-2, -1, -1):
            t[i+1] = t[i]
        t[0] = final    
    return t

print(rotationAdroite(array('I', [0, 1, 2, 3, 4, 5, 6]), 7))