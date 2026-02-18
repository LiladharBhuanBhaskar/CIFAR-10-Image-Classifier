import numpy as np
import tensorflow as tf
from sklearn.metrics import confusion_matrix, classification_report
from data_utils import load_cifar10

class_names = [
    "airplane","automobile","bird","cat","deer",
    "dog","frog","horse","ship","truck"
]

if __name__ == "__main__":
    (_, _), (x_test, y_test) = load_cifar10()

    model = tf.keras.models.load_model("saved_model/cifar10_model.h5")

    y_pred = model.predict(x_test)
    y_pred_classes = np.argmax(y_pred, axis=1)
    y_true = y_test.flatten()

    print("\nClassification Report:\n")
    print(classification_report(y_true, y_pred_classes, target_names=class_names))

    cm = confusion_matrix(y_true, y_pred_classes)
    print("\nConfusion Matrix:\n")
    print(cm)
