# Q5 :- Largest Sum

class Largest_Sum:

    def slice_array(self, arr : list[int], lower_bound : int, upper_bound : int) -> list[int]:
        
        sliced_array = []
        i : int = lower_bound
        while(i <= upper_bound):
            
            sliced_array.append(arr[i])
            i += 1

        return sliced_array
        

    def sum_array(self, arr : list[int]) -> int:
        
        total : int = 0
        
        i : int = 0
        while(i < len(arr)):

            total += arr[i]
            i += 1

        return total

    def find_largest_sum(self, arr : list[int]) -> int:
   
        possible_sums = []
    
        i : int = 0
        while(i < len(arr)):

            j : int = i
            while(j < len(arr)):
                
                # possible_sums.append(sum(arr[i : j + 1]))
                possible_sums.append(self.sum_array(self.slice_array(arr, i, j)))

                j += 1
            i += 1

        max_element : int = possible_sums[0]

        i = 0
        while(i < len(possible_sums)):
            
            if(possible_sums[i] > max_element):
                max_element = possible_sums[i]
            
            i += 1

        return max_element
    
def main():
    
    arr : str = input("Enter the array elements, separated by spaces : ")
    arr : list[int] = [int(e) for e in arr.split()]

    obj = Largest_Sum()
    largest_sum = obj.find_largest_sum(arr)

    print(f"\nLargest sum in the given array is : {largest_sum}")

if(__name__ == "__main__"):
    print()
    main()
    print()
