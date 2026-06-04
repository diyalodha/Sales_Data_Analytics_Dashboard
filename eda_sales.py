import pandas as pd

# =====================================
# LOAD DATASET
# =====================================

df = pd.read_csv("Sales_Dataset_50000_Advanced.csv")

# =====================================
# BASIC DATA ANALYSIS
# =====================================

print("\n" + "="*60)
print("DATASET INFORMATION")
print("="*60)

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

print("\nColumn Names:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

# =====================================
# MISSING VALUES
# =====================================

print("\n" + "="*60)
print("MISSING VALUES")
print("="*60)

print(df.isnull().sum())

# =====================================
# SUMMARY STATISTICS
# =====================================

print("\n" + "="*60)
print("SUMMARY STATISTICS")
print("="*60)

print(df.describe())

# =====================================
# BUSINESS KPIs
# =====================================

print("\n" + "="*60)
print("BUSINESS KPIs")
print("="*60)

total_sales = df["Sales"].sum()

total_profit = df["Profit"].sum()

total_orders = df["Order_ID"].nunique()

total_customers = df["Customer_ID"].nunique()

average_order_value = total_sales / total_orders

average_profit = total_profit / total_orders

profit_margin = (total_profit / total_sales) * 100

print(f"\nTotal Sales: ₹{total_sales:,.2f}")

print(f"Total Profit: ₹{total_profit:,.2f}")

print(f"Total Orders: {total_orders:,}")

print(f"Total Customers: {total_customers:,}")

print(f"Average Order Value: ₹{average_order_value:,.2f}")

print(f"Average Profit Per Order: ₹{average_profit:,.2f}")

print(f"Overall Profit Margin: {profit_margin:.2f}%")

# =====================================
# TOP 10 PRODUCTS
# =====================================

print("\n" + "="*60)
print("TOP 10 PRODUCTS BY SALES")
print("="*60)

top_products = (
    df.groupby("Product_Name")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_products)

# =====================================
# TOP 10 CITIES
# =====================================

print("\n" + "="*60)
print("TOP 10 CITIES BY SALES")
print("="*60)

top_cities = (
    df.groupby("City")["Sales"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
)

print(top_cities)

# =====================================
# REGION WISE SALES
# =====================================

print("\n" + "="*60)
print("REGION WISE SALES")
print("="*60)

region_sales = (
    df.groupby("Region")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(region_sales)

# =====================================
# CATEGORY WISE SALES
# =====================================

print("\n" + "="*60)
print("CATEGORY WISE SALES")
print("="*60)

category_sales = (
    df.groupby("Category")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(category_sales)

# =====================================
# PAYMENT MODE ANALYSIS
# =====================================

print("\n" + "="*60)
print("PAYMENT MODE ANALYSIS")
print("="*60)

payment_analysis = (
    df.groupby("Payment_Mode")["Sales"]
    .sum()
    .sort_values(ascending=False)
)

print(payment_analysis)

# =====================================
# RETURN ANALYSIS
# =====================================

print("\n" + "="*60)
print("RETURN ANALYSIS")
print("="*60)

return_rate = (
    df["Returned"]
    .value_counts(normalize=True)
    * 100
)

print(return_rate)

# =====================================
# CUSTOMER RATING ANALYSIS
# =====================================

print("\n" + "="*60)
print("CUSTOMER RATING ANALYSIS")
print("="*60)

print(df["Customer_Rating"].value_counts().sort_index())

print("\n")
print("="*60)
print("EDA COMPLETED SUCCESSFULLY")
print("="*60)