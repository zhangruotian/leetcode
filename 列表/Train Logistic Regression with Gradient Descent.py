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
        loss = -np.sum(y * np.log(pred) + (1 - y) * np.log(1 - pred))
        losses.append(loss.round(4).tolist())
        diff = pred - y
        grad = X.T @ diff
        theta -= learning_rate * grad
    return np.round(theta, 4).flatten().tolist(),losses


def sigmoid(v: np.ndarray) -> np.ndarray:
    return 1 / (1 + np.exp(-v))

