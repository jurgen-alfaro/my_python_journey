# sort() method     = used with lists
# sort() function   = used with iterables

# students = ["Squidward", "Sandy", "Patrick", "Spongebob", "Mr. Krabs"]

# students.sort()
# students.sort(reverse=True)
# # sorted_students = sorted(students) # the sorted method returns a list and accepts an iterable (tuple for example)

students = [("Squidward", "F", 60),
            ("Sandy", "A", 33),
            ("Patrick", "D", 36),
            ("Spongebob", "B", 20),
            ("Mr. Krabs", "C", 78)]

grade = lambda grades: grades[1]
students.sort(key=grade, reverse=True)
# sorted_students = sorted(students, key=grade) # use this in case you are using an iterable

for i in students:
    print(i)