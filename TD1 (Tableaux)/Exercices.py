from array import *

## Ex 3
tab = array('I', [5, 3, 4, 6, 1, 10, 2, 10, 4])

def delete(t: array, n: int, k: int) -> int:
	for i in range(k, n-1):
		t[i] = t[i+1]
	return n-1

print(delete(tab, 4, 3), tab)

## Ex 4
t = array("I", [2, 8, 11, 5, 9, 3, 1])

def amplitude(t: array, n: int):
	mini = t[0]
	maxi = t[0]
	for i in range(1, n):
		if t[i] < mini:
			mini = t[i]
		elif t[i] > maxi:
			maxi = t[i]
	return maxi - mini

print(amplitude(t, 4))

## Ex 5
t = array('I', [5, 3, 4, 6, 1, 10, 2, 10, 4])

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

print(max2(t, 5), max2(t, 9))

## Ex 6
def deleteFirstInstance(t: array, n: int, elt):
	for i in range(0, n):
		if t[i] == elt:
			return delete(t, n, i)
	return n

a = array('I', [5, 3, 4, 6, 1, 10, 2, 10, 4])

print(deleteFirstInstance(a, 3, 3))

## Ex 7
def deleteInstances(t: array, n: int, elt) -> int:
    occ = 0
    for i in range(n):
        if t[i] == elt:
            occ += 1
        else:
            t[i-occ] = t[i]
    return n - occ

a = array('I', [1, 3, 5, 3, 0])

print(deleteInstances(a, 5, 3))

## Ex 8
# def unduplicated(t: array, n: int) -> bool:
#     for i in range(n):
        

# print(unduplicated(a, 5))

## Ex 9
def myFunction(t, n, x):
    stop = False
    while n > 0 and not stop:
        numberOfElement = deleteFirstInstance(t, n, x)
        if numberOfElement == n:
            stop = True
        else:
            n = numberOfElement
    return n