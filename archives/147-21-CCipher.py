import math
import string

class CCipher:
    def decode(self, cipherText, shift):
        res = ""
        for val in cipherText:
            res = res + self.getDecodedChar(val, shift)
        return res

    def getDecodedChar(self, char, shift):
        seed = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz'
        index = seed.find(char)

        if index < 0:
            return char

        res = index - shift*2
        if res < 0:
            res = res + len(seed)
        elif res >= len(seed):
            res = res - len(seed)
        return seed[res]

# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pfx 2.1.9
import sys
import time
def KawigiEdit_RunTest(testNum, p0, p1, hasAnswer, p2):
    sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str("\"") + str(p0) + str("\"") + str(",") + str(p1))
    print(str("]"))
    obj = CCipher()
    startTime = time.clock()
    answer = obj.decode(p0, p1)
    endTime = time.clock()
    res = True
    print(str("Time: ") + str((endTime - startTime)) + str(" seconds"))
    if (hasAnswer):
        print(str("Desired answer:"))
        print(str("\t") + str("\"") + str(p2) + str("\""))

    print(str("Your answer:"))
    print(str("\t") + str("\"") + str(answer) + str("\""))
    if (hasAnswer):
        res = answer == p2

    if (not res):
        print(str("DOESN'T MATCH!!!!"))
    elif ((endTime - startTime) >= 2):
        print(str("FAIL the timeout"))
        res = False
    elif (hasAnswer):
        print(str("Match :-)"))
    else:
        print(str("OK, but is it right?"))

    print(str(""))
    return res

all_right = True


# ----- test 0 -----
p0 = "VQREQFGT"
p1 = 2
p2 = "TOPCODER"
all_right = KawigiEdit_RunTest(0, p0, p1, True, p2) and all_right
# ------------------

# ----- test 1 -----
p0 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
p1 = 10
p2 = "QRSTUVWXYZABCDEFGHIJKLMNOP"
all_right = KawigiEdit_RunTest(1, p0, p1, True, p2) and all_right
# ------------------

# ----- test 2 -----
p0 = "TOPCODER"
p1 = 0
p2 = "TOPCODER"
all_right = KawigiEdit_RunTest(2, p0, p1, True, p2) and all_right
# ------------------

# ----- test 3 -----
p0 = "ZWBGLZ"
p1 = 25
p2 = "AXCHMA"
all_right = KawigiEdit_RunTest(3, p0, p1, True, p2) and all_right
# ------------------

# ----- test 4 -----
p0 = "DBNPCBQ"
p1 = 1
p2 = "CAMOBAP"
all_right = KawigiEdit_RunTest(4, p0, p1, True, p2) and all_right
# ------------------

# ----- test 5 -----
p0 = "LIPPSASVPH"
p1 = 4
p2 = "HELLOWORLD"
all_right = KawigiEdit_RunTest(5, p0, p1, True, p2) and all_right
# ------------------

if (all_right):
    print(str("You're a stud (at least on the example cases)!"))
else:
    print(str("Some of the test cases had errors."))

# PROBLEM STATEMENT
#
# Julius Caesar used a system of cryptography, now known as Caesar Cipher, which shifted each letter 2 places further through the alphabet (e.g. 'A' shifts to 'C', 'R' shifts to 'T', etc.). At the end of the alphabet we wrap around, that is 'Y' shifts to 'A'.
#
# We can, of course, try shifting by any number. Given an encoded text and a number of places to shift, decode it.
#
# For example, "TOPCODER" shifted by 2 places will be encoded as "VQREQFGT". In other words, if given (quotes for clarity) "VQREQFGT"  and 2 as input, you will return "TOPCODER". See example 0 below.
#
#
# DEFINITION
# Class:CCipher
# Method:decode
# Parameters:string, integer
# Returns:string
# Method signature:def decode(self, cipherText, shift):
#
#
# CONSTRAINTS
# -cipherText has between 0 to 50 characters inclusive
# -each character of cipherText is an uppercase letter 'A'-'Z'
# -shift is between 0 and 25 inclusive
#
#
# EXAMPLES
#
# 0)
# "VQREQFGT"
# 2
#
# Returns: "TOPCODER"
#
# 1)
# "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# 10
#
# Returns: "QRSTUVWXYZABCDEFGHIJKLMNOP"
#
# 2)
# "TOPCODER"
# 0
#
# Returns: "TOPCODER"
#
# 3)
# "ZWBGLZ"
# 25
#
# Returns: "AXCHMA"
#
# 4)
# "DBNPCBQ"
# 1
#
# Returns: "CAMOBAP"
#
# 5)
# "LIPPSASVPH"
# 4
#
# Returns: "HELLOWORLD"
#
# END KAWIGIEDIT TESTING
#Powered by KawigiEdit-pfx 2.1.9!
