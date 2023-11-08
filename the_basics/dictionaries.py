# These are a changeable, unordered collection of unique key-value pairs. 
# These are fast as they use hashing, which allow us to access a value quickly

capitals = {"USA": "Washington DC",
             "India": "New Dehli",
             "China": "Beijing",
             "Russia": "Moscow"}

capitals.update({"Germany": "Berlin"}) # Add a new value
capitals.update({"USA": "Las Vegas"}) # Update a value
capitals.pop("China") # Remove the key-value
capitals.clear() # Clear the whole dictionary

print(capitals['Russia']) # Moscow
print(capitals.get('Germany')) # This is a much safer way to check a value exists
print(capitals.keys()) # dict_keys(['USA', 'India', 'China', 'Russia'])
print(capitals.values()) # dict_values(['Washington DC', 'New Dehli', 'Beijing', 'Moscow'])
print(capitals.items()) # dict_items([('USA', 'Washington DC'), ('India', 'New Dehli'), ('China', 'Beijing'), ('Russia', 'Moscow')])

for key, value in capitals.items():
    print(key, value) 
    

