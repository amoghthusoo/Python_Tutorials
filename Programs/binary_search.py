def binary_search(lower_bound, upper_bound, array, target):

    while lower_bound <= upper_bound:

        middle_index = (lower_bound + upper_bound) // 2

        if array[middle_index] == target:
            return middle_index
        else:

            if array[middle_index] > target:
                upper_bound = middle_index - 1
            else:
                lower_bound = middle_index + 1
    
    return None


def upper_index(lower_bound, upper_bound, array, target):

    upper_index = None

    while True:
        found_index = binary_search(lower_bound, upper_bound, array, target)
        
        
        if found_index != None:
            upper_index = found_index
            lower_bound = found_index + 1
        else:
            break

    return upper_index

def lower_index(lower_bound, upper_bound, array, target):

    lower_index = None

    while True:
        found_index = binary_search(lower_bound, upper_bound, array, target)
        
        
        if found_index != None:
            lower_index = found_index
            upper_bound = found_index - 1
        else:
            break

    return lower_index


    
array = [2, 3, 3, 3, 3, 8, 13]
target = 3
lower_bound = 0
upper_bound = 6

print(lower_index(lower_bound, upper_bound, array, target))