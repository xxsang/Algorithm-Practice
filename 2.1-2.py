# Insertion-sort in decreasing order
def insert_sort_dec(list_a):
    new_list = list_a
    for i in range(1,len(new_list)):
        key = new_list[i]
        # Insert the current key into list
        j = i-1
        while j>=0 and new_list[j]<key:
            new_list[j+1]=new_list[j]
            j -= 1
        new_list[j+1]=key
    return new_list

# Test the code with a sample list
list_a = [1,9,37,2,87,97]
print insert_sort_dec(list_a)
