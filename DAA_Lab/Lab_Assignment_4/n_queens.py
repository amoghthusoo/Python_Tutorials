# Q3 :- N-Queen Problem

import copy

class Board:

    def __init__(self, board_size : int) -> None:
        self.board_size = board_size        
        self.board = [[False for _ in range(board_size)] for _ in range(board_size)]

        self.stack = []
        self.visited_list = []


    def mark_vacancies(self, queen_position : list[int]) -> None:

        # 4. west       
        row : int = queen_position[0]
        column : int = queen_position[1]

        while(column >= 0):

            if(self.board[row][column] not in [True, None]):
                self.board[row][column] = True
            column -= 1

        # 5. east
        row : int = queen_position[0]
        column : int = queen_position[1]

        while(column < self.board_size):

            if(self.board[row][column] not in [True, None]):
                self.board[row][column] = True
            column += 1
        
        # 6. south-west
        row : int = queen_position[0]
        column : int = queen_position[1]

        while(row < self.board_size and column >= 0):

            if(self.board[row][column] not in [True, None]):
                self.board[row][column] = True
            row += 1
            column -= 1

        # 7. south
        row : int = queen_position[0]
        column : int = queen_position[1]

        while(row < self.board_size):

            if(self.board[row][column] not in [True, None]):
                self.board[row][column] = True
            row += 1
        
        # 8. south-east    
        row : int = queen_position[0]
        column : int = queen_position[1]

        while (row < self.board_size and column < self.board_size):

            if(self.board[row][column] not in [True, None]):
                self.board[row][column] = True
            row += 1
            column += 1

    def find_vacancies(self, row_number) -> list[int]:
        
        vacancy_list = []

        i = 0
        while(i < self.board_size):
            if(not self.board[row_number][i]):
                vacancy_list.append(i)
            
            i += 1

        return vacancy_list

    def find_positions_n_queens(self) -> list[list[int]]:

        if(self.board_size in [2, 3]):
            print("\nSolution doesn't exist.")
            return None
        
        elif(self.board_size <= 0):
            print("\nINVALID INPUT!")
            return None
        
        solution = []
        current_row = 0
        solution_count = 1
        
        print()
        while(True):

            
            temp_vacancy_list = self.find_vacancies(current_row)    
            
            if(len(temp_vacancy_list) != 0):
                
                queen_pos = temp_vacancy_list.pop(0)
                self.visited_list.append(queen_pos)
                
                self.board[current_row][queen_pos] = None
                self.mark_vacancies([current_row, queen_pos])
                
                self.stack.append({"row_num" : current_row, "board" : copy.deepcopy(self.board), "visited_list" : copy.deepcopy(self.visited_list)})
                
                self.visited_list = []
                
                if(current_row < self.board_size - 1):
                    current_row += 1
                
                else:

                    print(f"Solution {solution_count} : ", end="")
                    self.print_solution(self.extract_queen_positions())

                    solution_count += 1
                    
                    temp_dict = self.stack.pop()
                    
                    
                    current_row = temp_dict["row_num"]
                    queen_pos = temp_dict["board"][current_row].index(None)

                    self.board = copy.deepcopy(temp_dict["board"])
                    self.visited_list = copy.deepcopy(temp_dict["visited_list"])
                    self.sync_board(current_row, queen_pos)
            
            else:

                try:
                    temp_dict = self.stack.pop()
                except:
                    return
                
                current_row = temp_dict["row_num"]
                queen_pos = temp_dict["board"][current_row].index(None)

                self.board = copy.deepcopy(temp_dict["board"])
                self.visited_list = copy.deepcopy(temp_dict["visited_list"])
                self.sync_board(current_row, queen_pos)

    def print_solution(self, positions):
        
        i = 0
        while(i < len(positions)):
        
            print(f"{positions[i] + 1} ", end="")        
            i += 1
        print()

    def extract_queen_positions(self):
        
        queen_positions = []

        i = 0
        while(i < self.board_size):

            j = 0
            while(j < self.board_size):

                if(self.board[i][j] == None):
                    queen_positions.append(j)
                j += 1
            i += 1
            
        return queen_positions
            
               
    def sync_board(self, current_row, queen_pos):
        
        i = current_row
        while(i < self.board_size):

            j = 0
            while(j < self.board_size):

                self.board[i][j] = False

                j += 1
            i += 1

        i = 0
        while(i < current_row):

            queen_pos_temp = self.board[i].index(None)
            self.mark_vacancies([i, queen_pos_temp])

            i += 1

        self.board[current_row][queen_pos] = True

        for index in self.visited_list:
            self.board[current_row][index] = True
    

def main():
    
    size = int(input("Enter the size of board : "))
    b = Board(size)
    b.find_positions_n_queens()

if(__name__ == "__main__"):
    print()
    main()
    print()
