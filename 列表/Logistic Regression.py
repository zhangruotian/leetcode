# logistic regression
# p(x)=sig(wx) dp/dw = sig(wx)(1-sig(wx))*x = p(x)(1-p(x))x
# L = -y*ln(p(x))-(1-y)*ln(1-p(x))
# dL/dw = -y/p(x) *dp/dw+(1-y)/1-p(x)*dp/dw = -y(1-p(x))+(1-y)p(x)= p(x)y-y-p(x)y+p(x)=x(p(x)-y) = x(pred-y)=x(diff)
import numpy as np
import matplotlib.pyplot as plt

class LogisticRegression:

    def __init__(self,X,y,lambda_,lr):
        self.n,_ = X.shape
        self.X_b = np.concatenate((np.ones((self.n,1)),X),axis=1) 
        _,self.d = self.X_b.shape
        self.y = y 
        self.theta = np.ones((self.d,1))
        self.lambda_=lambda_
        self.lr = lr 

    def train(self, num_epoch):
        for _ in range(num_epoch):
            pred = self.sigmoid(self.X_b@self.theta)
            diff = pred-self.y  #diff(n,1)
            theta_w = np.copy(self.theta)
            theta_w[0,0]=0
            grad = 1/self.n*(self.X_b.T@diff+self.lambda_*theta_w)
            self.theta -= self.lr*grad
            loss1 = np.sum(-1*np.log(pred[self.y==1]))
            loss0 = np.sum(-1*np.log(1-pred[self.y==0]))
            loss = 1/self.n*(loss0+loss1)+0.5/self.n*(self.lambda_*theta_w.T@theta_w)
            print(loss)

    def sigmoid(self,v):
        # v(n,1)
        return 1/(1+np.exp(-1*v))

    def predict(self,X):
        X_b = np.concatenate((np.ones((X.shape[0],1)),X),axis=1) 
        preds = self.sigmoid(X_b@self.theta)
        return 1 if np.squeeze(preds)>=0.5 else 0

if __name__ == '__main__':
    X_1 = np.random.normal((1,1),1,(100,2))
    y_1 = np.ones((100,1))
    X_2 = np.random.normal((-1,-1),1,(100,2))
    y_2 = np.zeros((100,1))
    X = np.concatenate((X_1,X_2),axis=0)
    y = np.concatenate((y_1,y_2),axis=0)
    plt.scatter(X_1[:,0],X_1[:,1],color='blue')
    plt.scatter(X_2[:,0],X_2[:,1],color='green')
    model=LogisticRegression(X,y,0.1,0.01)
    model.train(1000)
    xline_1 = np.linspace(-2,2,100)
    xline_2=(-model.theta[0,0] - model.theta[1,0] * xline_1) / model.theta[2,0]
    plt.plot(xline_1,xline_2)

    X_test = np.array([[1,1]])
    print(model.predict(X_test))
    plt.show()
