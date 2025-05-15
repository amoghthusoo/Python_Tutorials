# Program to find the day when date, month and year are given
# NOTE :- The program can handle all types of exceptions.

import calendar as cl
import time as tm
class Day_Finder:

    def __init__(self, date, month, year) -> None:
        
        self.date : int = date
        self.month : int = month
        self.year : int = year
        self.day_dict = {
            0 : "Monday",
            1 : "Tuesday",
            2 : "Wednesday",
            3 : "Thusrday",
            4 : "Friday",
            5 : "Saturday",
            6 : "Sunday"
        }

        return None

    def find_day(self) -> str | int:
        
        try: 
            day_num : int = cl.weekday(self.year, self.month, self.date)
            day_name : str = self.day_dict[day_num]
            return day_name
        except:
            return -1
    
    def calculate_processing_time(self, start_time, end_time) -> float:

        processing_time = start_time - end_time
        return processing_time

def main() -> None:

    date : int = int(input("\nEnter date : "))
    month : int = int(input("Enter month : "))
    year : int = int(input("Enter year : "))

    start_time : float = tm.time()

    obj = Day_Finder(date, month, year)
    day : str = obj.find_day()

    end_time : float = tm.time()

    if (day != -1):
        for i in range(1, 11 + len(day)):
            print("-", end = "")
        print("\n| Day : " + day + " |")
        for i in range(1, 11 + len(day)):
            print("-", end = "")
        print("\nProcessing Time :", obj.calculate_processing_time(start_time, end_time))
    else:
        print("\nINVALID INPUT\n")
        print("Processing Time :", obj.calculate_processing_time(start_time, end_time))
    
    return None

if __name__ == "__main__":
    main()
    print()