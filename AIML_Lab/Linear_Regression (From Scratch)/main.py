from random import random

class Perceptron:

    def __init__(self, n : int) -> None:
        self.weights = [random() for _ in range(n)]
        self.bias = random()
        self.eta = 0.1

    def train(self, X : list[list[float]], y : list[float]):
        
        for outer_index, Xi in enumerate(X):

            for inner_index, xi in enumerate(Xi):
                h_hat += xi * self.weights[inner_index]
            
            h_hat += self.bias

            for inner_index, weight in enumerate(self.weights):
                self.weights[inner_index] = weight -  self.eta * (h_hat - y[outer_index])

            self.bias = self.bias - self.eta *  h_hat - y[outer_index]    

    def predict(self, Xi : list[float]) -> float:

        output = 0

        for index, weight in enumerate(self.weights):
            output += Xi[index] * weight

        output += self.bias

        return output

    def get_weights(self):
        return self.weights

def main():
 
    p = Perceptron(3)
    print(p.get_weights())

if(__name__ == "__main__"):
    main()