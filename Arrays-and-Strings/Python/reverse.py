""" Write code to reverse a C-Style String (C-String means that “abcd” 
    is represented as five characters, including the null character) """

def simple_reverse (string):

    string = list(string[:-1])
    string.reverse()
    string.append("\0")
    string = "".join(string)

    return string

def reverso (string):

    string = list(string[:-1])
    for x in range(0, int(len(string)/2)):
        temp = string[-(x + 1)]
        string[-(x + 1)] = string[x]
        string[x] = temp

    string.append("\0")
    string = "".join(string)

    return str(string)
