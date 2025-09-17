import numpy as np
from matplotlib import pyplot as plt
class Kmeans:
    def __init__(self,k):
        self.k = k 

    def train(self,X,num_steps):
        n,d = X.shape
        centroids = X[np.random.choice(n,self.k,replace=False)] #centroids (k,d)
        X_expanded = np.expand_dims(X,axis=1) #X(n,1,d)
        for _ in range(num_steps):
            new_centroids = np.zeros_like(centroids)
            dists = np.linalg.norm(X_expanded-centroids,axis=2) # dists (n,k)
            assign = np.argmin(dists,axis=1) #assign (n,)

            for i in range(self.k):
                new_centroids[i] = np.mean(X[assign==i],axis=0)

            if np.all(centroids==new_centroids):
                break
            centroids = new_centroids
        return assign,centroids

if __name__ == '__main__':
    X1 = np.random.normal(5,0.5,(50,2))
    X2 = np.random.normal(0,0.5,(50,2))
    X3 = np.random.normal(-5,0.5,(50,2))
    X = np.concatenate((X1,X2,X3),axis=0)
    model = Kmeans(3)
    assign,_=model.train(X,100)
    print(assign)
    plt.scatter(X[:,0],X[:,1],c=assign.flatten())
    plt.show()


 
