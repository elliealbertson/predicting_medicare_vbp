import pickle
import streamlit as st

with open('predicting_medicare_vbp_pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

st.title('Predicting Medicare Value-Based Payment Program Participation')