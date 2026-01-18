import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input 

# -----------------------
# CONFIG
# -----------------------
IMG_SIZE = (524, 524) 
MODEL_PATH = "ecovision_ai_model.keras"

# Must match the training labels exactly
CLASS_NAMES = ['Cardboard', 'Food Organics', 'Glass', 'Metal', 'Miscellaneous Trash', 'Paper', 'Plastic', 'Textile Trash', 'Vegetation']

# Define which classes are biodegradable
BIODEGRADABLE_CLASSES = ['Food Organics', 'Vegetation', 'Paper', 'Cardboard']

# -----------------------
# LOAD MODEL
# -----------------------
@st.cache_resource
def load_model():
    return tf.keras.models.load_model(
        MODEL_PATH, 
        custom_objects={'preprocess_input': preprocess_input}
    )

model = load_model()

# -----------------------
# UI
# -----------------------
st.set_page_config(page_title="EcoVision AI", layout="centered", page_icon="🌱")
st.title("🌱 EcoVision AI: Smart Waste Classifier")
st.write("Identify waste types and check their environmental impact.")

uploaded_file = st.file_uploader("Upload an image of waste...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Image", use_container_width=True)

    # -----------------------
    # PREDICTION LOGIC
    # -----------------------
    with st.spinner('Analyzing material properties...'):
        # Resize and prepare for MobileNetV2
        img = image.resize(IMG_SIZE)
        img_array = np.array(img)
        img_array = np.expand_dims(img_array, axis=0)
        
        predictions = model.predict(img_array)
        probs = predictions[0]

        predicted_index = np.argmax(probs)
        predicted_class = CLASS_NAMES[predicted_index]
        confidence = probs[predicted_index] * 100

        # Determine Biodegradability
        is_biodegradable = predicted_class in BIODEGRADABLE_CLASSES

    # -----------------------
    # DISPLAY RESULTS
    # -----------------------
    st.markdown("---")
    
    # Category and Confidence metrics
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Detected Category", predicted_class)
    with col2:
        st.metric("Confidence", f"{confidence:.2f}%")

    # Biodegradability Status
    if is_biodegradable:
        st.success(f"✅ **This item is Biodegradable.** It can be decomposed by natural processes.")
    else:
        st.error(f"⚠️ **This item is Non-Biodegradable.** It should be recycled or disposed of carefully to prevent environmental harm.")

    # Detailed probability breakdown (Optional)
    with st.expander("See probability breakdown"):
        for i, class_name in enumerate(CLASS_NAMES):
            st.write(f"{class_name}: {probs[i]*100:.1f}%")