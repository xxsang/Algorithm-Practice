# Selection sort algorithm

def selection_sort(list_a):
    for i in range(len(list_a)-1):
        j = i+1
        while j < len(list_a):
            if list_a[i]>list_a[j]:
                minimum = list_a[j]
                list_a[j] = list_a[i]
                list_a[i] = minimum
            j += 1
    return list_a

# Test the algorithm
list_a = [8,876,98,100,3,1,0]
print selection_sort(list_a)
