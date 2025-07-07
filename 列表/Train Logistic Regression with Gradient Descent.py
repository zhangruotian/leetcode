import matplotlib.pyplot as plt
import numpy as np

class LogisicRegression:
    def __init__(self, X, y, lambda_, num_epochs, lr):
        self.X = X
        self.y = y.reshape(-1, 1)
        self.n, self.d = X.shape
        self.X_b = np.concatenate((np.ones((self.n, 1)), self.X), axis=1)
        self.theta = np.zeros((self.d + 1, 1))
        self.lambda_ = lambda_
        self.num_epochs = num_epochs
        self.lr = lr

    def train(self):
        for _ in range(self.num_epochs):
            pred = self.sigmoid(self.X_b @ self.theta)
            loss = (1 / self.n) * (
                -np.sum(self.y * np.log(pred)) - np.sum((1 - self.y) * np.log(1 - pred))
            ) + (1 / self.n) * self.lambda_ * np.sum(self.theta[1:] ** 2)
            print(loss)
            diff = pred - self.y
            theta_w = np.copy(self.theta)
            theta_w[0, 0] = 0
            grad = (1 / self.n) * (self.X_b.T @ diff) + (
                1 / self.n
            ) * self.lambda_ * theta_w
            self.theta -= self.lr * grad

    def sigmoid(self, v):
        return 1 / (1 + np.exp(-1 * v))

    def predict(self, data):
        data = np.concatenate((np.ones((data.shape[0], 1)), data), axis=1)
        pred = self.sigmoid(data @ self.theta)
        return np.round(pred)


if __name__ == "__main__":
    np.random.seed(42)  # 使用种子确保每次运行结果一致
    num_points = 100
    X0 = np.random.randn(num_points,2)-1
    y0 = np.zeros((num_points,1))
    X1 = np.random.randn(num_points,2)+1
    y1 = np.ones((num_points,1))
    X_train = np.vstack((X0,X1))
    y_train = np.vstack((y0,y1))
    model = LogisicRegression(X_train,y_train,0.1,1000,0.01)
    model.train()
    plt.scatter(X0[:,0],X0[:,1],color = 'blue')
    plt.scatter(X1[:,0],X1[:,1],color = 'red')
    x0_line = np.linspace(-10,10,100)
    b,theta1,theta2 = model.theta
    # b+theta1*x0+theta2*x1 = 0
    x1_line = (-b-theta1*x0_line)/theta2
    plt.plot(x0_line,x1_line)
    plt.show()
