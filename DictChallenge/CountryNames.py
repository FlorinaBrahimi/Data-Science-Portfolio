# Initialize an empty dictionary to store country names categorized by their first letter
countries = {}

# Loop 4 times to allow the user to input 4 country names
for i in range(4):
    # Prompt the user to enter a country name
    name = input('Enter Country Name')
    
    # Check if the first letter (converted to uppercase) is not already a key in the dictionary
    if name[0].upper() not in countries:
        # If the first letter is not in the dictionary, add it as a key with the country name as the first entry in a list
        countries[name[0].upper()] = [name]
    else:
        # If the first letter is already a key, append the country name to the list of countries under that letter
        countries[name[0].upper()].append(name)

# Print the resulting dictionary where countries are grouped by their first letter
print(countries)
