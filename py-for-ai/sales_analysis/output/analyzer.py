# import os


# # check current directory
# print("Current directory:", os.getcwd())
# data_path="data/saless.csv"

# if not os.path.exists(data_path):
#     print("Data was not found at :" , {data_path})
# else:
#     print(f"Data found sucessfully at {data_path}")

import os
import pandas as pd
import json

from dotenv import load_dotenv

load_dotenv()
# read data from csv file
df = pd.read_csv("../data/saless.csv")
print("CSV Data :")
print(f"\nShape : {df.shape[0]} rows, {df.shape[1]} columns")

# calculate total fr each

df["total"] = df["price"] * df["quantity"]
print("\n With Totals:")
print(df)

# creating output directory
if not os.path.exists("output"):
    os.makedirs("output")

# os.makedirs("output", exist_ok=True)

# Save file in different formats

df.to_json("output/sales_data.json", orient="records", indent=2)

# excel format

df.to_excel("output/sales_data.xlsx", index=False)

# csv
df.to_csv("output/sales_data.csv", index=False)

print("\nFiles saved:")
print("- output/sales_data.json")
print("- output/sales_data.xlsx")
print("- output/sales_with_totals.csv")

import os
def   calculate_total(items):
    total=0
    for item in items:
        total+=item['price']*item['quantity']
    return total

shopping_cart=[{'name':'apple','price':0.5,'quantity':6},{'name':'banana','price':0.3,'quantity':8}]
print(calculate_total(shopping_cart))
