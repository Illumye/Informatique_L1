# TD2

## Ex 4
```python
def sequenceMax(t: array, n: int):
    s_max = 0
    for i in range(n):
        for j in range(i, n):
            s_temp = 0
            for k in range(i, j+1):
                s_temp += t[k]
                if s_temp > s_max:
                    s_max = s_temp
    return s_max
```

Complexité :

$$
\sum_{j=1}^{n-i} j =\frac{(n-1)(n-i+1)}{2}
$$
Pour un i donné i va de 0 à n-1
=> nombre de fois où on passe dans la boucle h

$$
\sum_{i=0}^{n-1}\frac{(n-i)(n-i+1)}{2}
$$
$$\frac{1}{2}\sum_{i=0}^{n-1}(n²-ni+n-ni+i²-i)$$
$$\frac{1}{2}\left( n^3+n²+\sum_{i=0}^{n-1}(i(-2n-1)+i²) \right)$$