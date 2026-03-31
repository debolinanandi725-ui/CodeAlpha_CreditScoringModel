
import streamlit as st
import pandas as pd

st.set_page_config(page_title="Credit Scoring Model")

st.title("💳 Credit Scoring Model")

st.write("Welcome to Credit Scoring Prediction App")

df = pd.read_csv("credit_dataset.csv")

if st.checkbox("Show Dataset"):
    st.write(df.head())

age = st.number_input("Enter Age", 18, 100, 25)
income = st.number_input("Enter Income", 0, 100000, 50000)

if st.button("Predict"):
    if income > 30000:
        st.success("✅ Credit Approved")
    else:
        st.error("❌ Credit Denied")
