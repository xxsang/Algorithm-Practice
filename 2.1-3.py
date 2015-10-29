# Linear search with list A and value v as inputs
def linear_search(list_a,v):
    return_v = False
    for i in range(len(list_a)):
        if v == list_a[i]:
            return_v = True
            return i

    if return_v == False:
        return "NIL"

# Test the code
list_a = [97, 87, 37, 9, 2, 1]
v = 9
print linear_search(list_a,v)
