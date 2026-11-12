# Snippet-1 --> using list, access list
# students = ["Hermoine", "Harry", "Ron"]

# print(students)
# print(students[0])
# print(students[1])
# print(students[2])

# Snippet-2
# students = ["Hermoine", "Harry", "Ron"]

# for student in students:
#     print(student)

# Snippet-2
# students = ["Hermoine", "Harry", "Ron"]

# for i in range(len(students)):
#     print(students[i])

# Snippet-3 --> using list, len 
# students = ["Hermoine", "Harry", "Ron"]

# for i in range(len(students)):
#     print(i + 1, students[i])

# Snippet-4 --> using dic
# students = {
#     "Harry" : "Gryffindor",
#     "Hermione" : "Gryffindor",
#     "Ron" : "Gryffindor",
#     "Draco" : "Slytherin",
# }

# print(students["Hermione"])
# print(students["Harry"])
# print(students["Ron"])
# print(students["Draco"]) 

# Snippet-5 --> using dic
# students = {
#     "Harry" : "Gryffindor",
#     "Hermione" : "Gryffindor",
#     "Ron" : "Gryffindor",
#     "Draco" : "Slytherin",
# }

# for student in students:
#     print(student) # by default python print only key not value

# Snippet-6 --> using dic
# students = {
#     "Harry" : "Gryffindor",
#     "Hermione" : "Gryffindor",
#     "Ron" : "Gryffindor",
#     "Draco" : "Slytherin",
# }

# for student in students:
#     print(student, students[student], sep=", ")

# Snippet-7 --> using dic
students = [
    {"name": "Hermoine", "house":"Gryffindor", "patronus": "otter"},
    {"name": "Harry", "house":"Gryffindor", "patronus": "stag"},
    {"name": "Ron", "house":"Gryffindor", "patronus": "Jack Russell terrier"},
    {"name": "Draco", "house":"Slytherin", "patronus": None},
]

for student in students:
    print(student["name"], student["house"], student["patronus"], sep=", ")