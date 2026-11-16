import pytest
from calculator import square


# # Snippet-1
# def main():
#     test_square()


# def test_square():
#     if square(2) != 4:
#         print("2 squared was not 4")
#     if square(3) != 9:
#         print("3 squared was not 9")


# if __name__ == "__main__":
#     main()

# Snippet-2
# def main():
#     test_square()


# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9


# if __name__ == "__main__":
#     main()

# Snippet-3
# def main():
#     test_square()


# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared was not 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 squared was not 9")


# if __name__ == "__main__":
#     main()

# Snippet-4
# def main():
#     test_square()


# def test_square():
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared was not 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 squared was not 9")
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("-2 squared was not 4")
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("-3 squared was not 9")
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("0 squared was not 0")


# if __name__ == "__main__":
#     main()

# Snippet-5
# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-2) == 4
#     assert square(-3) == 9
#     assert square(0) == 0

# Snippet-6
# def test_positive():
#     assert square(1) == 1
#     assert square(2) == 4
#     assert square(3) == 9


# def test_negative():
#     assert square(-1) == 1
#     assert square(-2) == 4
#     assert square(-3) == 9


# def test_zero():
#     assert square(0) == 0

# Snippet-7
def test_positive():
    assert square(2) == 4
    assert square(3) == 9


def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9


def test_zero():
    assert square(0) == 0


def test_str():
    with pytest.raises(TypeError):
        square("cat")