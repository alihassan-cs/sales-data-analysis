import pandas as pd
import matplotlib.pyplot as plt

# LOAD DATA
df = pd.read_csv("data/sales.csv")

print("First 5 rows:")
print(df.head())

# CLEAN DATA
df = df.dropna()

# ANALYSIS
top_products = df.groupby("Sub-Category")["Sales"].sum().sort_values(ascending=False)

print("\nTop Sub-Categories:\n")
print(top_products)

# VISUALIZATION
plt.figure(figsize=(10,5))
top_products.plot(kind="bar")
plt.title("Top Sub-Categories by Sales")
plt.xlabel("Sub-Category")
plt.ylabel("Sales")
plt.tight_layout()
plt.savefig("images/top_sales.png")
plt.clf()

# Sales by Region
region_sales = df.groupby("Region")["Sales"].sum()
print("\nSales by Region:\n", region_sales)

region_sales.plot(kind="bar", title="Sales by Region")
plt.savefig("images/region_sales.png")
plt.clf()

# Sales by Category
category_sales = df.groupby("Category")["Sales"].sum()
print("\nSales by Category:\n", category_sales)

category_sales.plot(kind="bar", title="Sales by Category")
plt.savefig("images/category_sales.png")
plt.clf()