import numpy as np
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
    m, n = X.shape
    theta = np.zeros((n, 1))
    y = y.reshape(-1,1)
    for _ in range(iterations):
        L = (X @ theta - y).T @ (X @ theta - y)
        gradient = (1 / m) * X.T @ (X @ theta - y)
        theta -= alpha * gradient
    return theta
