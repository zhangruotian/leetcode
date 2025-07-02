import numpy as np

def linear_regression_gradient_descent(
    X: np.ndarray, y: np.ndarray, alpha: float, iterations: int
):
    m, n = X.shape
    X_b = np.c_[np.ones((m, 1)), X]
    theta = np.zeros((n + 1, 1))
    losses = []
    y = y.reshape(-1, 1)
    for _ in range(iterations):
        pred = X_b @ theta
        diff = pred - y
        grad = (1 / m) * X_b.T @ diff
        theta -= alpha * grad
        loss = (1 / m) * (X_b @ theta - y).T @ (X_b @ theta - y)
        losses.append(loss.item())
    return theta.round(4).flatten().tolist(), losses

def linear_regression_gradient_descent_with_regularization(
    X: np.ndarray, y: np.ndarray, alpha: float, iterations: int, lambda_: float
):
    m, n = X.shape
    X_b = np.concatenate((np.ones((m, 1)), X), axis=1)
    theta = np.zeros((n + 1, 1))
    losses = []
    y = y.reshape(-1, 1)
    for _ in range(iterations):
        pred = X_b @ theta
        diff = pred - y
        theta_without_bias = np.copy(theta)
        theta_without_bias[0] = 0
        grad = (1 / m) * (X_b.T @ diff + lambda_ * theta_without_bias)
        theta -= alpha * grad
        loss = (1 / m) * (
            (X_b @ theta - y).T @ (X_b @ theta - y) + lambda_ * np.sum(theta[1:] ** 2)
        )
        losses.append(loss.item())
    return theta.round(4).flatten().tolist(), losses


# embed b in to theta.
# 正则化不作用于bias
