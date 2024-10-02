# Define a function 'message' that takes two positional-only arguments: 'name' and 'prof'

def message(name, prof, /):
    # Print a formatted message with the provided name and profession
    print('My name is ' + name + ' and I am a/an ' + prof)

# Call the function with positional arguments 'James' and 'Actor'
message('James', 'Actor')
