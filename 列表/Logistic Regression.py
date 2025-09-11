# for one datapoint
# h(x) = sigmoid(xw)  L = -y*ln(h(x)) - (1-y)*ln(1-h(x))  dsig/dx = sig(x)(1-sig(x))
# dL/dw = dL/dh* dh/dsig * dsig/dw
# dL/dh = -y/h(x)+(1-y)/(1-h(x))
# dh/dsig = h(x)(1-h(x))
# dL/dh*dh/dsig = yh(x)-y-yh(x)+h(x) = h(x)-y
# dL/dh*dh/dsig* dsig/dw = (h(x)-y)*x

# for all data
# grad = X.T @ (sigmoid(X@theta)-y) pred = sigmoid(X@theta) diff = pred-y
# grad = 1/m * X.T @ diff
import numpy as np 
import matplotlib.pyplot as plt
class LogisticRegression:
    def __init__(self,X,y,theta=None,lambda_=0.01, lr=0.001):
        self.X = X #(n,d)
        self.X_b = np.concatenate((np.ones((X.shape[0],1)),X),axis=1)
        self.n,self.d = self.X_b.shape
        self.y = y
        self.theta = np.zeros((self.d,1))
        self.lambda_ = lambda_
        self.lr = lr 

    def train(self,num_epoch):
        for _ in range(num_epoch):
            pred = self.sigmoid(self.X_b@self.theta)
            diff = pred-y
            theta_w = np.copy(self.theta)
            theta_w[0][0]=0
            loss = 1/self.n*(np.sum(-1*np.log(pred[y==1])) + np.sum(-1*np.log(1-pred[y==0]))+self.lambda_*sum(theta_w**2))
            print(loss)
            grad = 1/self.n*(self.X_b.T@diff+self.lambda_ *theta_w)
            self.theta = self.theta - self.lr*grad

    def predict(self,x):
        x_b = np.concatenate((np.ones((1,1)),x),axis=1)
        prob = self.sigmoid(x_b@self.theta)[0][0]
        print(prob)
        return 1 if prob>=0.5 else 0

    def sigmoid(self,v):
        return 1/(np.exp(-1*v)+1)

if __name__ == '__main__':
    X0 = np.random.normal(size=(100,2))-1
    y0 = np.zeros((100,1))
    X1 = np.random.normal(size=(100,2))+1
    y1 = np.ones((100,1))
    X = np.concatenate((X0,X1),axis=0)
    y = np.concatenate((y0,y1),axis=0)
    model = LogisticRegression(X,y)
    model.train(10000)
    print(model.predict(np.array([[-1,-1]])))
    print(model.predict(np.array([[1,1]])))

    x0_line = np.linspace(-10,10,100)
    b,theta1,theta2 = model.theta
    # 在分割线上的data x，wx=0，因此有 b+x0*theta1+x1*theta2 = 0
    # 可计算出 x1 = (-b-x0*theta1)/theta2
    x1_line = (-b-x0_line*theta1)/theta2
    plt.plot(x0_line,x1_line)
    plt.scatter(X0[:,0],X0[:,1],color='red')
    plt.scatter(X1[:,0],X1[:,1],color='blue')
    plt.show()

