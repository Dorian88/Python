import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def argmax(f):
    return float(minimize(lambda x: -f(x[0]), [0], method="BFGS").x[0])

if __name__ == "__main__":
    def A(x):
        return -(x - 1)**2

    B = lambda x: -(x + 2)**4

    print("El resultado A(x): ", argmax(A))
    print("El resultado B(x): ", argmax(B))

    x = np.linspace(-6, 4, 100)

    plt.figure(figsize=(10, 2))
    plt.subplot(121)
    plt.plot(x, [A(val) for val in x])
    plt.title("A(x)")

    plt.subplot(122)
    plt.plot(x, [B(val) for val in x])
    plt.title("B(x)")

    plt.show()