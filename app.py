import streamlit as st
import pandas as pd
import numpy as np
import joblib

model = joblib.load("model.pkl")

st.title("House Loan Prediction")
st.write(
    'This is a simple web app to predict whether a person can get a house loan or not based on the information provided by the user. Please provide the required information in the sidebar and click on the "Predict" button to check the prediction.'
)

st.image("house.jpg", use_column_width=True)

form = st.form(key='my_form')

gender = form.selectbox("Gender",["Male","Female"])
married = form.selectbox("Married",["No","Yes"])
dependents = form.selectbox("Dependents",["0","1","2","3+"])
education = form.selectbox("Education",["Not Graduate","Graduate"])
self_employed = form.selectbox("Self Employed",["Yes","No"])
credit_history = form.selectbox("Credit History",["Yes","No"])
property_area = form.selectbox("Property Area",["Urban","Semiurban","Rural"])
applicant_income = form.number_input("Applicant Income", value=0)
coapplicant_income = form.number_input("Coapplicant Income", value=0)
loan_amount = form.number_input("Loan Amount", min_value=1, max_value=10000, value=100)
loan_amount_term = form.number_input("Loan Amount Term", min_value=1, max_value=1000, value=360)
total_income = applicant_income + coapplicant_income
emi = loan_amount / loan_amount_term

submit = form.form_submit_button("Predict")

# change categorical data to numerical data

if gender == "Male":
    gender = 1
else:
    gender = 0

if married == "Yes":
    married = 1
else:
    married = 0

if education == "Graduate":
    education = 1
else:
    education = 0

if self_employed == "Yes":
    self_employed = 1
else:
    self_employed = 0

if credit_history == "Yes":
    credit_history = 1
else:
    credit_history = 0

if property_area == "Urban":
    property_area = 0
elif property_area == "Semiurban":
    property_area = 1
else:
    property_area = 2

if dependents == "0":
    dependents = 0
elif dependents == "1":
    dependents = 1
elif dependents == "2":
    dependents = 2
else:
    dependents = 3


if submit:
    prediction = model.predict([[applicant_income, coapplicant_income, loan_amount, loan_amount_term, total_income, emi, 
                               gender, married, dependents, education, self_employed, credit_history, property_area]])

    if prediction == 1:
        st.success("Congratulations! You are eligible for the loan.")
        st.balloons()
    else:
        st.error("Sorry, you are not eligible for the loan.")

