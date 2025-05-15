class Day_Finder:
    
    def __init__(self, date, month, year) -> None:
        self.REFERENCE : list = [1, 1, 1950, 1]
        self.date : int = date
        self.month : int = month
        self.year : int = year

        return None

    def brute_force(self) -> list:

        while True:
            #print(self.REFERENCE)
            
            if self.REFERENCE[0] == self.date and self.REFERENCE[1] == self.month and self.REFERENCE[2] == self.year:
                break

            self.REFERENCE[0] += 1
            if self.REFERENCE[1] in [4,6,9,11] and self.REFERENCE[0] == 31:
                self.REFERENCE[0] = 1
                self.REFERENCE[1] += 1
            
            if self.REFERENCE[1]  not in [4,6,9,11] and self.REFERENCE[0] == 32:
                self.REFERENCE[0] = 1
                self.REFERENCE[1] += 1

            if self.REFERENCE[1] == 2 and self.REFERENCE[2] % 4 == 0 and self.REFERENCE[0] == 30:
                self.REFERENCE[0] = 1
                self.REFERENCE[1] += 1

            if self.REFERENCE[1] == 2 and self.REFERENCE[2] % 4 != 0 and self.REFERENCE[0] == 29:
                self.REFERENCE[0] = 1
                self.REFERENCE[1] += 1

            if self.REFERENCE[1] == 13:
                self.REFERENCE[1] = 1
                self.REFERENCE[2] += 1

            self.REFERENCE[3] += 1

            if self.REFERENCE[3] == 8:
                self.REFERENCE[3] = 1

        return self.REFERENCE[3]        

def main():
    date : int = int(input("\nEnter date : "))
    month : int = int(input("Enter month : "))
    year : int = int(input("Enter year : "))

    obj = Day_Finder(date, month, year)
    day_number = obj.brute_force()

    days_dict : dict = {1 : 'Sunday', 2 : 'Monday', 3 : 'Tuesday', 4 : 'Wednesday', 5 : 'Thursday', 6 : 'Friday', 7 : 'Saturday'}

    print("\n" + days_dict[day_number] + "\n")

if __name__ == "__main__":
    main()