def linear_regression_closed_form(X: np.ndarray, y: np.ndarray):
    m, n = X.shape
    X_b = np.concatenate((np.ones((m, 1)), X), axis=1)
    theta = np.linalg.inv(X_b.T @ X_b) @ X_b.T @ y.reshape(-1, 1)
    loss = (1 / m) * (X_b @ theta - y).T @ (X_b @ theta - y)
    return theta.round(4).flatten().tolist(), loss.item()


def linear_regression_closed_form_with_regularization(
    X: np.ndarray, y: np.ndarray, lambda_: float
):
    m, n = X.shape
    X_b = np.concatenate((np.ones((m, 1)), X), axis=1)
    I = np.eye(n + 1)
    I[0, 0] = 0
    theta = (
        np.linalg.inv(X_b.T @ X_b + lambda_ * I) @ X_b.T @ y.reshape(-1, 1)
    )
    loss = (1 / m) * (
        (X_b @ theta - y).T @ (X_b @ theta - y) + lambda_ * np.sum(theta[1:] ** 2)
    )
    return theta.round(4).flatten().tolist(), loss.item()


# embed b into theta.
# regularization 不作用于bias
