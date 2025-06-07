def print_arr(arr, i):

    if(i == len(arr)):
        return

    print_arr(arr, i + 1)
    print(arr[i])



arr = [1, 3, 2, 5, 4]
print_arr(arr, 0)