import numpy as np
from scipy.optimize import minimize

def operation(X, y, W, b):
    relu = lambda x: x*(x>0)
    return np.mean((relu(X @ W + b) - y)**2) # @ se usa para la multiplicación matricial

if __name__ == "__main__":
    X = np.array([[-0.09348275, -0.17182042, -0.29143506],
                  [0.34581753, 0.37816707, 0.39850916],
                  [0.23478876, -0.07832256, 0.10793716],
                  [-0.1746856, -0.10240038, -0.27959607]])

    y = np.array([[-0.47312685],
                  [0.42086142],
                  [0.44194868],
                  [0.46536898]])

    W = np.array([[0.12650597],
                  [0.49952987],
                  [0.34470552]])

    b = -0.02

    print("Resultado: ", operation(X, y, W, b))