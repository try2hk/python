# Snippet-1
# print("#")
# print("#")
# print("#")

# Snippet-2
# for _ in range(3):
#     print("#")

# Snippet-3 --> func, print horizontal 

# def main():
#     print_column(3)

# def print_column(height):
#     # print("# \n" * height, end="")
#     for _ in range(height):
#         print("#")

# main()

# Snippet-4 --> func, print vertical 

# def main():
#     print_row(4)

# def print_row(width):
#     print("# \n" * width)

# main()

# Snippet-5

# def main():
#     print_square(3)

# def print_square(size):

#     # For each row in square
#     for i in range(size):

#         # For each brick in row
#         for j in range(size):

#             # Print brick
#             # print("#" * size)
#             print("#", end="")

#         print()

# main()

# Snippet-5

def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)

def print_row(width):
    print("#" * width)

main()