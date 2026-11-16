# Snippet-1
# print("meow")
# print("meow")
# print("meow")

# Snippet-2

# i = 3
# while i != 0:
#     print("meow")
#     i = i - 1

# Snippet-3
# i = 1
# while i <= 3:
#     print("meow")
#     i = i + 1

# Snippet-4
# i = 0
# while i < 3:
#     print("meow")
#     i = i + 1

# Snippet-5
# i = 0
# while i < 3:
#     print("meow")
#     i += 1

# Snippet-6 --> using list
# for i in [0, 1, 2]:
#     print("meow")

# Snippet-6  --> using range
# for i in range(5):
#     print("meow")
 
# Snippet-7  --> using underscore
# for _ in range(5):
#     print("meow")

# Snippet-8  --> using print func
# print("meow \n" * 3)

# Snippet-9  --> using print func
# print("meow \n" * 3, end="")

# Snippet-10 --> using break stmt
# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break

# for _ in range(n):
#     print("meow")

# Snippet-11 --> using func, while, break stmt
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()