def partition(array, lower_bound, upper_bound):
    
    pivot = array[upper_bound]
    i = lower_bound
    j = upper_bound - 1

    while(i < j):

        while(array[i] <= pivot and i < upper_bound):
            i += 1

        while(array[j] >= pivot and j > lower_bound):
            j -= 1

        if(i < j):
            array[i], array[j] = array[j], array[i]

    if (array[i] >= array[upper_bound]):
        array[i], array[upper_bound] = array[upper_bound], array[i]
           
    return i

def quick_sort(array, lower_bound, upper_bound):

    if(lower_bound < upper_bound):

        partition_index = partition(array, lower_bound, upper_bound)
        quick_sort(array, lower_bound, partition_index - 1)
        quick_sort(array, partition_index + 1, upper_bound)


# array = [2, 3, 7, 4, 6, 1, 5]
# array = [5, 4, 3, 2, 1]
array = [1, 1, 1, 1, 1]
quick_sort(array, 0, len(array) - 1)
print(array)
