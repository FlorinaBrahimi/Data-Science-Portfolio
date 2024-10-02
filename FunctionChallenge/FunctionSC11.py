# Define a function 'planet' that takes an ID and returns the corresponding planet name
def planet(id):
    # Dictionary mapping planet IDs to their corresponding names
    planets = {
        1: 'Mercury', 
        2: 'Venus', 
        3: 'Earth', 
        4: 'Mars', 
        5: 'Jupiter', 
        6: 'Saturn', 
        7: 'Uranus', 
        8: 'Neptune', 
        9: 'Pluto'
    }
    
    # Return the planet name that corresponds to the given ID
    return planets[id]


# Prompt the user to input a planet ID and convert it to an integer
id = int(input('Enter Planet ID: '))

# Call the planet function with the inputted ID and store
