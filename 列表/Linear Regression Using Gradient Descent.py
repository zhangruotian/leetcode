import matplotlib.pyplot as plt
import numpy as np


class LinearRegression:
    def __init__(self,X,y,num_iterations,lr,lambda_):
        self.X = X
        self.y = y
        self.n, self.d = self.X.shape
        self.X_b = np.concatenate((np.ones((self.n,1)),self.X),axis = 1)
        self.theta_b = np.zeros((self.d+1,1))
        self.num_iterations = num_iterations
        self.lr = lr
        self.lambda_  = lambda_

    def compute_closed_form(self):
        I = np.eye(self.d+1)
        I[0][0] = 0
        self.theta_b = np.linalg.inv(self.X_b.T@self.X_b+self.lambda_ * I)@self.X_b.T@self.y

    def train(self):
        for _ in range(self.num_iterations):
            pred = self.X_b@self.theta_b
            diff = pred-self.y
            loss = (1/self.n)*diff.T @ diff + (1/self.n)*np.sum(self.lambda_*(self.theta_b[1:]**2))
            print(loss)     
            theta_w = np.copy(self.theta_b)
            theta_w[0][0] = 0
            grad = (1/self.n)*(self.X_b.T@diff+self.lambda_*theta_w)
            self.theta_b -= self.lr*grad


    def predict(self,data):
        data_b = np.concatenate((np.ones((data.shape[0],1)),data),axis = 1)
        return data_b@self.theta_b


X = np.linspace(-10,10,100)
y = 2*X+np.random.randn(100)
plt.scatter(X,y)
X = X.reshape(-1,1)
y = y.reshape(-1,1)
model = LinearRegression(X,y,1000,0.01,0.1)
model.train()
# model.compute_closed_form()
print(model.theta_b)
ploty = np.concatenate((np.ones((X.shape[0],1)),X),axis = 1)@model.theta_b
plt.plot(X.flatten(),ploty.flatten())
plt.show()

