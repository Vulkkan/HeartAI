import joblib
import datetime
import pandas as pd
import streamlit as st


rf = joblib.load('models/ensembleModel.pkl')
lr = joblib.load('models/lr_classifier.pkl')

model = lr

# Select model based on session state
if 'model_type' in st.session_state:
    model = rf if st.session_state['model_type'] == 'Random Forest' else lr


date = datetime.date(2025, 1, 3)
formatted_date = date.strftime("%a %-d %b , %Y")


expected_columns = ['age', 'trestbps', 'chol', 'thalach', 'oldpeak', 'sex_0', 'sex_1', 'cp_0', 'cp_1', 'cp_2', 'cp_3', 'fbs_0', 'fbs_1', 'restecg_0', 'restecg_1', 'restecg_2', 'exang_0', 'exang_1', 'slope_0', 'slope_1', 'slope_2', 'ca_0', 'ca_1', 'ca_2', 'ca_3', 'ca_4', 'thal_0', 'thal_1', 'thal_2', 'thal_3']


def encode(input_df):
    input_df = pd.get_dummies(input_df, columns = ['sex', 'cp', 'fbs', 'restecg', 'exang', 'slope', 'ca', 'thal'])

    # Ensure all expected columns are present
    for col in expected_columns:
        if col not in input_df.columns:
            input_df[col] = 0  

    input_df = input_df[expected_columns]

    return input_df


def encodeBatch(df):
    applicants = df['Name'].tolist()
    df = df.drop(columns=['Name'])

    for col in expected_columns:
        if col not in df.columns:
            df[col] = 0

    df = df[expected_columns]

    return applicants, df