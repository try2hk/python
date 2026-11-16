# snippet-1
# name = input("What's your name? ")

# if name == "Harry":
#     print("Gryffindor")
# elif name == "Hermione":
#     print("Gryffindor")
# elif name == "Ron":
#     print("Grayfiindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

# # snippet-2
# name = input("What's your name? ")

# if name == "Harry" or name == "Hermione" or name == "Ron":
#     print("Gryffindor")
# elif name == "Draco":
#     print("Slytherin")
# else:
#     print("Who?")

# Snippet-3
# name = input("What's your name? ")

# match name:
#     case "Harry":
#         print("Gryffindor")
#     case "Hermione":    
#         print("Gryffindor")
#     case "Ron":
#         print("Gryffinder")
#     case "Draco":
#         print("Slyther")
#     case _:
#         print("Who?")

# Snippet-3
name = input("What's your name? ")

match name:
    case "Harry" | "Hermione | Ron":
        print("Gryffindor")
    case "Draco":
        print("Slyther")
    case _:
        print("Who?")  