from tensorflow.keras.models import load_model
import numpy as np
from PIL import Image

model = load_model('/Users/khinmyatnoe/PycharmProjects/finalproject/app/trained_plant_disease_model.keras')
class_names=['Apple___Apple_scab', 'Apple___Black_rot', 'Apple___Cedar_apple_rust', 'Apple___healthy', 'Blueberry___healthy', 'Cherry_(including_sour)___Powdery_mildew', 'Cherry_(including_sour)___healthy', 'Corn_(maize)___Cercospora_leaf_spot Gray_leaf_spot', 'Corn_(maize)___Common_rust_', 'Corn_(maize)___Northern_Leaf_Blight', 'Corn_(maize)___healthy', 'Grape___Black_rot', 'Grape___Esca_(Black_Measles)', 'Grape___Leaf_blight_(Isariopsis_Leaf_Spot)', 'Grape___healthy', 'Orange___Haunglongbing_(Citrus_greening)', 'Peach___Bacterial_spot', 'Peach___healthy', 'Pepper,_bell___Bacterial_spot', 'Pepper,_bell___healthy', 'Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy', 'Raspberry___healthy', 'Soybean___healthy', 'Squash___Powdery_mildew', 'Strawberry___Leaf_scorch', 'Strawberry___healthy', 'Tomato___Bacterial_spot', 'Tomato___Early_blight', 'Tomato___Late_blight', 'Tomato___Leaf_Mold', 'Tomato___Septoria_leaf_spot', 'Tomato___Spider_mites Two-spotted_spider_mite', 'Tomato___Target_Spot', 'Tomato___Tomato_Yellow_Leaf_Curl_Virus', 'Tomato___Tomato_mosaic_virus', 'Tomato___healthy']

def preprocess_image(image_path, target_size):
    image = Image.open(image_path).resize(target_size)
    image = np.array(image, dtype=np.float32)
    image = np.expand_dims(image, axis=0)  # Add batch dimension
    return image

def predict_disease(image_path):
    input_shape = model.input_shape[1:3]
    image = preprocess_image(image_path, input_shape)
    predictions = model.predict(image)  # Use Keras model to predict
    predicted_class_index = np.argmax(predictions)
    confidence = np.max(predictions)

    # Assuming 'class_names' is defined somewhere, adjust as needed
    predicted_class_name = class_names[predicted_class_index]

    return predicted_class_name, confidence