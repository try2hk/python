# Snippet-1
# import sys

# print("Hello, My name is", sys.argv[1])

# Snippet-2
# import sys

# print("Hello, My name is", sys.argv[0])

# Snippet-2
# import sys

# try:
#     print("Hello, My name is", sys.argv[1])
# except IndexError:
#     print("Too few argument")

# Snippet-3
# import sys

# if len(sys.argv) < 2:
#     print("Too few argument")
# elif len(sys.argv) > 2:
#     print("Too many argument")
# else:
#     print("hello,", "my name is", sys.argv[1])

# Snippet-4
# import sys

# if len(sys.argv) < 2:
#     sys.exit("Too few argument")
# elif len(sys.argv) > 2:
#     sys.exit("Too many argument")

# print("hello,", "my name is", sys.argv[1])

# Snippet-5
# import sys

# if len(sys.argv) < 2:
#     sys.exit("Too few argument")
# for arg in sys.argv:     # pass multiple argument 
#     print("hello,", "my name is", arg)

# Snippet-6
import sys

if len(sys.argv) < 2:
    sys.exit("Too few argument")
for arg in sys.argv[1:]:
    print("hello,", "my name is", arg)