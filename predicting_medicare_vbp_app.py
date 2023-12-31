import pickle
import tensorflow as tf
import streamlit as st
import pandas as pd

with open('predicting_medicare_vbp_pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)

model = tf.keras.models.load_model('predicting_medicare_vbp_model.h5')

st.set_page_config(layout="wide")

st.title('Predicting Medicare Hospital Value-Based Purchasing Program Participation')
st.write('Select hospital characteristics to get a prediction.')

st.markdown(
    """
    <style>
        .sidebar {
            background-color: #f2f2f2;
            padding: 10px;
            border-radius: 5px;
            margin-right: 10px;
            font-family: 'Calibri', sans-serif;
        }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.header('About')
st.sidebar.markdown('This app predicts whether a hospital is likely to participate in the [Medicare Hospital Value-Based Purchasing (HVBP) Program](https://www.cms.gov/medicare/quality/initiatives/hospital-quality-initiative/hospital-value-based-purchasing) with the Centers for Medicare & Medicaid Services (CMS). The training set consisted of acute care hospitals in California.')

st.sidebar.header('Source Code')
st.sidebar.markdown('Code is available [here](https://github.com/elliealbertson/predicting_medicare_vbp).')

category_options = {
    'ownership': ["Voluntary Non-Profit", "Proprietary", "Government"],
    'emergency': ["Yes", "No"],
    'interoperability': ["Yes", "No"],
    'teaching': ["Yes", "No"],
    'rural': ["Yes", "No"]
}

col1, col2 = st.columns(2)

with col1:
    ownership = st.selectbox('Hospital Ownership', list(category_options['ownership']))
    emergency = st.selectbox('Has Emergency Services', list(category_options['emergency']))
    interoperability = st.selectbox('Meets Criteria for Promoting Interoperability of EHRs', list(category_options['interoperability']))

with col2:
    teaching = st.selectbox('Teaching Hospital', list(category_options['teaching']))
    rural = st.selectbox('Rural Hospital', list(category_options['rural']))
    beds = st.slider('Number of Beds', min_value=0, max_value=1400, value=200)

input = pd.DataFrame({
    'ownership': [ownership],
    'emergency': [1 if emergency == 'Yes' else 0],
    'interoperability': [1 if interoperability == 'Yes' else 0],
    'teaching': [1 if teaching == 'Yes' else 0],
    'rural': [1 if rural == 'Yes' else 0],
    'beds': [beds]
})

input = pipeline.transform(input)

probability = model.predict(input)
if probability[0][0] > 0.8:
    predicted_class = "Very Likely to Participate"
elif probability[0][0] > 0.5:
    predicted_class = "Somewhat Likely to Participate"
else:
    predicted_class = "Not Likely to Participate"

st.success(f'The Hospital is {predicted_class} (Probability of Participation = {probability[0][0]:.3f})')