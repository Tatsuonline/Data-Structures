""" Write a method to decide if two strings are anagrams or not. """

def voldemort (string_0, string_1):

    string_0 = list(string_0)
    string_0.sort()
    string_1 = list(string_1)
    string_1.sort()

    if len(string_0) != len(string_1):
        return False
    
    for x in range(0, len(string_0)):
        if string_0[x] != string_1[x]:
            return False

    return True
