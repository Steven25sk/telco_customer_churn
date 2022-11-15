import pandas as pd
import pickle
import streamlit as st
import requests
import json

# load pipe
pipe = pickle.load(open("model/preprocess_churn.pkl", "rb"))

# widget input
st.title("Churn Customer Prediction")
seniorcitizen = st.selectbox("SeniorCitizen", ['Yes', 'No'])
partner = st.selectbox("Partner", ['Yes', 'No'])
dependents = st.selectbox("Dependents", ['Yes', 'No'])
tenure = st.number_input("tenure", min_value=0.0, max_value=72.0, value=36.0)
onlinesecurity = st.selectbox("OnlineSecurity", ['Yes', 'No', 'No internet service'])
onlinebackup = st.selectbox("OnlineBackup", ['Yes', 'No', 'No internet service'])
deviceprotection = st.selectbox("DeviceProtection", ['Yes', 'No', 'No internet service'])
techsupport = st.selectbox("TechSupport", ['Yes', 'No', 'No internet service'])
contract = st.selectbox("Contract", ['One year', 'Two year', 'Month-to-month'])
paperlessbilling = st.selectbox("PaperlessBilling", ['Yes', 'No'])
monthlycharges = st.number_input("MonthlyCharges", min_value=18.3, max_value=119.0, value=50.0)

# input to dataframe
new_data = {'SeniorCitizen': seniorcitizen,
            'Partner': partner,
            'Dependents' : dependents,
            'tenure' : tenure,
            'OnlineSecurity' : onlinesecurity,
            'OnlineBackup' : onlinebackup,
            'DeviceProtection' : deviceprotection,
            'TechSupport' : techsupport,
            'Contract' : contract,
            'PaperlessBilling' : paperlessbilling,
            'MonthlyCharges' : monthlycharges}

new_data = pd.DataFrame([new_data])

# preprocessing
new_data = pipe.transform(new_data)
new_data = new_data.tolist()

# input ke model
input_data_json = json.dumps({
    "signature_name": "serving_default",
    "instances": new_data
})

# inference
URL = "https://churn-backend-v1.herokuapp.com/v1/models/churn_model:predict"
r = requests.post(URL, data=input_data_json)

if r.status_code == 200:
    res = r.json()
    if res['predictions'][0][0] >= 0.5:
        st.write('Churn')
    else:
        st.write('Not Churn')
else:
  st.write('Error')

# heroku login
# git init
# git add .
# git status
# git commit -m "Add files"
# heroku create "webname"
# git push heroku main