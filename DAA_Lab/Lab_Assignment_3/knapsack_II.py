# Q7 :- Knapsack - II

class Knapsack_II:

    def __init__(self, profit : list[int], weight : list[int], capacity : int):
        
        self.profit : list[int] = profit
        self.weight : list[int] = weight
        self.capacity : int = capacity

    def sort_by_profit_weight_ratio(self):
        
        i : int = 0
        while(i < len(self.profit) - 1):

            j : int = 0
            while(j < len(self.profit) - 1 - i):

                if(self.profit[j]/self.weight[j] < self.profit[j + 1]/self.weight[j + 1]):

                    self.profit[j], self.profit[j + 1] = self.profit[j + 1], self.profit[j]
                    self.weight[j], self.weight[j + 1] = self.weight[j + 1], self.weight[j]

                j += 1
            i += 1

    def calculate_optimal_solution(self, fractionl_mode : bool = True) -> int | float:
        
        self.sort_by_profit_weight_ratio()

        weight : float = 0
        profit : float = 0

        i : int = 0
        while(i < len(self.profit)):

            if(weight == self.capacity):
                break

            elif(weight + self.weight[i] <= self.capacity):
                profit += self.profit[i]
                weight += self.weight[i]

            else:
                
                if(fractionl_mode):
                    profit += ((self.capacity - weight)/self.weight[i]) * self.profit[i] 
                    weight = self.capacity
                else:
                    break

            i += 1

        return profit

def main():
    
    profit : str = input("Enter the profit of objects, separated by spaces : ")
    profit : list[int] = [int(e) for e in profit.split()]
    
    weight : str = input("Enter the weight of objects, separated by spaces : ")
    weight : list[int] = [int(e) for e in weight.split()]

    capacity : int = int(input("Enter the maximum capacity of the knapsack : "))

    obj = Knapsack_II(profit, weight, capacity)
    fractional_knapsack_profit = obj.calculate_optimal_solution()
    non_fractional_knapsack_profit = obj.calculate_optimal_solution(False)

    print(f"\nMaximum Profit (Fraction of object NOT allowed) : {non_fractional_knapsack_profit}")
    print(f"Maximum Profit (Fraction of object allowed) : {round(fractional_knapsack_profit, 2)}")

if(__name__ == "__main__"):
    print()
    main()
    print()
