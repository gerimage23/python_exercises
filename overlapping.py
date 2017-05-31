# Define a function overlapping() that takes two lists and returns True if they have at least one member in common,
# False otherwise. You may use your is_member() function, or the in operator, but for the sake of the exercise,
# you should (also) write it using two nested for-loops.


def overlapping(list1, list2):
    for item in range(len(list1)):
        for item in list1:
            if item in list2:
                return True
    return False
