import numpy as np
from keras import datasets, utils
from sklearn.preprocessing import StandardScaler

def cargarDatos():
    (x_train, y_train), (x_test, y_test) = datasets.fashion_mnist.load_data()

    X_train = x_train.reshape(x_train.shape[0], -1)
    X_test = x_test.reshape(x_test.shape[0], -1)

    scaler = StandardScaler()
    X_trainN = scaler.fit_transform(X_train)
    X_testN = scaler.transform(X_test)

    y_trainOHE = utils.to_categorical(y_train)
    nb_classes = y_trainOHE.shape[1]
    input_dim = X_trainN.shape[1]

    return X_trainN, y_trainOHE, X_testN, y_test, input_dim, nb_classes