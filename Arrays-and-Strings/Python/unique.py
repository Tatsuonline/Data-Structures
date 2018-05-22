""" Implement an algorithm to determine if a string has all unique characters.
    What if you can not use additional data structures? """

def snowflake_with_data_structures (string):

    snow_dict = {}

    for character in string:
        if character in snow_dict.keys():
            return False
        else:
            snow_dict[character] = None

    return True

def snowflake (string):

    string = list(string)
    string.sort()
    previous = string[0]
    for character in string[1:]:
        if character == previous:
            return False

    return True
