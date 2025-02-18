import streamlit as st
from helper import individualHelper
from helper.strings import title
import pandas as pd
from helper.styles import custom_css


st.set_page_config(layout="wide")
st.markdown(f"<h1 class='title''>{title}</h1>", unsafe_allow_html=True)
st.markdown(custom_css(), unsafe_allow_html=True)

col1, col2 = st.columns([1.8, 1])

data = None
patient = None

# Information
with col1:
    st.subheader("Patient Information")

    # Create form
    with st.form('Patient form', clear_on_submit=False):
        c1, c2, c3 = st.columns([1, 1, 1])

        # First column
        with c1:
            name = st.text_input("Patient name", value="John Connor")
            age = st.number_input("Patient age (29-71)", min_value=29, max_value=71)
            sex = st.selectbox("Patient gender", ['Female', 'Male'])
            cp = st.selectbox("Chest pain type", 
                (0, 1, 2, 3))
            tres = st.number_input("Resting blood pressure (94 to 200)", min_value=94, max_value=200)

        # Second column
        with c2:
            chol = st.number_input('Serum cholestoral in mg/dl (126-564)', min_value=126, max_value=564) 
            fbs = st.selectbox("Fasting blood sugar", (0, 1))
            res = st.selectbox("Resting electrocardiographic results", (0 ,1, 2))
            tha = st.number_input("Maximum heart rate (71 - 202)", min_value=71, max_value=202)
            exa = st.selectbox('Exercise induced angina: ',(0, 1))
        
        with c3:
            old = st.number_input('Oldpeak (0 - 6.2)', min_value=0.0, max_value=6.2)
            slope = st.selectbox('Slope of peak exercise', (0, 1, 2))
            ca = st.selectbox('Number of major vessels', (0,1, 2, 3, 4))
            thal = st.selectbox('Thal', (0, 1, 2, 3))

        submit = st.form_submit_button('Submit', type='primary')
        
        if submit:
            patient = name

            data = pd.DataFrame ({
                'age': [age],
                'sex': [1 if sex == "Male" else 0],
                'cp': [cp],
                'trestbps': [tres],
                'chol': [chol],
                'fbs': [fbs],
                'restecg': [res],
                'thalach': [tha],
                'exang': [exa],
                'oldpeak': [old],
                'slope': [slope],
                'ca': [ca],
                'thal': [thal]
            })


# Evaluation
with col2:
    # selected_model = st.session_state['model_type']
    st.subheader(f"Diagnosis ({st.session_state['model_type']})")

    # Predictions container
    with st.container(border=True):
        # Submit and predict
        result = individualHelper.submitAndPredict(patient, data)

        if not result:
            st.write("Submit data to continue.")
        else:
            patient, outcome, x_prob, y_prob, insights = result

            st.markdown(f'##### {outcome}')
            st.write('')

            col1, col2 = st.columns(2)
            with col1:
                st.metric('Estimated risk:', y_prob)

            with col2:
                st.metric('Estimated health:', x_prob)

    # Insights container
    if result:
        with st.container(border=True):
            st.subheader('Insights')
            for insight in insights:
                st.write(f"- {insight}")