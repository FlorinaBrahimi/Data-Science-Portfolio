# A dictionary containing words as keys and their definitions as values
dict1 = {
    'piece': 'portion of an object or of material, produced by cutting',
    'patch': 'a piece of cloth or other material used to mend or strengthen a torn or weak point',
    'area': 'a region or part of a town, a country, or the world',
    'visit': 'go to see and spend time with (someone)',
    'small': 'less than normal',
    'with': 'having or possessing'
}

# Extract the keys (words) from the dictionary and store them in a list
keys = list(dict1.keys())

# Extract the values (definitions) from the dictionary and store them in a list
values = list(dict1.values())

# Create a list of lengths for each definition (value) in the dictionary
lens = [len(x) for x in values]

# Find the maximum length of the definitions
max_len = max(lens)

# Find the minimum length of the definitions
min_len = min(lens)

# Find the index of the maximum length definition in the 'lens' list
max_index = lens.index(max_len)

# Find the index of the minimum length definition in the 'lens' list
min_index = lens.index(min_len)

# Print the word (key) and the longest definition (value)
print('Max:', keys[max_index], values[max_index])

# Print the word (key) and the shortest definition (value)
print('Min:', keys[min_index], values[min_index])
