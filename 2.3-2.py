# The merge process in merge-sort algorithm

def merge(list_a,list_b):
    merged_list = []
    n1 = len(list_a)
    n2 = len(list_b)
    index = n1+n2
    i_a = 0
    i_b = 0
    for i in range(index):
        if i_a < n1 and i_b < n2:
            if list_a[i_a] > list_b[i_b]:
                merged_list.append(list_b[i_b])
                i_b += 1
            else:
                merged_list.append(list_a[i_a])
                i_a += 1
    return merged_list

# Test the algorithm
list_a = [1,3,5,7]
list_b = [0,4,6,8]
print merge(list_a,list_b)
