# Streamline App
import streamlit as st
st.set_page_config(page_title="Welcome")

left_co,cent_co,last_co = st.columns(3)
with cent_co:
    st.title("Project Star")
    st.image('img/star.webp')
    st.markdown('This project aims to help users locate jobs using NLP and ML techniques.')
    st.markdown('To start, enter your name:')
    Name = st.text_input('Name')

    if st.button('Proceed'):
      st.switch_page('pages/getskills.py')


#st.markdown('<div style="text-align: center"><a href="/pages/getskills" target="_self">Start</a></div>', unsafe_allow_html=True)
