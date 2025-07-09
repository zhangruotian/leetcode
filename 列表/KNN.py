# X_train (n,d) y_train (n,1) X(m,d)
import numpy as np
from collections import Counter
import matplotlib.pyplot as plt

class KNN:
    def __init__(self,k):
        self.k = k 

    def fit(self,X_train,y_train):
        self.X_train = X_train
        self.y_train = y_train

    def euclidean_dist(self,X):
        return np.sqrt(np.sum((self.X_train[:,np.newaxis,:] - X)**2,axis=2))

    def predict(self,X):
        distances = self.euclidean_dist(X).T 
        res = []
        for d in distances:
            most_close_k_index = np.argsort(d)[:self.k]
            most_close_k_class = self.y_train[most_close_k_index].flatten()
            counter = Counter(most_close_k_class)
            # implement tie-breaker
            tied_classes = []
            max_votes_count = counter.most_common()[0][1]
            for cat,c in counter.items():
                if c==max_votes_count:
                    tied_classes.append(cat)
            if len(tied_classes)==1:
                res.append(tied_classes[0])
            else:
                for cls in most_close_k_class:
                    if cls in tied_classes:
                        res.append(cls)
                        break

        return np.array(res).reshape(-1,1)

X_0 = np.random.randn(10,2) + np.array([-2,-2])
y_0 = np.zeros((10,1))
X_1 = np.random.randn(10,2) + np.array([2,2])
y_1 = np.ones((10,1))
X_train = np.vstack((X_0,X_1))
y_train = np.vstack((y_0,y_1))
X = np.array([[-2,0],[2,0]])

model = KNN(3)
model.fit(X_train,y_train)

y = model.predict(X)
X_draw = np.vstack((X_train,X))

y_draw = np.vstack((y_train,y))
plt.scatter(X_draw[:,0],X_draw[0:,1],c=y_draw.flatten())
plt.scatter(X[:,0],X[:,1],marker='x')
plt.show()







