# Write a function that takes a character (i.e. a string of length 1) and
# returns True if it is a vowel, False otherwise.


def vowel(char):
    if char in ("a", "e", "i", "o", "u"):
        print("True")
        return True
    else:
        print("False")
        return False
