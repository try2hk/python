from hello import hello

# Snippet-1
# def test_hello():
#     hello("David") == "hello, David"

# Snippet-2
# def test_hello():
#     assert hello("David") == "hello, David"
#     assert hello() == "hello, world"

# Snippet-2
def test_defaut():
    assert hello() == "hello, world"

def test_argument():
    assert hello("David") == "hello, David"