import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import timedelta

# -----------------------------
# Initialization
# -----------------------------
fake = Faker('en_IN')
np.random.seed(42)
random.seed(42)

NUM_RECORDS = 50000

# -----------------------------
# Products
# -----------------------------
products = {
    "Electronics": [
        ("Laptop", 50000),
        ("Smartphone", 25000),
        ("Tablet", 15000),
        ("Smartwatch", 8000),
        ("Headphones", 3000)
    ],
    "Furniture": [
        ("Chair", 2500),
        ("Table", 6000),
        ("Sofa", 25000),
        ("Wardrobe", 18000),
        ("Bookshelf", 5000)
    ],
    "Clothing": [
        ("T-Shirt", 800),
        ("Jeans", 1500),
        ("Jacket", 2500),
        ("Kurta", 1200),
        ("Dress", 1800)
    ],
    "Home Appliances": [
        ("Refrigerator", 35000),
        ("Washing Machine", 28000),
        ("Microwave", 10000),
        ("Mixer", 3000),
        ("Air Conditioner", 45000)
    ],
    "Sports": [
        ("Cricket Bat", 2500),
        ("Football", 1200),
        ("Badminton Racket", 1800),
        ("Gym Bag", 1000),
        ("Yoga Mat", 800)
    ]
}

# -----------------------------
# Region-State-City Mapping
# -----------------------------
locations = {
    "North": {
        "Rajasthan": ["Jaipur", "Jodhpur"],
        "Delhi": ["New Delhi"],
        "Punjab": ["Chandigarh", "Ludhiana"]
    },
    "South": {
        "Karnataka": ["Bangalore", "Mysore"],
        "Tamil Nadu": ["Chennai", "Coimbatore"],
        "Telangana": ["Hyderabad"]
    },
    "East": {
        "West Bengal": ["Kolkata"],
        "Bihar": ["Patna"],
        "Odisha": ["Bhubaneswar"]
    },
    "West": {
        "Maharashtra": ["Mumbai", "Pune"],
        "Gujarat": ["Ahmedabad", "Surat"]
    },
    "Central": {
        "Madhya Pradesh": ["Bhopal", "Indore"],
        "Chhattisgarh": ["Raipur"]
    }
}

# -----------------------------
# Salespersons
# -----------------------------
salespersons = []

for i in range(1, 51):
    salespersons.append(
        (
            f"SP{i:03}",
            fake.name()
        )
    )

# -----------------------------
# Options
# -----------------------------
payment_modes = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Cash",
    "Net Banking"
]

shipping_modes = [
    "Standard",
    "Express",
    "Premium",
    "Same Day"
]

discount_types = [
    "No Discount",
    "Festival Offer",
    "Clearance Sale",
    "Loyalty Discount"
]

genders = [
    "Male",
    "Female"
]

customer_types = [
    "New",
    "Returning"
]

# -----------------------------
# Data Generation
# -----------------------------
records = []

for i in range(1, NUM_RECORDS + 1):

    # Product Selection
    category = random.choice(list(products.keys()))
    product_name, base_price = random.choice(products[category])

    # Region -> State -> City
    region = random.choice(list(locations.keys()))
    state = random.choice(list(locations[region].keys()))
    city = random.choice(locations[region][state])

    # Customer
    customer_id = f"CUST{random.randint(1000,9999)}"
    customer_name = fake.name()

    age = random.randint(18, 65)
    gender = random.choice(genders)

    customer_type = random.choices(
        customer_types,
        weights=[30, 70]
    )[0]

    # Quantity
    quantity = random.randint(1, 10)

    # Seasonal Demand
    order_date = fake.date_between(
        start_date='-3y',
        end_date='today'
    )

    month = order_date.month

    seasonal_multiplier = 1

    if month in [10, 11, 12]:
        seasonal_multiplier = 1.4
    elif month == 1:
        seasonal_multiplier = 0.9

    # Pricing
    unit_price = round(
        base_price *
        np.random.uniform(0.9, 1.1) *
        seasonal_multiplier,
        2
    )

    gross_sales = quantity * unit_price

    # Discount
    discount_type = random.choice(discount_types)

    if discount_type == "No Discount":
        discount_percent = 0
    elif discount_type == "Festival Offer":
        discount_percent = random.randint(10, 20)
    elif discount_type == "Clearance Sale":
        discount_percent = random.randint(15, 30)
    else:
        discount_percent = random.randint(5, 15)

    discount_amount = gross_sales * discount_percent / 100

    sales = gross_sales - discount_amount

    # Cost and Profit
    cost_price = sales * np.random.uniform(0.60, 0.85)

    profit = sales - cost_price

    profit_margin = (
        profit / sales * 100
        if sales > 0 else 0
    )

    # Shipping
    shipping_mode = random.choice(shipping_modes)

    if shipping_mode == "Same Day":
        delivery_days = 0
    elif shipping_mode == "Express":
        delivery_days = random.randint(1, 3)
    elif shipping_mode == "Premium":
        delivery_days = random.randint(2, 5)
    else:
        delivery_days = random.randint(4, 8)

    ship_date = order_date + timedelta(days=delivery_days)

    # Returns
    returned = np.random.choice(
        ["Yes", "No"],
        p=[0.05, 0.95]
    )

    # Ratings
    if returned == "Yes":
        rating = random.randint(1, 3)
    else:
        rating = random.randint(3, 5)

    # Salesperson
    salesperson_id, salesperson_name = random.choice(
        salespersons
    )

    records.append([
        f"ORD{i:06}",
        order_date,
        ship_date,
        delivery_days,
        customer_id,
        customer_name,
        age,
        gender,
        customer_type,
        region,
        state,
        city,
        category,
        product_name,
        quantity,
        round(unit_price, 2),
        round(cost_price, 2),
        round(sales, 2),
        discount_percent,
        discount_type,
        round(profit, 2),
        round(profit_margin, 2),
        returned,
        rating,
        random.choice(payment_modes),
        shipping_mode,
        salesperson_id,
        salesperson_name
    ])

# -----------------------------
# DataFrame
# -----------------------------
columns = [
    "Order_ID",
    "Order_Date",
    "Ship_Date",
    "Delivery_Days",
    "Customer_ID",
    "Customer_Name",
    "Customer_Age",
    "Gender",
    "Customer_Type",
    "Region",
    "State",
    "City",
    "Category",
    "Product_Name",
    "Quantity",
    "Unit_Price",
    "Cost_Price",
    "Sales",
    "Discount_Percent",
    "Discount_Type",
    "Profit",
    "Profit_Margin_Percent",
    "Returned",
    "Customer_Rating",
    "Payment_Mode",
    "Shipping_Mode",
    "Salesperson_ID",
    "Salesperson_Name"
]

df = pd.DataFrame(records, columns=columns)

# Save CSV
df.to_csv(
    "Sales_Dataset_50000_Advanced.csv",
    index=False
)

print("Dataset Generated Successfully")
print("Shape:", df.shape)
print(df.head())