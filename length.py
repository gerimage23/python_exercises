# Define a function that computes the length of a given list or string.
# (It is true that Python has the len() function built in, but writing it yourself is nevertheless a good exercise.)


def length(user_input):
    counter = 0
    if user_input is str():
        for word in user_input:
            counter += 1
        print(counter)
        return counter
    else:
        for item in user_input:
            counter += 1
        print(counter)
        return counter
