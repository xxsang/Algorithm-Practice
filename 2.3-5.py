# Binary search algorithm
def binary_search(list_a,v):
    list_a.sort()
    first = 0
    last = len(list_a)-1
    flag = False

    while first <= last and not flag:
        mid = (last-first)//2+first
        if list_a[mid] > v:
            last = mid -1
        elif list_a[mid] < v:
            first = mid +1
        else:
            flag = True
            return mid

    if not flag:
        return "Nil"

# Test algorithm
list_a =[1,1,5,6,8,10,15]
v = 10
print binary_search(list_a,v)