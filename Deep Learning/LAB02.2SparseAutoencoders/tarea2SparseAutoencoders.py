import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
import tensorflow as tf
from keras import Model, Input
from keras.layers import Dense

# =============================
# Cargar dataset MNIST reducido
# =============================
# Si no tienes el archivo, puedes descargarlo manualmente
# o usar el dataset original de Keras (comentado más abajo)

try:
    mnist = pd.read_csv("local/data/mnist1.5k.csv.gz", compression="gzip", header = None).values
    X = (mnist[:, 1:785] / 255.).astype(np.float32)
    y = (mnist[:, 0]).astype(int)
except:
    #Alternativa con el dataset de keras
    (X_train_full, _), (X_test_full, _) = tf.keras.datasets.mnist.load_data()
    X = np.concatenate([X_train_full, X_test_full])
    X = X.reshape(-1, 28*28) / 255.0
    y = np.zeros(len(X), dtype = int)

print("Dimensiones de las imágenes: ", X.shape)

X_train, X_test, _, _ = train_test_split(X, y, test_size = .2)
print("Train/Test: ", X_train.shape, X_test.shape)

# =====================
# Definición del modelo
# =====================

def get_model(input_dim, code_size, beta=.01):
    inputs = Input(shape=(input_dim,), name="input")
    encoder = Dense(code_size, activation='relu', name="encoder",
                    activity_regularizer=lambda x: beta * tf.reduce_mean(x))(inputs)
    outputs = Dense(input_dim, activation='sigmoid', name="decoder")(encoder)

    model = Model(inputs, outputs)
    model.compile(loss='mse', optimizer='adam')
    return model

# Crear y resumir el modelo
model = get_model(input_dim=X.shape[1], code_size=50, beta=0.05)
model.summary()

# ========================
# Entrenamiento del modelo
# ========================

print("\nEntrenando modelo (50 épocas)...")
model.fit(X_train, X_train, epochs=50, batch_size=32, verbose=1)

# ===================================
# Evaluar y visualizar reconstrucción
# ===================================

X_sample = np.random.permutation(X_test)[:10]
X_pred = model.predict(X_sample)

plt.figure(figsize=(20, 5))
for i in range(len(X_sample)):
    plt.subplot(2, len(X_sample), i + 1)
    plt.imshow(X_sample[i].reshape(28, 28), cmap=plt.cm.Greys_r)
    plt.axis("off")

    plt.subplot(2, len(X_sample), len(X_sample) + i + 1)
    plt.imshow(X_pred[i].reshape(28, 28), cmap=plt.cm.Greys_r)
    plt.axis("off")

plt.show()