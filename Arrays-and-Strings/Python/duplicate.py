"""Design  an  algorithm  and  write  code  to  remove  the  duplicate  characters  in  a  string 
   without using any additional buffer. NOTE: One or two additional variables are fine, an extra 
   copy of the array is not.

   FOLLOW UP

   Write the test cases for this method. """

import beyonder # Test case module I have written.

def clone_saga (string):

    string = list(string)

    for x in range(0, len(string)): # Preserving order.
        y = x + 1
        while y < len(string):            
            original = string[x]
            clone = string[y]
            
            if clone == original:
                string.pop(y)

            y += 1

    string = "".join(string)
                
    return string

# Test cases to use with the beyonder module:

test_cases = {}

test_cases["Peter Parker"] = "Petr ak"
test_cases["Ben Reilly"] = "Ben Rily"
test_cases["Kaine Parker"] = "Kaine Prk"
test_cases["Gwen Stacy"] = "Gwen Stacy"

beyonder.beyonder(clone_saga, test_cases) 
