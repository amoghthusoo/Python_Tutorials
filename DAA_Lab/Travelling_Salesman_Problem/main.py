from copy import deepcopy

class Travelling_Salesman:
    
    def __init__(self, m):
        self.m = m
        
        self.reduce_matrix(self.m)
    
    def find_min_in_column(self, matrix, column):
        
        min_element = matrix[0][column]

        i = 1
        while(i < len(matrix)):

            if(matrix[i][column] < min_element):
                min_element = matrix[i][column]

            i += 1
        
        return min_element
        

    def reduce_matrix(self, matrix):
        
        matrix = deepcopy(matrix)

        i = 0
        while(i < len(matrix)):
            
            min_element = min(matrix[i])
            if(min_element == 0):
                i += 1
                continue
            
            j = 0
            while(j < len(matrix)):

                matrix[i][j] -= min_element

                j += 1
            
            i += 1
        

        j = 0
        while(j < len(matrix)):

            min_element = self.find_min_in_column(matrix, j)
            
            if(min_element == 0):
                j += 1
                continue
            
            i = 0
            while(i < len(matrix)):

                matrix[i][j] -= min_element

                i += 1
        
            j += 1
        
        return matrix

def main():
    
    inf = int(2 ** 31 -1)

    matrix = [
        [inf, 2, 3, 22, 1],
        [1, inf, 24, 2, 3],
        [3, 25, inf,3, 22],
        [2, 3, 1, inf, 24],
        [25, 22, 2, 1, inf]
    ]
    obj = Travelling_Salesman(matrix)

    


if(__name__ == "__main__"):
    print()
    main()
    print()
    