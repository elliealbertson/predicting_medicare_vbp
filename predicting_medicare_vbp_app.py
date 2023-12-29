import pickle

with open('predicting_medicare_vbp_pipeline.pkl', 'rb') as file:
    pipeline = pickle.load(file)