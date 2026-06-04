import pandas as pd
import matplotlib.pyplot as plt
import os

# =====================================
# LOAD DATASET
# =====================================

df = pd.read_csv("Sales_Dataset_50000_Advanced.csv")

# Convert dates
df["Order_Date"] = pd.to_datetime(df["Order_Date"])
df["Ship_Date"] = pd.to_datetime(df["Ship_Date"])

# Create output folder
os.makedirs("Charts", exist_ok=True)

# =====================================
# 1. MONTHLY SALES TREND
# =====================================

df["Month"] = df["Order_Date"].dt.to_period("M")

monthly_sales = (
    df.groupby("Month")["Sales"]
    .sum()
)

plt.figure(figsize=(12, 6))
monthly_sales.plot()

plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)

plt.tight_layout()
plt.savefig("Charts/01_Monthly_Sales_Trend.png")
plt.close()

# =====================================
# 2. TOP 10 PRODUCTS
# =====================================

top_products = (
    df.groupby("Product_Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))
top_products.plot(kind="bar")

plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("Charts/02_Top_Products.png")
plt.close()

# =====================================
# 3. REGION SALES
# =====================================

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(8, 5))
region_sales.plot(kind="bar")

plt.title("Region-wise Sales")
plt.xlabel("Region")
plt.ylabel("Sales")

plt.tight_layout()
plt.savefig("Charts/03_Region_Sales.png")
plt.close()

# =====================================
# 4. CATEGORY SALES
# =====================================

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

plt.figure(figsize=(10, 6))
category_sales.plot(kind="bar")

plt.title("Category-wise Sales")
plt.xlabel("Category")
plt.ylabel("Sales")

plt.xticks(rotation=20)

plt.tight_layout()
plt.savefig("Charts/04_Category_Sales.png")
plt.close()

# =====================================
# 5. PAYMENT MODE ANALYSIS
# =====================================

payment_sales = (
    df.groupby("Payment_Mode")["Sales"]
    .sum()
)

plt.figure(figsize=(8, 8))
payment_sales.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")
plt.title("Sales by Payment Mode")

plt.tight_layout()
plt.savefig("Charts/05_Payment_Mode.png")
plt.close()

# =====================================
# 6. CUSTOMER RATING DISTRIBUTION
# =====================================

plt.figure(figsize=(8, 5))

df["Customer_Rating"].value_counts().sort_index().plot(
    kind="bar"
)

plt.title("Customer Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Count")

plt.tight_layout()
plt.savefig("Charts/06_Customer_Rating.png")
plt.close()

# =====================================
# 7. RETURN ANALYSIS
# =====================================

returns = df["Returned"].value_counts()

plt.figure(figsize=(7, 7))

returns.plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")
plt.title("Return Analysis")

plt.tight_layout()
plt.savefig("Charts/07_Return_Analysis.png")
plt.close()

# =====================================
# 8. TOP 10 CITIES
# =====================================

top_cities = (
    df.groupby("City")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))

top_cities.plot(kind="bar")

plt.title("Top 10 Cities by Sales")
plt.xlabel("City")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("Charts/08_Top_Cities.png")
plt.close()

# =====================================
# 9. CUSTOMER TYPE ANALYSIS
# =====================================

customer_type = (
    df.groupby("Customer_Type")["Sales"]
    .sum()
)

plt.figure(figsize=(7, 5))

customer_type.plot(kind="bar")

plt.title("Customer Type Sales")
plt.xlabel("Customer Type")
plt.ylabel("Sales")

plt.tight_layout()
plt.savefig("Charts/09_Customer_Type.png")
plt.close()

# =====================================
# 10. SALESPERSON PERFORMANCE
# =====================================

top_salesperson = (
    df.groupby("Salesperson_Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

plt.figure(figsize=(12, 6))

top_salesperson.plot(kind="bar")

plt.title("Top 10 Salespersons")
plt.xlabel("Salesperson")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("Charts/10_Top_Salespersons.png")
plt.close()

# =====================================
# SUCCESS MESSAGE
# =====================================

print("=" * 60)
print("ALL CHARTS GENERATED SUCCESSFULLY")
print("=" * 60)

print("\nCharts saved in:")
print("Charts/")

print("\nGenerated Charts:")
print("""
01_Monthly_Sales_Trend.png
02_Top_Products.png
03_Region_Sales.png
04_Category_Sales.png
05_Payment_Mode.png
06_Customer_Rating.png
07_Return_Analysis.png
08_Top_Cities.png
09_Customer_Type.png
10_Top_Salespersons.png
""")