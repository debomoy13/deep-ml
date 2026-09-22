import numpy as np
def sgd_update(X: np.ndarray, y: np.ndarray, weights: np.ndarray, learning_rate: float, n_iter: int) -> list:
    """
    Perform n_iter steps of stochastic gradient descent on a linear regression
    model with MSE loss, cycling through samples in order.

    Returns the final weight vector as a Python list.
    """
    loss1=1000
    best_weight=0
    for i in range(n_iter):
        x=X[i%len(X)]
        y_i=y[i%len(y)]
        loss=((x @ weights)-y_i)**2
        gradient=2*(((x @ weights)- y_i)*x)
        weights=weights - learning_rate*gradient
        
    return weights.flatten()


    pass
