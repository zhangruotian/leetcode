import numpy as np

def train_logreg(
    X: np.ndarray, y: np.ndarray, learning_rate: float, iterations: int
) -> tuple[list[float], ...]:
    """
    Gradient-descent training algorithm for logistic regression, optimizing parameters with Binary Cross Entropy loss.
    """
    m, n = X.shape
    X = np.concatenate((np.ones((m, 1)), X), axis=1)
    y = y.reshape(-1, 1)
    theta = np.zeros((n+1, 1))
    losses = []
    
    for _ in range(iterations):
        pred = sigmoid(X @ theta)
        diff = pred - y
        grad = (1/m)*X.T @ diff
        theta -= learning_rate * grad
        loss = (1/m)*(-np.sum(y * np.log(pred) + (1 - y) * np.log(1 - pred)))
        losses.append(loss.round(4).tolist())
    return np.round(theta, 4).flatten().tolist(),losses

def logistic_regression_gradient_descent_with_regularization(
    X: np.ndarray, y: np.ndarray, learning_rate: float, iterations: int, lambda_: float
):
    m, n = X.shape
    X = np.concatenate((np.ones((m, 1)), X), axis=1)
    y = y.reshape(-1, 1)
    theta = np.zeros((n+1, 1))
    losses = []
    
    for _ in range(iterations):
        pred = sigmoid(X @ theta)
        loss = (1/m)*(-np.sum(y * np.log(pred) + (1 - y) * np.log(1 - pred)) + lambda_ * np.sum(theta[1:] ** 2))
        losses.append(loss.round(4).tolist())
        
        diff = pred - y
        theta_without_bias = np.copy(theta)
        theta_without_bias[0] = 0
        grad = (1/m)*(X.T @ diff + lambda_ * theta_without_bias)
        theta -= learning_rate * grad

    return np.round(theta, 4).flatten().tolist(),losses

def sigmoid(v: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-v))
