import pandas as pd
import matplotlib.pyplot as plt

# Load the sample retail sales dataset
df = pd.read_csv("sales_data.csv")
df["Date"] = pd.to_datetime(df["Date"])
df["Month"] = df["Date"].dt.to_period("M").astype(str)

# 1. Monthly revenue trend
monthly = df.groupby("Month")["Revenue_INR"].sum()
monthly.plot(kind="line", marker="o", title="Monthly Sales Revenue")
plt.xlabel("Month")
plt.ylabel("Revenue (INR)")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("monthly_sales.png")
plt.close()

# 2. Revenue by product
product = df.groupby("Product")["Revenue_INR"].sum().sort_values()
product.plot(kind="barh", title="Revenue by Product")
plt.xlabel("Revenue (INR)")
plt.tight_layout()
plt.savefig("product_sales.png")
plt.close()

# 3. Revenue share by category
category = df.groupby("Category")["Revenue_INR"].sum()
category.plot(kind="pie", autopct="%1.1f%%", title="Revenue Share by Category")
plt.ylabel("")
plt.tight_layout()
plt.savefig("category_sales.png")
plt.close()

# 4. Revenue by region
region = df.groupby("Region")["Revenue_INR"].sum().sort_values(ascending=False)
region.plot(kind="bar", title="Revenue by Region")
plt.xlabel("Region")
plt.ylabel("Revenue (INR)")
plt.tight_layout()
plt.savefig("regional_sales.png")
plt.close()

print("Charts created successfully.")
print("Total revenue (INR):", round(df["Revenue_INR"].sum(), 2))
print("Total profit (INR):", round(df["Profit_INR"].sum(), 2))
print("Number of orders:", len(df))
