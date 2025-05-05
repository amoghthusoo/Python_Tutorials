from random import random
from dataset import Dataset

class Perceptron:

    def __init__(self, n : int) -> None:
        self.weights = [random() for _ in range(n)]
        self.bias = random()
        self.eta = 0.0001

    def train(self, X : list[list[float]], y : list[float]):
        
        for outer_index, Xi in enumerate(X):
            h_hat = 0
            for inner_index, xi in enumerate(Xi):
                h_hat += xi * self.weights[inner_index]
            
            h_hat += self.bias

            for inner_index, weight in enumerate(self.weights):
                self.weights[inner_index] = weight -  self.eta * (h_hat - y[outer_index]) * Xi[inner_index]
            self.bias -= self.eta * (h_hat - y[outer_index])    

    def predict(self, X : list[list[float]]) -> list[float]:
        
        predictions = []

        for Xi in X:

            output = 0
            for index, weight in enumerate(self.weights):
                output += Xi[index] * weight
            output += self.bias

            predictions.append(output)

        return predictions
    
    def calculate_mean_absolute_percentage_error(y_test, y_pred):

        summation = 0
        i = 0
        while(i < len(y_test)):
            summation += (abs(y_test[i] - y_pred[i]) / y_test[i] )
            i += 1

        return summation / len(y_test) * 100 

    def get_weights(self):
        return self.weights

def main():
 
    p = Perceptron(1)

    df = Dataset(r"C:\Users\Dell\Desktop\Python_Tutorials\AIML_Lab\Lab_Assignment_2\Linear_Regression (From Scratch)\SOCR-HeightWeight.csv")

    X_test, y_test = df.get_X_y(1, 20000, 1)
    X_train, y_train = df.get_X_y(20001, 25000, 1)

    # X_train = [[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]
    # y_train = [2.1, 4.0, 5.9, 8.2, 10.1, 12.2, 13.9, 16.1, 18.0, 19.8]
    # X_test = [[11], [12], [13]]
    # y_test = [22.2, 24.3, 26.1]


    p.train(X_train, y_train)
    y_pred = p.predict(X_test)

    error = Perceptron.calculate_mean_absolute_percentage_error(y_test, y_pred)
    print(f"Error : {error}")

if(__name__ == "__main__"):
    main()