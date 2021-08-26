import streamlit as st
import pandas as pd
import pickle
import numpy as np
st.markdown("<h1 style='text-align: center; color: red;'>Car Price Predictor</h1>", unsafe_allow_html=True)
st.sidebar.write("# Car Information")
m=pd.read_csv('https://raw.githubusercontent.com/mishra1683/Old-Car-Price-Predictor/main/Cleaned%20Car.csv')
model=pickle.load(open('LinearRegressionModel.pkl','rb'))
def predict(a,b,c,d,e):
    p=model.predict(pd.DataFrame(columns=['name','company','year','kms_driven','fuel_type'],data=np.array([a,b,c,d,e]).reshape(1,5)))
    return st.write("The Reselling Price of",e,a,"borrowed in the year",c,"is",float(p))
A=st.sidebar.selectbox("Car Comapny",m['company'].unique())
B=st.sidebar.selectbox("Car Model",m['name'].unique())
C=st.sidebar.text_input("kms_driven")
D=st.sidebar.text_input("Year of purchase")
E=st.sidebar.selectbox("Fuel Type",m['fuel_type'].unique())
if st.sidebar.button("Predict"):
    predict(B,A,D,C,E)