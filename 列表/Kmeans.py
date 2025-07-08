import numpy as np
import matplotlib.pyplot as plt

def k_means_clustering(X,k,num_iter):
    n,d = X.shape
    centroids = X[np.random.choice(n, size=k, replace=False)]
    for _ in range(num_iter):
        distances = np.array([np.sqrt(((X-centroid)**2).sum(axis=1)) for centroid in centroids])
        assignments = np.argmin(distances,axis=0)
        
        loss=0
        for i in range(n):
            loss+=distances[assignments[i],i]
        print(loss)

        new_centroids = np.zeros((k,d))
        for i in range(k):
            cluster_points = X[assignments==i]
            if len(cluster_points)>0:
                new_centroids[i]=cluster_points.mean(0)
            else:
                new_centroids[i] = centroids[i]

        if np.all(centroids==new_centroids):
            break
            
        centroids = new_centroids
    return centroids, assignments

np.random.seed(0)
points_per_cluster = 50
cluster1 = np.random.randn(points_per_cluster, 2) + np.array([0, 0])
cluster2 = np.random.randn(points_per_cluster, 2) + np.array([8, 8])
cluster3 = np.random.randn(points_per_cluster, 2) + np.array([0, 10])
X = np.vstack([cluster1, cluster2, cluster3])
k = 3
num_iter = 100
final_centroids, final_assignments = k_means_clustering(X, k, num_iter)
plt.scatter(X[:, 0], X[:, 1], c=final_assignments)
plt.show()
