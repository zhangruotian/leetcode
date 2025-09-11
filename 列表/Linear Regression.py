# y = X@w   L=1/n*(X@w-y).T@(X@w-y)+1/n*w.T@w  L = (w.T@X.T -y.T)(X@w-y)=w.T@X.T@X@w-2y.T@X@w = 
# dL/dw = X.T@X@w-X.T@y = X.T(X@w-y)
# I = 0 0 0
#   = 0 1 0
#   = 0 0 1
import numpy as np
import matplotlib.pyplot as plt 
class LinearRegression:
    def __init__(self,X,y,lr=0.01,lambda_=0.1,epochs=100):
        self.X = X
        self.y = y 
        self.X_b = np.concatenate((np.ones((self.X.shape[0],1)),X),axis = 1)
        self.n,self.d = self.X_b.shape
        self.theta =  np.zeros((self.d,1))
        self.lr = lr 
        self.lambda_ = lambda_
        self.epochs = epochs

    def closed_form(self):
        I = np.eye(self.d)
        I[0][0]=0
        self.theta = np.linalg.inv(self.X_b.T@self.X_b+self.lambda_*I)@self.X_b.T@y


    def train(self):
        for _ in range(self.epochs):
            pred = self.X_b@self.theta
            diff = pred-self.y
            theta_w = np.copy(self.theta)
            theta_w[0][0]=0
            loss = 1/self.n*(diff.T@diff + np.sum(self.lambda_*theta_w**2))
            grad = 1/self.n*(self.X_b.T@diff + self.lambda_*theta_w)
            self.theta -= self.lr*grad

    def predict(self,X):
        X_b = np.concatenate((np.ones((X.shape[0],1)),X),axis = 1)
        a = X_b@self.theta 
        return X_b@self.theta 

if __name__ == '__main__':
    X = np.linspace(-10,10,100)
    y = 2*X+np.random.normal(size=100)
    plt.scatter(X,y)

    model = LinearRegression(X.reshape(100,1),y.reshape(100,1))
    model.closed_form()
    pred_y = model.predict(X.reshape(100,1))
    plt.plot(X,pred_y.flatten(),color='red')

    model = LinearRegression(X.reshape(100,1),y.reshape(100,1))
    model.train()
    pred_y = model.predict(X.reshape(100,1))
    plt.plot(X,pred_y.flatten(),color='green')
    
    plt.show()
