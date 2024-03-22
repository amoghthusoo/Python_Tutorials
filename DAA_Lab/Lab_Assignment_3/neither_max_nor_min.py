# Q4 :- Neither Maximum Nor Minimum

class Neither_Max_Nor_Min:

    def find_neither_max_not_min(self, arr : list[int]) -> int | None:
        
        min_element = arr[0]
        max_element = arr[0]

        i : int = 0
        while(i < len(arr)):
            
            if(arr[i] < min_element):
                min_element = arr[i]

            if(arr[i] > max_element):
                max_element = arr[i]
    
            i += 1

        i = 0
        while(i < len(arr)):

            if(arr[i] not in [min_element, max_element]):
                return arr[i]
            i += 1

        return None

def main():
    
    arr : str = input("Enter the array elements, separated by spaces : ")
    arr : list[int] = [int(e) for e in arr.split()]

    obj = Neither_Max_Nor_Min()
    neither_max_nor_min_element : int = obj.find_neither_max_not_min(arr)

    if(neither_max_nor_min_element != None):
        print(f"\nElement which is neither maximum nor minimum is : {neither_max_nor_min_element}")
    else:
        print("\nNo such element found which is neither maximum nor minimum.")

if(__name__ == "__main__"):
    print()
    main()
    print()
