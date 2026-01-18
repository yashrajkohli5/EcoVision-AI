# 🌱 EcoVision AI: Smart Waste Classification System

EcoVision AI is a deep learning-based application designed to automate the process of waste sorting. By leveraging computer vision and transfer learning, the system identifies various types of waste from images and determines their biodegradability to promote better recycling habits.

## 🚀 Features
- **High-Accuracy Classification**: Uses a fine-tuned MobileNetV2 model to classify waste into 9 categories.
- **Environmental Impact Analysis**: Automatically determines if an object is Biodegradable or Non-Biodegradable.
- **Interactive GUI**: A user-friendly Streamlit web application for real-time image uploads and predictions.
- **Optimized Performance**: Implements TensorFlow data pipelines with prefetching and autotuning for efficient processing.

## 📊 Dataset
Link: https://archive.ics.uci.edu/dataset/908/realwaste
The model is trained on the **RealWaste** dataset, which contains images across 9 distinct classes:
- Cardboard
- Food Organics
- Glass
- Metal
- Miscellaneous Trash
- Paper
- Plastic
- Textile Trash
- Vegetation

## 🛠️ Tech Stack
- **Language**: Python
- **Deep Learning**: TensorFlow, Keras
- **Computer Vision**: MobileNetV2 (Transfer Learning)
- **Web Framework**: Streamlit
- **Data Handling**: NumPy, Pandas, PIL

## 📂 Project Structure
```text
├── Dataset/RealWaste/       # Raw image data organized by class
├── app.py                   # Streamlit application GUI
├── data_loader.py           # Data pipeline and preprocessing logic
├── model_builder.py         # Transfer learning model architecture
├── train.py                 # Model training and saving script
├── ecovision_ai_model.keras # Trained model file
└── README.md                # Project documentation
