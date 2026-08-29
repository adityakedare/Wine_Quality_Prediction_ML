import streamlit as st
import pandas as pd
import joblib

# -----------------------------
# Load the trained model
# -----------------------------
model = joblib.load("wine_quality_model.pkl")


# -----------------------------
# Page title
# -----------------------------
st.title("🍷 Wine Quality Prediction")

st.write(
    "Enter the wine's physicochemical properties "
    "to predict its quality."
)


# -----------------------------
# User Inputs
# -----------------------------

fixed_acidity = st.number_input(
    "Fixed Acidity",
    min_value=0.0,
    value=7.0
)

volatile_acidity = st.number_input(
    "Volatile Acidity",
    min_value=0.0,
    value=0.5
)

citric_acid = st.number_input(
    "Citric Acid",
    min_value=0.0,
    value=0.3
)

residual_sugar = st.number_input(
    "Residual Sugar",
    min_value=0.0,
    value=2.5
)

chlorides = st.number_input(
    "Chlorides",
    min_value=0.0,
    value=0.08
)

free_sulfur_dioxide = st.number_input(
    "Free Sulfur Dioxide",
    min_value=0.0,
    value=15.0
)

total_sulfur_dioxide = st.number_input(
    "Total Sulfur Dioxide",
    min_value=0.0,
    value=45.0
)

density = st.number_input(
    "Density",
    min_value=0.0,
    value=0.997
)

pH = st.number_input(
    "pH",
    min_value=0.0,
    value=3.3
)

sulphates = st.number_input(
    "Sulphates",
    min_value=0.0,
    value=0.6
)

alcohol = st.number_input(
    "Alcohol",
    min_value=0.0,
    value=10.0
)


# -----------------------------
# Prediction
# -----------------------------

if st.button("Predict Wine Quality"):

    input_data = pd.DataFrame({
        "fixed acidity": [fixed_acidity],
        "volatile acidity": [volatile_acidity],
        "citric acid": [citric_acid],
        "residual sugar": [residual_sugar],
        "chlorides": [chlorides],
        "free sulfur dioxide": [free_sulfur_dioxide],
        "total sulfur dioxide": [total_sulfur_dioxide],
        "density": [density],
        "pH": [pH],
        "sulphates": [sulphates],
        "alcohol": [alcohol]
    })

    prediction = model.predict(input_data)[0]

    # Display result
    if prediction == 1:
        st.success("🍷 Good Quality Wine")
    else:
        st.error("🍷 Bad Quality Wine")
        