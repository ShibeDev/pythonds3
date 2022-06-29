def compareswap(L,a,b):
    L[a], L[b] = min(L[a],L[b]),max(L[a],L[b])

def medianfirst(L,a,b,c):
    compareswap(L,b,a) # L[b]<=L[a]
    compareswap(L,b,c) # L[b]<=L[c] i.e L[b] smallest
    compareswap(L,a,c) # L[a]<=L[c] i.e L[c] largest 

def quick_sort(L):
    #call helper function and pass in initial list and end indexes
    quick_sort_helper(L,0,len(L)-1)

#helper function to be recursively called on the left & right partitions based on the pivot value
def quick_sort_helper(L,first,last):
    if first<last:
        split = partition(L,first,last)
        quick_sort_helper(L,first,split-1)
        quick_sort_helper(L,split+1,last)

def partition(L,first,last):
    #use median of 3 for pivot
    print(L)
    middle = (first+last-1)//2
    medianfirst(L,first,middle,last-1)
    pivot_val = L[first]
    left_mark = first + 1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and L[left_mark] <= pivot_val:
            left_mark += 1
        while left_mark <= right_mark and L[right_mark] >= pivot_val:
            right_mark -=1
        if right_mark < left_mark:
            done = True
        else:
            if L[left_mark] > L[right_mark]:
                L[left_mark],L[right_mark] = L[right_mark],L[left_mark]
    
    L[first],L[right_mark] = L[right_mark], L[first]

    return right_mark

L = [54, 26, 93, 17, 77, 31, 44, 55, 20]
quick_sort(L)
print(L)
