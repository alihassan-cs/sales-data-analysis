import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -----------------------------
# LOAD DATA (IMPORTANT FIX)
# -----------------------------
df = pd.read_csv("../data/sales.csv")

print("First 5 rows:")
print(df.head())

# -----------------------------
# CLEAN DATA
# -----------------------------
df = df.dropna()

# -----------------------------
# ANALYSIS
# -----------------------------
top_products = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False)

print("\nTop Sub-Categories:\n")
print(top_products)

# -----------------------------
# VISUALIZATION
# -----------------------------
plt.figure(figsize=(10,5))
top_products.plot(kind="bar")
plt.title("Top Sub-Categories by Sales")
plt.xlabel("Sub-Category")
plt.ylabel("Sales")
plt.tight_layout()

# SAVE IMAGE (IMPORTANT FIX)
plt.savefig("../images/top_sales.png")

plt.show()