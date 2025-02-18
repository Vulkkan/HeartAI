import streamlit as st
from helper.styles import custom_css

st.set_page_config(layout="wide")
st.markdown(custom_css(), unsafe_allow_html=True)

st.markdown(
    "<h1 class='title'>Select profile</h1> <br><br>", unsafe_allow_html=True
)

with st.container():
    # Create a centered layout
    col1, col2 = st.columns([1, 1])

    with col1:
        st.subheader('Create patient datasets', divider="blue")
        if st.button('Create data', type='primary'):
            st.switch_page('pages/Data_Creation.py')

    with col2:
        st.subheader('Run diagnoses', divider="violet")
        if st.button('Run diagnoses', type='primary'):
            st.switch_page('pages/2_Configuration.py')
