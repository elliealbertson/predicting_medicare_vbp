st.title('Predicting Medicare Value-Based Payment Program Participation')

st.write("This app predicts whether a hospital is likely to participate in the Medicare Hospital Value-Based Purchasing (HVBP) Program with the Centers for Medicare & Medicaid Services (CMS). The training set consisted of acute care hospitals in California.")

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