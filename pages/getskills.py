# Streamline App
import streamlit as st
st.set_page_config(page_title="Get Skills")

left_co,cent_co,last_co = st.columns(3)
with cent_co:
    st.markdown('Select ')
    st.selectbox('Select', [1,2,3])
    st.button("Proceed")

if st.button("Proceed"):
    st.switch_page("pages/getskills.py") 