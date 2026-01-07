import pandas as pd
import numpy as np

np.random.seed(42)

n = 500

data = {
    "revenue": np.random.randint(50000, 500000, n),
    "expenses": np.random.randint(30000, 450000, n),
    "cash_inflow": np.random.randint(20000, 400000, n),
    "cash_outflow": np.random.randint(25000, 420000, n),
    "debt": np.random.randint(10000, 300000, n),
    "assets": np.random.randint(50000, 600000, n)
}

df = pd.DataFrame(data)

df["cash_flow"] = df["cash_inflow"] - df["cash_outflow"]
df["risk"] = np.where(df["cash_flow"] < 0, 1, 0)

df.to_csv("data/financial_data.csv", index=False)

print("Financial dataset generated successfully.")
