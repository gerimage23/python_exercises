# Define a function max_of_three() that takes three numbers as arguments and returns the largest of them.


def max3(num1, num2, num3):
    if num1 > num2 and num1 > num3:
        print("The largest of the three numbers is: " + str(num1))
    elif num2 > num1 and num2 > num3:
        print("The largest of the three numbers is: " + str(num2))
    else:
        print("The largest of the three numbers is: " + str(num3))
