# kmeans
import numpy as np 
import matplotlib.pyplot as plt
class Kmeans:

    def __init__(self,k):
        self.k = k 

    def train(self,X,num_epochs):
        n,d = X.shape
        centorids = X[np.random.choice(n,self.k,replace=False)] #centorids(k,d)
        X = np.expand_dims(X,axis=1)# X(n,1,d)
        for _ in range(num_epochs):
            new_centroids = np.zeros_like(centorids)
            dists = np.linalg.norm(X-centorids,axis=2)  #(n,k)
            assign=np.argmin(dists,axis=1)#(n,)
            for i in range(self.k):
                if len(X[assign==i])>0:
                    new_centroids[i]=np.mean(X[assign==i],axis=0)
                else:
                    new_centroids[i] = centroids[i]

            if np.allclose(new_centroids,centorids):
                break
            centorids = new_centroids
        return centorids,assign

if __name__=='__main__':
    X1 = np.random.normal((2,2),1,(50,2))
    X2 = np.random.normal((0,0),1,(50,2))
    X3 = np.random.normal((-2,-2),1,(50,2))
    X = np.concatenate((X1,X2,X3),axis=0)
    model = Kmeans(3)
    _,assign=model.train(X,100)
    plt.scatter(X[:,0],X[:,1],c=assign)
    plt.show()
