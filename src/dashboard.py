import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Financial Risk Analytics Dashboard", layout="wide")

st.title("📊 Financial Risk Analytics Dashboard")

df = pd.read_csv("data/financial_data.csv")

with open("risk_model.pkl", "rb") as f:
    model = pickle.load(f)

st.sidebar.header("Enter Business Financial Details")

revenue = st.sidebar.number_input("Revenue", 50000, 500000, 150000)
expenses = st.sidebar.number_input("Expenses", 30000, 450000, 120000)
cash_inflow = st.sidebar.number_input("Cash Inflow", 20000, 400000, 100000)
cash_outflow = st.sidebar.number_input("Cash Outflow", 25000, 420000, 130000)
debt = st.sidebar.number_input("Debt", 10000, 300000, 50000)
assets = st.sidebar.number_input("Assets", 50000, 600000, 200000)

cash_flow = cash_inflow - cash_outflow
expense_ratio = expenses / revenue
debt_ratio = debt / assets

input_data = pd.DataFrame([[
    revenue, expenses, cash_flow, debt, assets, expense_ratio, debt_ratio
]], columns=[
    "revenue", "expenses", "cash_flow",
    "debt", "assets", "expense_ratio", "debt_ratio"
])

prediction = model.predict(input_data)[0]

st.subheader("📌 Risk Prediction Result")

if prediction == 1:
    st.error("⚠️ High Financial Risk Detected")
else:
    st.success("✅ Low Financial Risk")

st.subheader("📈 Cash Flow Distribution")
st.bar_chart(df["cash_flow"])
