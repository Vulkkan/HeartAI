import pandas as pd
import streamlit as st
from helper.strings import title
from helper.styles import custom_css


st.set_page_config(layout="wide")
st.markdown(custom_css(), unsafe_allow_html=True)
st.markdown(
    f"<h1 class='title''>{title}</h1>", unsafe_allow_html=True
)


st.subheader("Your Information")

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
        tres = st.number_input("Resting blood pressure: Between 94 to 200", min_value=94, max_value=200)

    # Second column
    with c2:
        chol = st.number_input('Serum cholestoral in mg/dl: Between 126 to 564') 
        fbs = st.selectbox("Fasting blood sugar", (0, 1))
        res = st.selectbox("Resting electrocardiographic results", (0 ,1, 2))
        tha = st.number_input("Maximum heart rate achieved (71 - 202)")
        exa = st.selectbox('Exercise induced angina: ',(0, 1))
    
    with c3:
        old = st.number_input('Oldpeak (0 - 6.2)', min_value=0.0, max_value=6.2)
        slope = st.selectbox('Slope of peak exercise ST segmen', (0, 1, 2))
        ca = st.selectbox('Number of major vessels', (0,1, 2, 3, 4))
        thal = st.selectbox('Thal', (0, 1, 2, 3))

    submit = st.form_submit_button('Submit', type='primary')

    if submit:
        input_data = pd.DataFrame({
            'Name': [name],
            'age': [age],
            'sex': [1 if sex == "Male" else 0],
            'cp': [int(cp)], 
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

        try:
            existing_data = pd.read_csv('input-data/heart.csv')

            existing_data = pd.concat([existing_data, input_data], axis=0). reset_index(drop=True)

            existing_data.to_csv('input-data/heart.csv', index=False)

            st.success('Information has been saved successfully!')
        except Exception as e:
            st.error(f'Error: {e}')