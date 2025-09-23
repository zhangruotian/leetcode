# KNN
import numpy as np 
import matplotlib.pyplot as plt 
class KNN:

    def __init__(self,k,X,y):
        self.k = k 
        self.X = X #X(n,d)
        self.n,self.d = X.shape
        self.y = y #y(n,1)

    def predict(self,X_test):
        
        X_test=np.expand_dims(X_test,1) # X_test(m,1,d)
        dists = np.linalg.norm(X_test-self.X,axis=2) #(m,n)
        k_neighbors = np.argsort(dists,axis=1)[:,:self.k] #(m,k)
        classes=self.y.flatten()[k_neighbors]#(m,k)
        return np.apply_along_axis(self.count,1,classes)#(m,)

    def count(self,v):
        vals,cnts=np.unique(v,return_counts=True)
        return vals[np.argmax(cnts)]

if __name__ == '__main__':
    X1 = np.random.normal((1,1),1,(50,2))
    X2 = np.random.normal((-1,-1),1,(50,2))
    y1 = np.ones((50,1))
    y2 = np.zeros((50,1))
    X = np.concatenate((X1,X2),axis=0)
    y = np.concatenate((y1,y2),axis=0)
    model = KNN(4,X,y)
    X_test = np.array([[1,1],[-1,-1]])
    preds = np.expand_dims(model.predict(X_test),1)
    X_plot = np.concatenate((X,X_test),axis=0)
    y_plot = np.concatenate((y,preds),axis=0)
    plt.scatter(X_plot[:,0],X_plot[:,1],c=y_plot.flatten())
    plt.scatter(X_test[:,0],X_test[:,1],marker='x')
    plt.show()

