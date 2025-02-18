import streamlit as st
from helper.styles import custom_css

# Page Configuration
st.set_page_config(layout="wide", page_icon="⚙️")
st.markdown(custom_css(), unsafe_allow_html=True)

# Title
st.markdown(
    "<h1 class='title'>Configuration</h1> <br><br>",
    unsafe_allow_html=True
)

# Initialize session state variables if they don't exist
if 'model_type' not in st.session_state:
    st.session_state['model_type'] = 'Random Forest'  
if 'prediction_type' not in st.session_state:
    st.session_state['prediction_type'] = 'Single Patient'

# Layout for selection
col1, col2 = st.columns([1, 1])

with col1:
    st.markdown("### 🔍 Model Selection")
    with st.container():
        model_type = st.radio(
            "Choose model:",
            ['Random Forest', 'Logistic Regressor'],
            index=1 if st.session_state['model_type'] == 'Logistic Regressor' else 0
        )
        st.session_state['model_type'] = model_type
        st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown("### 📊 Prediction Type")
    with st.container():
        prediction_type = st.radio(
            "Choose prediction type:",
            ['Single Patient', 'Multiple Patients'],
            index=0 if st.session_state['prediction_type'] == 'Single Patient' else 1
        )
        st.session_state['prediction_type'] = prediction_type
        st.markdown('</div>', unsafe_allow_html=True)

# Spacing before button
st.write("")
st.write("")

if st.button("Next", type='primary'):
    if st.session_state['prediction_type'] == 'Single Patient':
        st.switch_page('pages/3_Prediction.py')
    else:
        st.switch_page('pages/4_Batch_Prediction.py')
