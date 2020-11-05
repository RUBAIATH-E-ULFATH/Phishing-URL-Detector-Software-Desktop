from ruba_project_1.src.build_dataset import *
from sklearn.externals import joblib
import pickle
import numpy as np


def main(url):
    #url = "http://www.facebook.com/"

    X_test = feature_extract(url)
    print(X_test)
    X_test = (np.array(X_test)).reshape(1, -1)

    # Load the model from the file
    rf_from_joblib = joblib.load('C:/Users/Rubaiath/PycharmProjects/PhishingDetectionApp/ruba_project_1/notebook_files/model_rf_1.pkl')

    # Use the loaded model to make predictions
    # print(rf_from_joblib.predict(X_test)[0])
    status = rf_from_joblib.predict(X_test)[0]

    if status == 1:
        print("This is a phising website")
    else:
        print("This is a genuine website")
    return status, X_test


if __name__ == "__main__":
    url = "http://www.facebook.com/"
    main(url)
