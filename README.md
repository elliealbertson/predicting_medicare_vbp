# Predicting Medicare Hospital Value-Based Purchasing Program Participation

Value-based purchasing programs can incentivize higher quality health care at a lower cost.

This project used the `keras` library in Python to develop a deep learning model to predict hospital participation in a Medicare value-based purchasing program from the Centers for Medicare and Medicaid Services (CMS), and used Streamlit to publish an app interface.

Key steps in this project:

- Used the `requests` and `pandas` packages to get data from the CMS API and the State of California
- Used the `fuzzywuzzy` package to fuzzy match state and federal hospital datasets on hospital name and address
- Used the `scikit-learn` and `pandas` packages to prepare a clean dataset for analysis, and used `pickle` to save a preprocessing pipeline
- Used `keras` to generate a classification algorithm to predict hospital participation in the program, and saved the best-performing model
- Used `streamlit` to develop an app to enable predictions based on user-defined hospital characteristics, and published the app [here](https://predicting-medicare-vbp.streamlit.app/)
