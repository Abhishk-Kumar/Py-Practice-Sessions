# helpers.py

# def calculate_total(quantity, price):
#     """Calculate total for a single item"""
#     return quantity * price

# def format_currency(amount):
#     """Format number as currency"""
#     return f"${amount:,.2f}"

def calculate_total(price, quantity):
    return price* quantity

def format_currency(amount):
    return f"${amount:,.2f}"
