# These are collection which are ordered and unchangeable. 
# Are used to group together related data.

student = ("Jurgen", 28, "male")

print(student.count("Jurgen")) # 1
print(student.index("male")) # 2

for x in student:
    print(x)

if "Jurgen" in student:
    print("Jurgen is here!")