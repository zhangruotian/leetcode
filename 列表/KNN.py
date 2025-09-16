# X_train (n,d) y_train (n,1) X_test(m,d) KNN
import numpy as np
from matplotlib import pyplot as plt
class KNN:
    def __init__(self,k):
        self.k = k 
        
    def train(self,X_train,y_train):
        self.X_train = X_train
        self.y_train = y_train
        self.n,self.d = X_train.shape 


    def euclidean_dist(self,X_train,X_test):
        X_test = X_test.reshape((self.m,1,self.d))
        return np.sum((X_train-X_test)**2,axis=2) 

    def row_mode(self,row):
        vals, counts = np.unique(row, return_counts=True)
        return vals[np.argmax(counts)]     

    def predict(self,X_test):
        self.m,_ = X_test.shape
        dists = self.euclidean_dist(self.X_train,X_test)
        top_k = np.argsort(dists,axis=1)[:self.m,:self.k] #m,k y_train (n,1
        preds = self.y_train[top_k].reshape((self.m,self.k))#m,k
        return np.apply_along_axis(self.row_mode, 1, preds)


X_0 = np.random.randn(10,2) + np.array([-2,-2])
y_0 = np.zeros((10,1))
X_1 = np.random.randn(10,2) + np.array([2,2])
y_1 = np.ones((10,1))
X_train = np.vstack((X_0,X_1))
y_train = np.vstack((y_0,y_1))
X = np.array([[-2,0],[2,0]])

model = KNN(3)
model.train(X_train,y_train)

y = model.predict(X)
y = y.reshape((-1,1))
print(y.shape)
X_draw = np.vstack((X_train,X))

y_draw = np.vstack((y_train,y))
plt.scatter(X_draw[:,0],X_draw[0:,1],c=y_draw.flatten())
plt.scatter(X[:,0],X[:,1],marker='x')
plt.show()
