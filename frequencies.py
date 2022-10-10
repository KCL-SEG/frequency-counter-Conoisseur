"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    """
    algorithm:
    convert every item in list to a string if its not already
    count number of each item in list
        Can use a brute force method for this
    add each item to dict
    :param items:
    :return:
    """

    frequencies = {}
    # Your code goes here
    strings = []
    for item in items:
        if type(item) != "str":
            strings.append(str(item))
        else:
            strings.append(item)

    for string in strings:
        if frequencies.get(string) is None:
            frequencies[string] = strings.count(string)

    return frequencies


