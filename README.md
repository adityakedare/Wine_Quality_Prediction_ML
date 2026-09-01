# 🍷 Wine Quality Prediction using Machine Learning

## 📌 Project Overview

This project focuses on predicting the quality of wine based on its physicochemical properties using Machine Learning techniques.

The project performs data preprocessing, exploratory data analysis, model training, evaluation, and hyperparameter tuning to identify the best-performing model.

The final trained model is saved using Joblib and can be used for deployment.

---

## 🚀 Live Demo

🔗 **Try the Streamlit App:**  
[🍷 Wine Quality Prediction App](https://winequalitypredictionml-jriu4cbywalbbtxsrhzkei.streamlit.app/)

---

## 🎯 Problem Statement

The objective of this project is to predict wine quality based on its chemical properties.

The dataset contains features such as:

- Fixed Acidity
- Volatile Acidity
- Citric Acid
- Residual Sugar
- Chlorides
- Free Sulfur Dioxide
- Total Sulfur Dioxide
- Density
- pH
- Sulphates
- Alcohol

The wine quality is predicted using Machine Learning algorithms.

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-learn
- Joblib
- Streamlit

---

## 📊 Machine Learning Workflow

1. Data Collection
2. Data Understanding
3. Data Cleaning
4. Checking Missing Values
5. Handling Duplicate Records
6. Exploratory Data Analysis
7. Feature Engineering
8. Train-Test Split
9. Feature Scaling
10. Model Training
11. Model Evaluation
12. Model Comparison
13. Hyperparameter Tuning
14. Model Saving

---

## 🤖 Machine Learning Models

The following Machine Learning models were implemented:

### Regression Models

- Random Forest Regressor
- Support Vector Regressor
- Decision Tree Regressor

### Classification Models

- Random Forest Classifier
- Support Vector Machine (SVM)
- Logistic Regression
- Decision Tree Classifier

---

## 📈 Model Evaluation

### Regression Metrics

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- R² Score

### Classification Metrics

- Accuracy Score
- Precision
- Recall
- F1-Score
- Confusion Matrix

---

## ⚙️ Feature Engineering

Wine quality can be categorized into two classes:

- **0 → Bad Quality**
- **1 → Good Quality**

Example:

```python
df["quality_label"] = df["quality"].apply(
    lambda x: 0 if x <= 5 else 1
)
