# Q10 :- Assignment Problem

from copy import deepcopy
from math import pow


class Assignment_Problem:

    def __init__(self):
        self.INF = int(pow(2, 31))

    def blacklist_column(self, cost_matrix_copy : list[list[int]], minimum_cost_index : int):
        
        j = minimum_cost_index
        i = 0
        while(i < len(cost_matrix_copy)):

            cost_matrix_copy[i][j] = self.INF
            i += 1

    def calculate_total_cost(self, temp_assignment : list[list[int | list[int | None]]]):
        
        cost = 0
        for element in temp_assignment:
            cost += element[0]

        return cost
    
    def sort_by_person(self, minimum_cost_assignment : list[list[int | list[int]]]):

        i : int = 0
        while(i < len(minimum_cost_assignment) - 1):
            
            j : int = 0
            while(j < len(minimum_cost_assignment) - 1 - i):

                if(minimum_cost_assignment[j][1][0] > minimum_cost_assignment[j + 1][1][0]):
                    minimum_cost_assignment[j], minimum_cost_assignment[j + 1] = minimum_cost_assignment[j + 1], minimum_cost_assignment[j] 

                j += 1
            i += 1

    def assign_jobs(self, cost_matrix : list[list[int]]):

        minimum_cost_assignment = [[self.INF, [None, None]] for _ in range(len(cost_matrix))]
        
        for i in range(len(cost_matrix)):
            
            cost_matrix_copy = deepcopy(cost_matrix)
            temp_assignment = []

            j = i
            while(True):

                minimum_cost = min(cost_matrix_copy[j])

                minimum_cost_index = cost_matrix[j].index(minimum_cost)
                temp_assignment.append([minimum_cost, [j, minimum_cost_index]])
                
                self.blacklist_column(cost_matrix_copy, minimum_cost_index)
                
                j = (j + 1) % len(cost_matrix)

                if(j == i):
                    break

            if(self.calculate_total_cost(temp_assignment) < self.calculate_total_cost(minimum_cost_assignment)):
                minimum_cost_assignment = deepcopy(temp_assignment)

        self.sort_by_person(minimum_cost_assignment)
        return minimum_cost_assignment
        
def main():

    n : int = int(input("Enter the number of jobs or person : "))
    cost_matrix : list[list[int]] = []

    print()
    for i in range(n):
        temp_costs : str = input(f"Enter the costs for {n} jobs for Person {i + 1}, separated by spaces : ")
        temp_costs = [int(cost) for cost in temp_costs.split()]
        cost_matrix.append(temp_costs)

    obj = Assignment_Problem()
    minimum_cost_assignment : list[list[int | list[int]]] = obj.assign_jobs(cost_matrix)
    minimum_cost : int = obj.calculate_total_cost(minimum_cost_assignment)

    
    print(f"\nMinimized total cost of Assignment : {minimum_cost}")
    print("\nAssignment :\n")
    for cost in minimum_cost_assignment:
        print(f"Person : {cost[1][0] + 1} is assignment Job : {cost[1][1] + 1} with cost : {cost[0]}")


if(__name__ == "__main__"):
    print()
    main()
    print()
