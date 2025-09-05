from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image
model = load_model('../models/mnist_cnn.keras')


def preprocessing_image(image):
    image = image.convert('L')
    image = image.resize((28, 28), Image.Resampling.LANCZOS)
    new_img = np.array(image)
    new_img = new_img / 255.0
    new_img = new_img.reshape(-1, 28, 28, 1)

    return new_img

def predict_digit(image):
    preprocessed_image = preprocessing_image(image)
    prediction = model.predict(preprocessed_image)
    predicted_class = np.argmax(prediction)
    return predicted_class