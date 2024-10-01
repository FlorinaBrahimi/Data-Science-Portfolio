""" 
Program to calculate cafe stock, price, and calculate the total stock 
"""

# 1. Create a list with 4-6 items called 'menu'
menu = ['Soup', 'Scone', 'Cake', 'Brownie', 'Cheese Sandwich']  # List of items available in the café

# 2. Create a dictionary called 'stock', with the values of the above items representing their quantities
stock = {
    'Soup': 14,            # Quantity of Soup
    'Scone': 10,           # Quantity of Scone
    'Cake': 17,            # Quantity of Cake
    'Brownie': 16,         # Quantity of Brownie
    'Cheese Sandwich': 18   # Quantity of Cheese Sandwich
}

# 3. Create another dictionary named 'price', with prices for each item
price = {
    'Soup': 5,             # Price of Soup
    'Scone': 3,            # Price of Scone
    'Cake': 4,             # Price of Cake
    'Brownie': 4,          # Price of Brownie
    'Cheese Sandwich': 6   # Price of Cheese Sandwich
}

# Print the prices of each item
print(f'Price of each item: {price}\n')

# 4. Calculate the total item value for each of the 5 items 
# Using the formula: item_value = (stock[item] * price[item])
item_value = {}  # Create an empty dictionary to store item values
for key in stock:
    item_value[key] = stock[key] * price[key]  # Calculate total value for each item and store in item_value dictionary
# Print the total value of the 5 items
print(f'Total value of 5 items: {item_value}')

# 5. Calculate the total stock worth in the café by summing all values in the item_value dictionary
total_stock = sum(item_value.values())  # Sum all the values in item_value

# 6. Print the result of total_stock for all 5 items
print(
    f"""\n==================================================
    
    Cafe's total stock value is: {total_stock}  # Display the total stock value
    \n===================================================""")
