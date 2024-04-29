# Streamline App
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.tree import DecisionTreeClassifier # Import Decision Tree Classifier
from sklearn.model_selection import train_test_split # Import train_test_split function
from sklearn import metrics
import os
from joblib import load
from sklearn.metrics.pairwise import cosine_similarity
from gensim.models import Word2Vec
import sys
sys.path.append('../ML-Logic/word2vec/')
sys.path.append('../ML-Logic/decision_tree/')
import word2vec_functions as wf
import decision_tree_functions as dt
from sklearn.feature_extraction.text import CountVectorizer # For the tokenizer and stop words removal
import re


def process_skills(skills):
    skills = re.sub('[^a-zA-Z, ]','',skills)
    skills = skills.lower()
    skills_token = skills.split(',')
    return skills_token

def process_skills2(skills):
    skills = skills.lower()
    skills_token = skills.split(',')
    for i,s in enumerate(skills_token):
      skills_token[i] = s.strip()
      skills_token[i] = skills_token[i].replace(' ','_')
    return skills_token


st.set_page_config(page_title="Waiting for your input")

left_co,cent_co,last_co = st.columns(3)
with cent_co:

    st.subheader("Step 1")
    st.markdown("Select your dream job")
 #   option = st.selectbox('Choose', ["Software Engineer","Nurse","Chef"])
    option = st.selectbox('Choose', ["Software Engineer"])

    st.subheader("Step 2")
    st.markdown("Enter your skills relevant to the job, separated by a comma (,)")
    st.markdown("Example: program, develop, software, java, c++, node.js")

    skills = st.text_input('Enter your skills separated by ,')
    new_job_skills = process_skills(skills)
    new_job_skills_2 = process_skills2(skills)

    st.markdown('----------------')

    if skills and option == "Software Engineer":
      st.subheader("Results")
      prediction_data = dt.predict(new_job_skills_2)
#      st.dataframe(prediction_data,hide_index=True)
      prob_is_1 = np.floor(prediction_data.is_software_engineer[0] * 100)
      prob_is_not_1 = np.floor(prediction_data.not_software_engineer[0] * 100)
      st.markdown("##### Based on your skills, you are: ")

      if(prob_is_1 > 55):
        st.markdown("**Congratulations! You are a software engineer. (" + str(prob_is_1) + "%)** :sunglasses:")
      else:
        st.markdown("**Sorry, you are not a software engineer. (" + str(prob_is_1) + "%)**")

#    if skills and option == "Nurse":
#      st.subheader("Results")
#      st.write("Nurse selected")

#    if skills and option == "Chef":
#      st.subheader("Results")
#      st.write("Chef selected")


    if skills and option:
      st.markdown('----------------')
      st.markdown("**Other jobs that we recommend based on your skillset:**")
      data = wf.getTop5Jobs(new_job_skills)
      data['Confidence Score'] = data['Confidence Score'].astype(float).round(2)
      data['Confidence Score'] = data['Confidence Score'] * 100.0

#      st.dataframe(data,hide_index=True)
      for index, row in data.iterrows():
        st.markdown(str(row['Job'])+" ("+str(row['Confidence Score'])+"% match)")