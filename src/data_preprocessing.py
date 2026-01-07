import pandas as pd

def load_and_preprocess():
    df = pd.read_csv("data/financial_data.csv")

    df["expense_ratio"] = df["expenses"] / df["revenue"]
    df["debt_ratio"] = df["debt"] / df["assets"]

    X = df[[
        "revenue",
        "expenses",
        "cash_flow",
        "debt",
        "assets",
        "expense_ratio",
        "debt_ratio"
    ]]

    y = df["risk"]

    return X, y
