# Q4 :- All Pair Shortest Path

from copy import deepcopy

class All_Pair_Shortest_Path:

    def __init__(self, graph_matrix):
        self.D = graph_matrix
        self.P = [[-1 for _ in range(len(graph_matrix))] for _ in range(len(graph_matrix))]

    def find_path(self, start_node, end_node):
        self.start_node = start_node - 1
        self.end_node = end_node - 1

        self.construct()

        negative_cycle_nodes = []
        i = 0
        while(i < len(self.D)):
            
            if(self.D[i][i] < 0):
                negative_cycle_nodes.append(i)
            i += 1

        i = 0
        while(i < len(negative_cycle_nodes)):
            
            negative_cycle_nodes[i] += 1
            
            i += 1

        if(len(negative_cycle_nodes) > 0):
            print("\nFound negative cycle at node(s) : ", end = "")
            print(negative_cycle_nodes)
            return None
        else:
            return self.find_optimal_path()

    def construct(self):
        
        D_prev = deepcopy(self.D)

        d = 0
        while(d < len(self.D)):
            
            D_current = [[None for _ in range(len(self.D))] for _ in range(len(self.D))]
            
            i = 0
            while(i < len(self.D)):

                j = 0
                while(j < len(self.D)):

                    term1 = D_prev[i][j]
                    term2 = D_prev[i][d] + D_prev[d][j]

                    if(term2 < term1):
                        D_current[i][j] = term2
                        self.P[i][j] = d
                    else:
                        D_current[i][j] = term1


                    j += 1
                i += 1

            d += 1

            D_prev = deepcopy(D_current)

        self.D = deepcopy(D_prev)

        # print(D_prev)
        # print(self.P)
        

    def try_insert_node(self, path):
        
        i = 0
        while(i < len(path) - 1):
            
            inserted_node = self.P[path[i]][path[i + 1]]

            if(inserted_node != -1):
                path.insert(i + 1, inserted_node)
                return True
            
            i += 1

        return False

    def find_optimal_path(self):
        
        path = [self.start_node, self.end_node]

        while(self.try_insert_node(path)):
            pass
        
        path = [node + 1 for node in path]
        return path

def main():
    
    INF = int(2 ** 31)

    # D = [
    #     [0, 3, 8, INF, -4], 
    #     [INF, 0, INF, 1, 7],
    #     [INF, 4, 0, INF, INF],
    #     [2, INF, -5, 0, INF],
    #     [INF, INF, INF, 6, 0]
    # ]

    # D = [
    #     [0, -3, INF], 
    #     [-7, 0, 2],
    #     [INF, 5, 0]
    # ]

    D = []

    n = int(input("Enter the number of nodes : "))
    print()

    for i in range(n):
        row = input(f"Enter the weight, separated by spaces (Row : {i + 1}) : ")
        row = row.split(" ")
        temp = []
        for weight in row:
            if(weight != "INF"):
                temp.append(int(weight))
            else:
                temp.append(INF)
            
        D.append(temp)

    print()
    start_node = int(input("Enter the starting node : "))
    end_node = int(input("Enter the ending node : "))
    # print(D)

    obj = All_Pair_Shortest_Path(D)
    path = obj.find_path(start_node, end_node)

    if(path != None):
        print()
        print(f"Optimal Path : ", end = "")
        
        i = 0
        while(i < len(path)):
            print(path[i], end = "")

            if(i != len(path) - 1):
                print(" -> ", end = "")
            else:
                print()

            i += 1


if(__name__ == "__main__"):
    print()
    main()
    print()
