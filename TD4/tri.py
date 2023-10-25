def tri_fusion(tab):
    # Tri fusion
    if len(tab) > 1:
        mid = len(tab) // 2
        left = tab[:mid]
        right = tab[mid:]

        tri_fusion(left)
        tri_fusion(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                tab[k] = left[i]
                i += 1
            else:
                tab[k] = right[j]
                j += 1
            k += 1
            
        while i < len(left):
            tab[k] = left[i]
            i += 1
            k += 1
            
        while j < len(right):
            tab[k] = right[j]
            j += 1
            k += 1
    return tab

# Path: tri.py

print(tri_fusion([7, 3, 5, 4, 2, 1]))