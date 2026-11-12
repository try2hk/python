# Snippet-1
name = input("What's your name? ")
print(f"hello, {name}")

# Snippet-2
name = input("What's your name? ").strip().title()
print(f"hello, {name}")

# Snippet-3
name = input("What's your name? ").strip().title()
first, last = name.split(" ")
print(f"hello, {first}")