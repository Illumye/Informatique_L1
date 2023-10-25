from array import *
import random

def rollDice(n: int):
    tirage = array('H', [0]*n)
    for i in range(n):
        tirage[i] = random.randint(1, 6)
    return tirage

def sumValues(t: array, n: int):
    somme = 0
    for i in range(n):
        somme += t[i]
    return somme

def numberOfDiceWithSameValue(t: array, n: int, value: int):
    occ = 0
    for i in range(n):
        if t[i] == value:
            occ += 1
    return occ

def histogram(t: array, n: int):
    histogram = array('H', [0]*7)
    histogram[0] = n
    for i in range(1, 7):
        histogram[i] = numberOfDiceWithSameValue(t, n, i)
    return histogram

def histogram_bis(m: int, n: int):
    a = array('H', [0]*7)
    a[0] = n
    for i in range(m):
        t = rollDice(n)
        print(t)
        for j in range(1, 7):
            a[j] += numberOfDiceWithSameValue(t, n, j)
    return a

def maxSubarraySum(t: array, n: int) -> int:
    maxi = t[0]
    for i in range(1, n):
        if t[i] > maxi:
            maxi = t[i]
    return maxi*numberOfDiceWithSameValue(t, n, maxi)

def moveDice(t: array, n: int, value: int) -> array:
    r = 0
    for i in range(n):
        if t[i] == value:
            tmp = t[r]
            t[r] = t[i]
            t[i] = tmp
            r += 1
    return t

def rollDiceAgain(t: array, nt: int, s: array, ns: int) -> array:
    for i in range(ns):
        t[s[i]] = random.randint(1, 6)
    return t

def searchSequence(t: array, n: int) -> int:
    h = histogram(t, n)
    # Si séquence = [1, 2, 3, 4, 5] (pas d'ordre)
    if h[1] == 1:
        for i in range(2, 6):
            if h[i] == 0:
                # Si aucune séquence
                return -1
        return 0
    # Si séquence = [2, 3, 4, 5, 6] (pas d'ordre)
    elif h[1] == 0:
        for i in range(3, 7):
            if h[i] == 0:
                # Si aucune séquence
                return -1
        return 1
    else:
        return -1

# def jouerTour(t: array):
#     a = rollDice(5)
#     h = histogram(a, 5)
#     occ_max = 0
#     for i in range(1, 6):
        
            
        
        
        
            
        
        
        
dices = rollDice(5)
index = array('H', [3, 4])
test = array('H', [4, 6, 3, 2, 5])

print(dices)

# print(sumValues(dices, 5))
# print(numberOfDiceWithSameValue(dices, 5, 3))
# print(histogram(dices, len(dices)))
# print(histogram_bis(3, 5))
# print(maxSubarraySum(dices, 5))
# print(moveDice(dices, 5, 6))
# print(rollDiceAgain(dices, len(dices), index, len(index)))
# print(searchSequence(test, 5))