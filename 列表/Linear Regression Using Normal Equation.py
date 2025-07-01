import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
	# Your code here, make sure to round
    X = np.array(X)
    y = np.array(y)[:,np.newaxis]
    theta = np.linalg.inv(X.T@X)@X.T@y
    return np.round(theta.flatten(),4).tolist()
