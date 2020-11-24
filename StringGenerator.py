"""
Python – Generate Random String of Specific Length
A random string can be needed for a strong password created by the device, or for other scenarios.
Using the random Python programming module, you will create the strings of the specified length and the specified
character classes.
In this section, we create the Generate String Method
This method BY DEFAULT Create a 10 characters string
We may also adjust the size of the string array when calling a certain method
"""
import random
import string


# method generate Alphabet character from ascii table
def random_string(chars=string.ascii_uppercase + string.digits, longer=10):
    return ''.join(random.choice(chars) for _ in range(longer))


# default length(=10) random string
# print("Default Random String :"+random_string())
# random string of length 20
# print("string length 20 : "+random_string(longer=20))
# random string with characters picked from ascii_lowercase
# print("String Lower character "+random_string(chars=string.ascii_lowercase))
# random string with characters picked from 'abcdef123456'
# print("here we give the string to generate :abcdefghi1234567 :\n"+random_string(chars='abcdefghi1234567'))
