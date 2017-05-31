# Write a function is_member() that takes a value (i.e. a number, string, etc)
# x and a list of values a, and returns True if x is a member of a, False otherwise.
# (Note that this is exactly what the in operator does, but for the sake of the exercise
# you should pretend Python did not have this operator.)


def is_member(x, list_of_values):
    i = 0
    while i < len(list_of_values):
        for value in list_of_values:
            if x == value:
                print("True")
                return True
            else:
                i += 1
    print("False")
    return False
