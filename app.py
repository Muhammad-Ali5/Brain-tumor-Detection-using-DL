import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import os

# Set page configuration
st.set_page_config(page_title="Brain Tumor Classification", layout="wide")

# Title
st.title("Brain Tumor Classification")

# Load the trained model
@st.cache_resource
def load_classification_model():
    model = load_model('Brain tumor model.h5')
    return model

model = load_classification_model()

# Class labels
class_labels = ['glioma', 'meningioma', 'notumor', 'pituitary']

# File uploader
uploaded_file = st.file_uploader("Choose an MRI image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    col1, col2 = st.columns(2)
    
    with col1:
        st.image(uploaded_file, caption='Uploaded MRI Image', use_column_width=True)
        
    # Preprocess the image
    img = Image.open(uploaded_file)
    img = img.resize((150, 150))  # Resize to match the model's expected input size
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalize the image
    
    # Make prediction
    with col2:
        if st.button('Predict'):
            prediction = model.predict(img_array)
            predicted_class = class_labels[np.argmax(prediction)]
            confidence = np.max(prediction) * 100
            
            st.write('## Results')
            st.write(f'**Prediction:** {predicted_class}')
            st.write(f'**Confidence:** {confidence:.2f}%')
            
            # Display probability distribution
            st.write('### Probability Distribution')
            probabilities = prediction[0]
            for label, prob in zip(class_labels, probabilities):
                st.progress(float(prob))
                st.write(f'{label}: {float(prob)*100:.2f}%')
else:
    st.write("Please upload an MRI image for classification")