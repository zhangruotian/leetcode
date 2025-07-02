import numpy as np
def linear_regression_closed_form(X: np.ndarray, y: np.ndarray) -> np.ndarray:
    m, n = X.shape
    X_b = np.concatenate((np.ones((m, 1)), X), axis=1)
    theta = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y.reshape(-1, 1)
    loss = (1 / m) * (X_b @ theta - y).T @ (X_b @ theta - y)
    return theta.round(4).flatten().tolist(), loss.item()
