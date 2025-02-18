import streamlit as st
from helper.strings import image
from helper.strings import title
from helper.styles import custom_css


st.set_page_config(layout="wide")
st.markdown(custom_css(), unsafe_allow_html=True)

col1, col2 = st.columns([1.5, 3])
with col1:
    st.image(image)

with col2:
    st.markdown(f"<h1 class='title''>{title}</h1>", unsafe_allow_html=True)

    # st.markdown('''
    #     Garbage In, Garbage Out!' — My last boss
    # ''')
    st.markdown('''
        'We don’t have better algorithms. We just have more data.' — Peter Norvig
    ''')

    st.write('')
    st.write('')
    st.write('')
    st.write('')


    # Button to navigate to another page
    go = st.button('Proceed', type='primary')

    if go:
        st.switch_page('pages/1_Select_Profile.py')
