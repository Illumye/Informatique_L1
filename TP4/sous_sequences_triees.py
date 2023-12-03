from copy import deepcopy
from random import randint as rd
from array import *
import timeit
import sys

sys.setrecursionlimit(1000000)

def XSort(t, i, j):
    if i >= j:
        return
    XSort(t, i, j-1)
    if t[j-1] > t[j]:
        tmp = t[j-1]
        t[j-1] = t[j]
        t[j] = tmp
        XSort(t, i, j-1)

def triFusion(t: array, g:int, d:int):
    if g < d - 1:
        m = (g + d)//2
        triFusion(t, g, m)
        triFusion(t, m, d)
        fusionner(t, g, d)
        
def fusionner(t, g, d):
    t_tmp = array('l', [0 for i in range(d-g)])
    m = (g + d)//2
    
    ind_g = g
    int_d = m
    ind_tmp = 0
    
    while ind_g < m and int_d < d:
        if t[ind_g] < t[int_d]:
            t_tmp[ind_tmp] = t[ind_g]
            ind_g += 1
        else:
            t_tmp[ind_tmp] = t[int_d]
            int_d += 1
        ind_tmp += 1
        
    while ind_g < m:
        t_tmp[ind_tmp] = t[ind_g]
        ind_g += 1
        ind_tmp += 1
    
    while int_d < d:
        t_tmp[ind_tmp] = t[int_d]
        int_d += 1
        ind_tmp += 1
    
    for i in range(len(t_tmp)):
        t[g + i] = t_tmp[i]
        
def triInsertion(t, n):
    for i in range(1, n):
        tmp = t[i]
        j = i
        while j > 0 and t[j-1] > tmp:
            t[j] = t[j-1]
            j -= 1
        t[j] = tmp
    
time_triFusion = 0
time_triInsertion = 0
time_XSort = 0

nb_tour = 1
taille = 100

T0 = [rd(0, 10) for i in range(taille)]

for j in range(nb_tour):
    T0 = array('l', [rd(0, 10) for i in range(taille)])
    
    T = deepcopy(T0)
    start_time = timeit.default_timer()
    triFusion(T, 0, taille)
    end_time = timeit.default_timer()
    time_triFusion += end_time - start_time
    
    if taille <= 10000:
        T = deepcopy(T0)
        start_time = timeit.default_timer()
        triInsertion(T, taille)
        end_time = timeit.default_timer()
        time_triInsertion += end_time - start_time
    
    if taille <= 1000:
        T = deepcopy(T0)
        start_time = timeit.default_timer()
        XSort(T, 0, taille-1)
        end_time = timeit.default_timer()
        time_XSort += end_time - start_time

time_triFusion /= nb_tour
time_triInsertion /= nb_tour
time_XSort /= nb_tour

print(f'Pour taille = {taille}\ntime_triFusion = {time_triFusion}\ntime_triInsertion = {time_triInsertion}\ntime_XSort = {time_XSort}')

# def partition(n, k):
    
#     part = k*[1]
#     if k < n:
#         for i in range(k):
#             total = sum(part)
#             if i == k - 1:
#                 p = n-total+1
#             else:
#                 p = rd(1, n-total)
#             part[i] = p
#     return part
    
# def fabriquerSousSequenceTrie(n, p, inf, sup):
    
#     T = []
#     une_partition = partition(n, p)
#     for taille in une_partition:
#         T += sorted([rd(inf, sup) for i in range(taille)])
#     return T
