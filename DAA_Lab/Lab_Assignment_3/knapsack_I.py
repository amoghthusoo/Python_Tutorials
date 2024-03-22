# Q6 :- Knapsack - I

class Knapsack_I:

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

    def sort_by_non_increasing_order_of_profit(self):
        
        i : int = 0
        while(i < len(self.profit) - 1):

            j : int = 0
            while(j < len(self.profit) - 1 - i):

                if(self.profit[j] < self.profit[j + 1]):

                    self.profit[j], self.profit[j + 1] = self.profit[j + 1], self.profit[j]
                    self.weight[j], self.weight[j + 1] = self.weight[j + 1], self.weight[j]
                    
                j += 1
            i += 1

    def fill_knapsack(self) -> float:

        weight : float = 0
        profit : float = 0

        i : int = 0
        while(i < len(self.profit)):

            if(weight == self.capacity):
                return profit

            elif(weight + self.weight[i] <= self.capacity):
                profit += self.profit[i]
                weight += self.weight[i]

            else:
                profit += ((self.capacity - weight)/self.weight[i]) * self.profit[i] 
                weight = self.capacity

            i += 1

        return profit
    
    def calculate_ratio(self):
        self.sort_by_profit_weight_ratio()
        p1 = self.fill_knapsack()
        
        self.sort_by_non_increasing_order_of_profit()
        p2 = self.fill_knapsack()

        return p1 / p2

def main():
    
    profit : str = input("Enter the profit of objects, separated by spaces : ")
    profit : list[int] = [int(e) for e in profit.split()]
    
    weight : str = input("Enter the weight of objects, separated by spaces : ")
    weight : list[int] = [int(e) for e in weight.split()]

    capacity : int = int(input("Enter the maximum capacity of the knapsack : "))

    obj = Knapsack_I(profit, weight, capacity)
    ratio = obj.calculate_ratio()
    print(f"\nThe ratio [F*(I)/F(I)] is given by : {round(ratio, 2)}")
    print("\nwhere, F*(I) is the value of the optimal solution, and")
    print("where, F(I) is the value of the solution when objects are input in non-increasing order of profit's.")



if(__name__ == "__main__"):
    print()
    main()
    print()
    