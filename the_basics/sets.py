# a collection which is unordered, unindexed. No duplicate values

utensils = {"fork", "spoon", "knife"}
dishes = {"bowl", "plate", "cup", "knife"}

# useful methods
# utensils.add("napkin")
# utensils.remove("fork")
# utensils.clear()
# utensils.update(dishes) # this adds another set 
# dinner_table = utensils.union(dishes) # put together two sets
# print(utensils.difference(dishes)) # check what utensils has that dishes doesn't
# print(utensils.intersection(dishes)) # what element they have in common

for x in dishes:
    print(x)