import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv("data.csv")

data_x = data["x"].to_numpy()
data_y = data["y"].to_numpy()


def loss_function_MSE(m, b, data_x, data_y):
    predictions = m * data_x + b
    MSE = np.mean((predictions - data_y) ** 2)

    return MSE


class Linear_Regression:
    def __init__(self, learning_rate=0.0001, n_iterations=100):
        self.learning_rate = learning_rate
        self.n_iterations = n_iterations
        self.m = 0
        self.b = 0

    def forward(self, x):
        return self.m * x + self.b

    def train_one_epoch(self, data_x, data_y):
        loss = loss_function_MSE(self.m, self.b, data_x, data_y)
        predictions = self.m * data_x + self.b
        error = predictions - data_y

        del_by_m = 2 * np.mean(error * data_x)
        del_by_b = 2 * np.mean(error)

        self.m = self.m - self.learning_rate * del_by_m
        self.b = self.b - self.learning_rate * del_by_b

        print(f"Loss: {loss:.4f}")
        print(f"y = {self.m:.4f}x + {self.b:.4f}")
        self.plot(data_x, data_y)

    def plot(self, data_x, data_y):
        x_line = np.linspace(0, 60, 1000)
        y_line = self.m * x_line + self.b

        plt.figure(figsize=(8, 5))
        plt.scatter(data_x, data_y, color="blue", label="Scatter Points", s=50)
        plt.plot(x_line, y_line, color="red", label="y = 2x + 1", linewidth=2)
        plt.show()


model = Linear_Regression()
model.train_one_epoch(data_x, data_y)
