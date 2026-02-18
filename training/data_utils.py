import tensorflow as tf
from tensorflow.keras.datasets import cifar10

def load_cifar10():
    (x_train, y_train), (x_test, y_test) = cifar10.load_data()

    # Normalize images to [0,1]
    x_train = x_train.astype("float32") / 255.0
    x_test = x_test.astype("float32") / 255.0

    return (x_train, y_train), (x_test, y_test)
