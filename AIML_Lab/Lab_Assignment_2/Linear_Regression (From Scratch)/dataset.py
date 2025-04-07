import csv

class Dataset:

    def __init__(self, path):
        self.dataset = []
        
        with open(path, "r") as f:
            reader = csv.reader(f)

            for row in reader:
                self.dataset.append(row)

    def get_row_count(self):
        return len(self.dataset)
    
    def get_column_count(self):
        return len(self.dataset[0])
    
    def get_X_y(self, lower_limit, upper_limit, column_lower_limit = 0):

        X = []
        y = []
        i = lower_limit
        while(i <= upper_limit):
            temp_X = []
            j = column_lower_limit
            while(j < len(self.dataset[i]) - 1):
                temp_X.append(float(self.dataset[i][j]))
                j += 1

            y.append(float(self.dataset[i][j]))            
            X.append(temp_X)

            i += 1

        return X, y
        
def main():
    df = Dataset(r"C:\Users\Dell\Desktop\Python_Tutorials\AIML_Lab\Lab_Assignment_2\Linear_Regression (From Scratch)\SOCR-HeightWeight.csv")
    print(df.get_row_count())
    print(df.get_column_count())

    # print(df.get_X_y(1, 5, 1))

if(__name__ == "__main__"):
    main()