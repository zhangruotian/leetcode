import numpy as np 
import matplotlib.pyplot as plt 
# L = (X@w-y).T@(X@w-y)+w.T@w = (w.T@X.T-y.T)@(X@w-y)+w.T@w = w.T@X.T@X@w-2*w.T@X.T@y+y.T@y +w.T@w

# dL/dw = 2(X.T@X)w-2*(X.T@y)+2Iw = 0
# grad:
# (X.T@X)w-*(X.T@y)=X.T@(X@w-y) = X.T@(pred-y) = X.T@diff + lambda*w 

# close form:
# w = inv(X.T@X+lambda*I)@(X.T@y)

class LinearRegression:

    def __init__(self,X,y,lambda_,lr):
        self.n,_ = X.shape
        self.lambda_ = lambda_
        self.X_b = np.concatenate((np.ones((self.n,1)),X),axis=1) 
        _,self.d = self.X_b.shape
        self.y = y 
        self.theta = np.zeros((self.d,1))
        self.lr = lr 

    def closed_form(self):
        I = np.eye(self.d)
        I[0,0]=0
        self.theta = np.linalg.inv(self.X_b.T@self.X_b+self.lambda_*I)@self.X_b.T@self.y

    def train(self,num_epoch):
        for _ in range(num_epoch):
            pred = self.X_b@self.theta
            diff = pred-y
            w_reg = np.copy(self.theta)
            w_reg[0,0]=0
            grad = 1/self.n * (self.X_b.T@diff+self.lambda_*w_reg)  
            self.theta -= self.lr*grad
            loss = 1/self.n*(diff.T@diff+self.lambda_*w_reg.T@w_reg)
            print(loss)

    def predict(self,X):
        X_b = np.concatenate((np.ones((X.shape[0],1)),X),axis = 1)
        return X_b@self.theta

if __name__=='__main__':
    X = np.linspace(-10,10,100)
    y = 2*X 
    noise = np.random.randn(100)
    y = y+noise
    plt.scatter(X,y)
    X = np.expand_dims(X,axis=1) #X(100,1)
    y = np.expand_dims(y,axis=1) #y(100,1)
    model = LinearRegression(X,y,0.1,0.01)
    # model.closed_form()
    # preds = model.X_b@model.theta
    model.train(10)
    preds = model.predict(X)
    plt.plot(X,preds.flatten(),color='red')
    plt.show()
