# # analyzer.py
# import pandas as pd
# from helpers import calculate_total, format_currency

# # Read data
# df = pd.read_csv('../data/saless.csv')

# # Calculate total for each row
# totals = []
# for index, row in df.iterrows():
#     total = calculate_total(row['quantity'], row['price'])
#     totals.append(total)

# # Add totals to our data
# df['total'] = totals

# # Display with formatted totals
# print("Sales Data:")
# for index, row in df.iterrows():
#     formatted_total = format_currency(row['total'])
#     print(f"{row['product']}: {formatted_total}")

# # Show grand total
# grand_total = df['total'].sum()
# formatted_grand_total = format_currency(grand_total)
# print(f"\nGrand Total: {formatted_grand_total}")



import pandas as pd
from helpers import calculate_total, format_currency

df=pd.read_csv('../data/saless.csv')

totals=[]
for item, row in df.iterrows():
    total=calculate_total(row['price'], row['quantity'])
    totals.append(total)

df['total']=totals

print("Sales data: ")
for item, row in df.iterrows():
    formatted_total=format_currency(row['total'])
    print(f"{row['product']}: {formatted_total}")

# show total

grand_total=df['total'].sum()
formatted_grand_total=format_currency(grand_total)
print(f"\nGrand total : {formatted_grand_total}")

