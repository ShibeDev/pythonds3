def mergesort(L):
    print("Splitting", L)
    if len(L)>1:
        mid = len(L) // 2
        left_half = L[:mid]
        right_half = L[mid:]

        mergesort(left_half)
        mergesort(right_half)

        i,j,k = 0,0,0
        while i<len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                L[k] = left_half[i]
                i+=1
            else:
                L[k] = right_half[j]
                j+=1
            k+=1

        while i < len(left_half):
            L[k] = left_half[i]
            i+=1
            k+=1
        
        while j < len(right_half):
            L[k] = right_half[j]
            j+=1
            k+=1
        
    print("Merging", L)

L = [54, 26, 93, 17, 77, 31, 44, 55, 20]
mergesort(L)
print(L)