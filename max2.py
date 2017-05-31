# Define a function max() that takes two numbers as arguments and returns the largest of them.
# Use the if-then-else construct available in Python. (It is true that Python has the max() function
# built in, but writing it yourself is nevertheless a good exercise.) ##


def max2(num1, num2):
    if num1 > num2:
        print("The largest of the two numbers is: " + str(num1))
        return num1
    else:
        print("The largest of the two numbers is: " + str(num2))
        return num2
