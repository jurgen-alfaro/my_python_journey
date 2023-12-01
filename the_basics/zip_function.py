# zip(*iterables) = aggregate elements from two or more iterables (list, tuples, sets, etc.)
# creates a zip object with paired elements stored in tuples for each element

# Example 1
username = ["Dude", "Bro", "Mister"]
password = ("p@ssword", "abc123", "guest")
login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]

users = zip(username, password, login_date)

print(type(users))

for i in users:
    print(i)    