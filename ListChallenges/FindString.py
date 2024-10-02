# Define a list of food items
food = ['pizza', 'nuggets', 'hotdog', 'noodles', 'pasta', 'burger']

# Prompt the user to enter a letter
letter = input('Enter a Letter: ')

# Loop through each item in the food list
for x in food:
    # Check if the current food item starts with the letter entered by the user
    if x.startswith(letter):
        # If it does, print the food item
        print(x)
