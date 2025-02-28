# Breast-Cancer-Wisconsin-Diagnosis

## Project Overview

Breast Cancer Wisconsin Diagnosis is a machine learning application designed to predict whether a breast tumor is malignant or benign using the Wisconsin Breast Cancer dataset. Sourced from Kaggle, this dataset includes 569 samples with 30 features such as radius, texture, and smoothness, derived from digitized images of fine needle aspirates. The project employs a Logistic Regression model to perform binary classification, delivering reliable predictions based on these tumor characteristics.

Deployed on Streamlit, the application provides an intuitive interface where users can input tumor feature values and receive a diagnosis prediction instantly. This tool serves as an educational and research resource, showcasing the application of machine learning in medical diagnostics, though it is not intended for clinical use. The project aims to make breast cancer prediction accessible while demonstrating the effectiveness of Logistic Regression on a well-known healthcare dataset.

## Dataset Details

The dataset used is the Breast Cancer (Diagnostic) dataset, available from Kaggle. It contains 569 samples, each with 30 numerical features derived from digitized images of fine needle aspirates, including mean, standard error, and "worst" values for attributes like radius, texture, perimeter, area, smoothness, compactness, concavity, concave points, symmetry, and fractal dimension. The target variable indicates whether the tumor is Malignant (1) or Benign (0).

Number of Samples: 569
Number of Features: 30
Feature Examples: Radius, texture, perimeter, area, smoothness
Target Variable: Malignant (1) or Benign (0)

Dataset link: https://www.kaggle.com/datasets/rahmasleam/breast-cancer/data

## Model Details and Streamlit Deployment

Model Type: Logistic Regression.
Training Process: Feature selection, mean normalization.
Performance Metrics: Accuracy score.

Visit the app at .
Input fields will appear for features like radius, texture, etc..
Enter the values and click "Diagnosis Result" to see the result: "Malignant" or "Benign."

## Dependencies and Local Setup

Python 3.x
Streamlit
Scikit-learn
Pandas
NumPy

Step-by-step instructions:

Clone the repository: git clone https://github.com/AamishB/Breast-Cancer-Wisconsin-Diagnosis.git
Navigate to the project directory: cd Breast_Cancer_Wisconsin_Diagnosis
Install dependencies: pip install -r requirements.txt
Run the application: streamlit run app.py