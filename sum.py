# Define a function sum() and a function multiply() that sums and multiplies (respectively) all
# the numbers in a list of numbers.
# For example, sum([1, 2, 3, 4]) should return 10, and multiply([1, 2, 3, 4]) should return 24.


def sum2(list_of_numbers):
    add = 0
    for number in list_of_numbers:
        add = add + number
    print(add)
    return add

sum2([1, 2, 3, 4])


def multiply2(list_of_numbers):
    product = 1
    for number in list_of_numbers:
        product = product * number
    print(product)
    return product

multiply2([1, 2, 3, 4])