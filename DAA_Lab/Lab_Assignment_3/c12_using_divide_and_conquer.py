# Q2 :- C12 Using Divide and Conquer

class Strassens_Matix:

    def divide_matrix(self, matrix: list[list[int]], part: int) -> list[list[int]]:

        size: int = len(matrix) // 2
        out_matrix: list[list[int]] = [
            [0 for _ in range(size)] for _ in range(size)]

        if (part == 1):

            i: int = 0
            x: int = 0
            while (i < size):

                j: int = 0
                y: int = 0
                while (j < size):

                    out_matrix[x][y] = matrix[i][j]

                    j += 1
                    y += 1

                i += 1
                x += 1

        elif (part == 2):
            i = 0
            x = 0
            while (i < size):

                j = size
                y = 0
                while (j < len(matrix)):

                    out_matrix[x][y] = matrix[i][j]

                    j += 1
                    y += 1

                i += 1
                x += 1

        elif (part == 3):

            i = size
            x = 0
            while (i < len(matrix)):

                j = 0
                y = 0
                while (j < size):

                    out_matrix[x][y] = matrix[i][j]

                    j += 1
                    y += 1

                i += 1
                x += 1

        else:

            i = size
            x = 0
            while (i < len(matrix)):

                j = size
                y = 0
                while (j < len(matrix)):

                    out_matrix[x][y] = matrix[i][j]

                    j += 1
                    y += 1

                i += 1
                x += 1

        return out_matrix

    def add_matrix(self, matrix1: list[list[int]], matrix2: list[list[int]], sub_mode: bool = False) -> list[list[int]]:

        out_matrix: list[list[int]] = [
            [0 for _ in range(len(matrix1))] for _ in range(len(matrix1))]

        i: int = 0
        while (i < len(matrix1)):

            j: int = 0
            while (j < len(matrix1)):

                if (not sub_mode):
                    out_matrix[i][j] = matrix1[i][j] + matrix2[i][j]
                else:
                    out_matrix[i][j] = matrix1[i][j] - matrix2[i][j]
                j += 1
            i += 1

        return out_matrix

    def multiply_matrix(self, matrix1: list[list[int]], matrix2: list[list[int]]) -> list[list[int]]:

        if (len(matrix1) == 2):

            D: int = (matrix1[0][0] + matrix1[1][1]) * \
                (matrix2[0][0] + matrix2[1][1])
            E: int = (matrix1[1][0] + matrix1[1][1]) * matrix2[0][0]
            F: int = (matrix1[0][0]) * (matrix2[0][1] - matrix2[1][1])
            G: int = (matrix1[1][1]) * (matrix2[1][0] - matrix2[0][0])
            H: int = (matrix1[0][0] + matrix1[0][1]) * (matrix2[1][1])
            M: int = (matrix1[1][0] - matrix1[0][0]) * \
                (matrix2[0][0] + matrix2[0][1])
            P: int = (matrix1[0][1] - matrix1[1][1]) * \
                (matrix2[1][0] + matrix2[1][1])

            c11: int = D + G - H + P
            c12: int = F + H
            c21: int = E + G
            c22: int = D + F - E + M

            out_matrix: list[list[int]] = [[c11, c12], [c21, c22]]

            return out_matrix

        else:

            A11: list[list[int]] = self.divide_matrix(matrix1, 1)
            A12: list[list[int]] = self.divide_matrix(matrix1, 2)
            B12: list[list[int]] = self.divide_matrix(matrix2, 2)
            B22: list[list[int]] = self.divide_matrix(matrix2, 4)

            F: list[list[int]] = self.multiply_matrix(A11, self.add_matrix(B12, B22, True))
            H: list[list[int]] = self.multiply_matrix(self.add_matrix(A11, A12), B22)

            c12: list[list[int]] = self.add_matrix(F, H)

            return c12

    def display_matrix(self, matrix: list[list[int]]) -> None:

        i: int = 0
        while (i < len(matrix)):

            j: int = 0
            while (j < len(matrix)):

                print(matrix[i][j], end=" ")

                j += 1

            print()
            i += 1


def main():

    mat1 = [[0 for _ in range(4)] for _ in range(4)]
    mat2 = [[0 for _ in range(4)] for _ in range(4)]

    i = 0
    while(i < 4):

        row = input(f"Enter the elements of row {i + 1} of matrix 1 (4X4), separated by spaces : ")
        row = row.split()

        j = 0
        while(j < 4):
            
            mat1[i][j] = int(row[j])
            j += 1

        i += 1
    
    print()
    i = 0
    while(i < 4):

        row = input(f"Enter the elements of row {i + 1} of matrix 2 (4X4), separated by spaces : ")
        row = row.split()

        j = 0
        while(j < 4):
            
            mat2[i][j] = int(row[j])
            j += 1

        i += 1

    ob = Strassens_Matix()
    print()
    print("C12 is given by : ")
    print()
    C12 = ob.multiply_matrix(mat1, mat2)

    ob.display_matrix(C12)

if (__name__ == "__main__"):
    print()
    main()
    print()
