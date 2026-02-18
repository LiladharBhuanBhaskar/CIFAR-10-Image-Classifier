import tensorflow as tf

MODEL_PATH = "backend/model/cifar10_model.h5"

model = tf.keras.models.load_model(MODEL_PATH)
