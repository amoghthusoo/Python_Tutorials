# Q11 :- Average Compilation  Time

class Average_Compilation_Time:

    def __init__(self, execution_time):
        self.execution_time = execution_time
        self.compilation_time = []

    def sort_list(self, arr : list[int]) -> None:
        
        i : int = 0
        while(i < len(arr) - 1):

            j : int = 0
            while(j < len(arr) - 1 - i):
                
                if(arr[j] > arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]

                j += 1
            i += 1

    def calulate_sum(self, arr : list[int]) -> int:

        total : sum = 0

        i : int = 0
        while(i < len(arr)):

            total += arr[i]
            i += 1

        return total

    def calculate_average_compilation_time(self) -> float:
        
        temp_complilation_time : int = 0

        i : int = 0
        while(i < len(self.execution_time)):
            
            temp_complilation_time += self.execution_time[i]
            self.compilation_time.append(temp_complilation_time)

            i += 1

        return self.calulate_sum(self.compilation_time)/len(self.compilation_time)
        

    def calculate_minimum_average_compilation_time(self):
        
        self.sort_list(self.execution_time)
        self.compilation_time = []
        return self.calculate_average_compilation_time()
    

def main() -> None:
    
    execution_time : str = input("Enter the execution time of n tasks, separated by spaces : ")
    execution_time : list[int] = [int(e) for e in execution_time.split()]

    obj = Average_Compilation_Time(execution_time)
    average_compilation_time = obj.calculate_average_compilation_time()
    minimum_average_compilation_time = obj.calculate_minimum_average_compilation_time()

    print(f"\nAverage Compilation Time (T1) : {round(average_compilation_time, 2)}")
    print(f"Minimum Average Compilation Time (T2) : {round(minimum_average_compilation_time, 2)}")
    print(f"Ratio (T1/T2) : {round(average_compilation_time / minimum_average_compilation_time, 2)}")
    
if(__name__ == "__main__"):
    print()
    main()
    print()
