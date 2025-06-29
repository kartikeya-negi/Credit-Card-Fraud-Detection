import streamlit as st
import numpy as np
import joblib

st.set_page_config(page_title="Credit Card Fraud Detection", layout="wide")
st.title("💳 Credit Card Fraud Detection")

st.write(
    "Enter transaction details below (features V1–V28 and Amount) to predict if a transaction is fraudulent."
)

# List of features as per your notebook
feature_columns = [
    'Time',  
    'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10',
    'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18', 'V19', 'V20',
    'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount'
]


# Input fields for all features
user_input = []
cols = st.columns(3)
for idx, feature in enumerate(feature_columns):
    with cols[idx % 3]:
        val = st.number_input(f"{feature}", value=0.0, format="%.5f")
        user_input.append(val)

# Load the trained model
@st.cache_resource
def load_model():
    return joblib.load("model.pkl")

model = load_model()

if st.button("Predict"):
    input_array = np.array([user_input])
    prediction = model.predict(input_array)
    if prediction[0] == 1:
        st.error("⚠️ This transaction is predicted to be FRAUDULENT.")
    else:
        st.success("✅ This transaction is predicted to be LEGITIMATE.")
