# Snippet-1
# x = int(input("What's x? "))
# print(f"x is {x}") # print("x is ", x)

# snippet-3
# try:
#     x = int(input("What's x? "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not an integer")

# snippet-4
# try:
#     x = int(input("What's x? "))
#     print(f"x is {x}")
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

# snippet-5
# while True:
#     try:
#         x = int(input("What's x? "))
#         print(f"x is {x}")
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break

# print(f"x is {x}")

# snippet-6
# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():

#     while True:
#         try:
#             x = int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             break

#     return x

# main()

# snippet-7
# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():

#     while True:
#         try:
#             x = int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             return x

# main()

# snippet-8
# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():

#     while True:
#         try:
#             x = int(input("What's x? "))
#             return x
#         except ValueError:
#             print("x is not an integer")

# main()

# snippet-9
# def main():
#     x = get_int()
#     print(f"x is {x}")

# def get_int():

#     while True:
#         try:
#            return int(input("What's x? "))  
#         except ValueError:
#             pass

# main()

# snippet-10
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
    while True:
        try:
           return int(input(prompt))  
        except ValueError:
            pass

main()

