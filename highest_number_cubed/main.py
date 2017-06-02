"""This is the entry point of the program."""

def highest_number_cubed(limit):
    number = -1
    test = 0
    while test < limit:
        number += 1
        test = number * number * number
    return (number - 1)
