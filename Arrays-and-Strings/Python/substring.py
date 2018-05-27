""" Assume  you  have  a  method  isSubstring  which 
    checks  if  one  word  is  a  substring  of another.
    Given two strings, s1 and s2, write code to check if 
    s2 is a rotation of s1 using only one call to isSubstring 
    (i.e., “waterbottle” is a rotation of “erbottlewat”).  """

def polywrath (s1, s2):

    temp = s1 + s1

    isSubstring(s2, temp)
    
def isSubstring (string1, string2):

    print(string1, string2)
    if string1 in string2:
        return True

polywrath("erbottlewat", "waterbottle")
