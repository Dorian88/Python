import numpy as np
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import backend as K, optimizers
from sklearn.metrics import confusion_matrix
import matplotlib.pyplot as plt

from cargarDatos import cargarDatos

X_trainN, y_trainOHE, X_testN, y_test, input_dim, nb_classes = cargarDatos()

def weighted_categorical_crossentropy(weights):
    def loss_function(y_true, y_pred):
        y_pred = tf.clip_by_value(y_pred, K.epsilon(), 1 - K.epsilon())
        loss = -tf.reduce_mean(tf.reduce_sum(y_true * tf.math.log(y_pred) * weights, axis=1))
        return loss
    return loss_function

def get_model_custom(input_dim, nb_classes):
    model = Sequential([
        Dense(64, activation='relu', input_shape=(input_dim,)),
        Dense(32, activation='relu'),
        Dense(nb_classes, activation='softmax')
    ])
    return model

weights0 = np.array([1,1,1,1,1,1,1,1,1,1])
weights1 = np.array([1,1,1,1,1,1,4,1,1,1])
weights2 = np.array([1.5,1,1,1,1,1,4,1,1,1])

model = get_model_custom(input_dim, nb_classes)
sgd = optimizers.SGD(learning_rate=0.01, momentum=0.9, nesterov=True)
model.compile(loss=weighted_categorical_crossentropy(weights1), optimizer=sgd)

model.fit(X_trainN[:1000, :], y_trainOHE[:1000, :], epochs=10, batch_size=32, verbose=1)
preds = np.argmax(model.predict(X_testN, verbose=0), axis=1)

acc = np.mean(preds == y_test)
print(f"Accuracy = {acc*100:.2f}%")

# Matriz de confusión
cm = confusion_matrix(y_test, preds)
cm = cm / np.sum(cm, axis=1, keepdims=True)
plt.imshow(cm, cmap='Blues')
plt.title('Matriz de confusión normalizada')
plt.colorbar()
plt.show()