def linear_regression_gradient_descent(
    X: np.ndarray, y: np.ndarray, alpha: float, iterations: int
) -> np.ndarray:
    m, n = X.shape
    # Using X_b to avoid overwriting the original X variable, which is useful for plotting.
    X_b = np.concatenate((np.ones((m, 1)), X), axis=1)
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

# embed b in to theta.
