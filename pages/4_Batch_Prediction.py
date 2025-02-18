import streamlit as st
import pandas as pd
from helper import batchHelper
from helper.strings import title
from helper.styles import custom_css


st.set_page_config(layout="wide")
st.markdown(custom_css(), unsafe_allow_html=True)

st.markdown(f"<h1 class='title''>{title}</h1>", unsafe_allow_html=True)

batch_data = batchHelper.batch_data
results = None

col1, col2 = st.columns([2, 3])

# (Column) Upload
with col1:
    st.subheader('Upload')

    input_dataset = st.file_uploader('Upload a CSV file containing patients data', type=['csv'])
    if input_dataset is not None:
        batch_data = pd.read_csv(input_dataset)
        # Get results
        results = batchHelper.submitAndPredictBatch(batch_data)

# (Column) Patients
with col2:
    if batch_data is not None:

        # Patients dataframe
        st.subheader('Patients')
        if input_dataset:
            st.dataframe(batch_data, hide_index=False, use_container_width=True, height=170)

# Predictions
if results:
    cx, cy = st.columns([1, 2])

    with cx:
        st.subheader(f'Actions')

        for result in results:
            best_patients = [p for p in results if p["Y_Probability"] < 40]  # Health above 60%
            worst_patients = [p for p in results if p["Y_Probability"] > 60]  # Health below 40%

        def display_patients(title, patients):
            with st.expander(title, expanded=True):
                if patients:
                    for patient in patients:
                        st.write(f'**{patient["Patient"]}**: {patient["Y_Probability"]:.2f}% risk detected')
                else:
                    st.write("No patients in this category.")

        display_patients('Healthy patients can be evacuated', best_patients)
        display_patients('Immediate attention required for these patients', worst_patients)


    with cy:
        st.subheader(f'Diagnosis')
        
        for result in results:
            # Expander for each patient
            with st.expander(f'Patient: {result["Patient"]}' , expanded=True):
                

                c1, c2, c3 = st.columns([3, 1, 1])
                with c1:
                    st.markdown(f'#### {result["Prediction"]}')
                    
                with c2:
                    st.metric("Estimated risk:", f'{result["Y_Probability"]:.2f}%')

                with c3:
                    st.metric("Estimated health:", f'{result["X_Probability"]:.2f}%')
                with st.popover('Insights'):
                    for insight in result["Insights"]:
                        st.write(f"- {insight}")
        