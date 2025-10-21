import numpy as np

def apply_autoencoder(Xin, We, be, Wd, bd, beta = 0.05):
    """
    Calcula la salida y pérdida de un autoencoder disperso implementado manualmente.
    todos los argumentos son arreglos numpy
    """

    sigm = lambda z: 1 / (1 + np.exp(-z))
    relu = lambda z: z * (z > 0)

    eX = Xin @ We + be
    rX = relu(eX)
    dX = rX @ Wd + bd
    Xout = sigm(dX)

    m, n = Xin.shape
    _, c = We.shape

    rec_error = np.sum((Xin - Xout) ** 2) / (m * n)
    sparsity_penalty = np.sum(rX) / (m * c)
    loss = rec_error + beta * sparsity_penalty

    return Xout, loss

# --------------------------------------------
# Prueba del autoencoder con los valores dados
# --------------------------------------------
if __name__ == "__main__":
    Xin = np.array([
        [-0.37035694, -0.34542735,  0.15605706, -0.33053004],
        [-0.3153002 , -0.41249585,  0.30073246,  0.13771319],
        [-0.30017424, -0.15409659, -0.43102843,  0.38578104],
        [-0.14914677, -0.4411987 , -0.33116959, -0.32483895],
        [-0.17407847,  0.0946155 , -0.48391975,  0.34075492]
    ])

    We = np.array([
        [-0.28030543, -0.46140969, -0.18068483],
        [ 0.31530074,  0.29354581, -0.30835241],
        [-0.35849794, -0.12389752, -0.01763293],
        [ 0.44245022, -0.4465276 , -0.40293482]
    ])

    be = np.array([0.33030961, 0.33221543, -0.32828997])
    Wd = np.array([
        [ 0.42964391, -0.22892199,  0.09340045,  0.25372971],
        [-0.41209546, -0.23107885, -0.28591832,  0.15998353],
        [-0.16731707, -0.10630373, -0.15786946, -0.20899463]
    ])
    bd = np.array([0.32558449, 0.31610265, -0.25844944, 0.28249571])

    Xout, loss = apply_autoencoder(Xin, We, be, Wd, bd)

    print("=== RESULTADOS AUTOENCODER MANUAL ===")
    print("Xout: \n", np.round(Xout, 6))
    print("Loss: ", loss)