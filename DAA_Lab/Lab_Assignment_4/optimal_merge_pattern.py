class OptimalMergePattern:

    def bubbleSort(self, arr):

        i = 0
        while(i < len(arr) - 1):

            j = 0
            while(j < len(arr) - 1 - i):

                if(arr[j] > arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

                j += 1
            i +=1

    
    def calculateOptimalMergePattern(self, arr):
        
        total = 0
        while(len(arr) != 1):
            self.bubbleSort(arr)
            arr[1] = arr[0] + arr[1]
            total += arr[1]
            arr.pop(0)

        return total

def main():
    
    arr : str = input("Enter the size of arrays, separated by spaces : ")
    arr : list[int] = [int(e) for e in arr.split()]
    
    obj = OptimalMergePattern()
    result = obj.calculateOptimalMergePattern(arr)
    print(f"Minimum space required is : {result}")
    

if(__name__ == "__main__"):
    print()
    main()
    print()
