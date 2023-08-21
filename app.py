import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from keras.models import load_model

st.title("Project - Prediction of Probability of Default")
st.subheader("Classification Model for Loan Default Risk Prediction")
image = Image.open("ecg.jpg.webp")
st.image(image, use_column_width=True)


patient_name = st.text_input(label="Enter the name of Patient", value="")

ECG_data = st.file_uploader(label="Upload the patient's ECG Data")

if ECG_data is not None:
    st.write(f"Patient Name: {patient_name} has uploaded the ECG data in file {ECG_data.name}")
    data = pd.read_csv(ECG_data,header=None, delimiter="\t")
    data = np.array(data)
    if st.button(label="Predict the Type of Cardiovascular Disease"):
        reshape_ecg_data = data.reshape(1, data.shape[1], 1)
        model = load_model('baseline_1Dcnn_mitbih.h5')
        prediction = np.argmax(model.predict(reshape_ecg_data))
        print(prediction)
