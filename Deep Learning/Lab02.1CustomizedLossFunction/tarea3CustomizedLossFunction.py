import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense
from tensorflow.keras import regularizers, optimizers
from cargarDatos import cargarDatos

X_trainN, y_trainOHE, X_testN, y_test, input_dim, nb_classes = cargarDatos()

def get_L1L2_model(input_dim, nb_classes):
    reg = regularizers.L1L2(l1 = 0.001, l2 = 0.001)
    model = Sequential([
        Dense(128, activation='relu', kernel_regularizer=reg, input_shape=(input_dim,)),
        Dense(64, activation='relu', kernel_regularizer=reg),
        Dense(32, activation='relu', kernel_regularizer=reg),
        Dense(16, activation='relu', kernel_regularizer=reg),
        Dense(nb_classes, activation='softmax')
    ])
    return model

model = get_L1L2_model(input_dim, nb_classes)
sgd = optimizers.SGD(learning_rate=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd)

model.fit(X_trainN[:500, :], y_trainOHE[:500, :], epochs=100, batch_size=16, verbose=1)
preds = np.argmax(model.predict(X_testN, verbose=0), axis=1)

accuracy = np.mean(preds == y_test)
print(f"Accuracy = {accuracy*100:.2f}%")