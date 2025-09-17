import numpy as np
from matplotlib import pyplot as plt
# KNN  X_train(n,d) y_train(n,1) X_test(m,d)
class KNN:

    def __init__(self,k):
        self.k = k 
        
    def train(self,X_train,y_train):
        self.X_train = X_train
        self.y_train = y_train
        self.n,self.d = self.X_train.shape

    def row_counts(self,row):
        vals, counts = np.unique(row,return_counts=True)
        return vals[np.argmax(counts)]

    def predict(self,X_test):
        m,_ = X_test.shape 
        X_test = np.expand_dims(X_test,axis=1) #(m,1,d)
        dists = np.linalg.norm(self.X_train-X_test,axis=2) #(m,n,d)->(m,n)
        top_k = np.argsort(dists,axis=1)[:,:self.k] #(m,k)
        preds = self.y_train.flatten()[top_k] #(m,k)
        return np.apply_along_axis(self.row_counts,1,preds).reshape(-1,1)

if __name__ == '__main__':
    X_Train1 = np.random.normal(1,0.5,(100,2))
    X_Train2 = np.random.normal(-1,0.5,(100,2))
    y_Train1 = np.ones((100,1))
    y_Train2 = np.zeros((100,1))
    X_train = np.concatenate((X_Train1,X_Train2),axis=0)
    y_train = np.concatenate((y_Train1,y_Train2),axis=0)
    model = KNN(3)
    model.train(X_train,y_train)


    X_test = np.array([[1,1],[-1,-1]])
    preds = model.predict(X_test)


    X_draw = np.concatenate((X_train,X_test),axis=0)
    y_draw = np.concatenate((y_train,preds),axis=0)
    plt.scatter(X_draw[:,0],X_draw[:,1],c=y_draw.flatten())


    plt.scatter(X_test[:,0],X_test[:,1],marker='x')
    plt.show()


