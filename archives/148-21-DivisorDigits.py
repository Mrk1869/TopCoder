import math
import string

class DivisorDigits:
    def howMany(self, number):

        ans = []
        for num in str(number):
            num = int(num)
            if num != 0:
                if number % num == 0:
                    ans.append(num)
        return(len(ans))

# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pfx 2.1.9
import sys
import time
def KawigiEdit_RunTest(testNum, p0, hasAnswer, p1):
    sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str(p0))
    print(str("]"))
    obj = DivisorDigits()
    startTime = time.clock()
    answer = obj.howMany(p0)
    endTime = time.clock()
    res = True
    print(str("Time: ") + str((endTime - startTime)) + str(" seconds"))
    if (hasAnswer):
        print(str("Desired answer:"))
        print(str("\t") + str(p1))

    print(str("Your answer:"))
    print(str("\t") + str(answer))
    if (hasAnswer):
        res = answer == p1

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
p0 = 12345
p1 = 3
all_right = KawigiEdit_RunTest(0, p0, True, p1) and all_right
# ------------------

# ----- test 1 -----
p0 = 661232
p1 = 3
all_right = KawigiEdit_RunTest(1, p0, True, p1) and all_right
# ------------------

# ----- test 2 -----
p0 = 52527
p1 = 0
all_right = KawigiEdit_RunTest(2, p0, True, p1) and all_right
# ------------------

# ----- test 3 -----
p0 = 730000000
p1 = 0
all_right = KawigiEdit_RunTest(3, p0, True, p1) and all_right
# ------------------

if (all_right):
    print(str("You're a stud (at least on the example cases)!"))
else:
    print(str("Some of the test cases had errors."))

# PROBLEM STATEMENT
# Create a class DivisorDigits containing a method howMany which takes an integer number and returns how many digits in number divide evenly into number itself.
#
# DEFINITION
# Class:DivisorDigits
# Method:howMany
# Parameters:integer
# Returns:integer
# Method signature:def howMany(self, number):
#
#
# NOTES
# -No number is divisible by 0.
#
#
# CONSTRAINTS
# -number will be between 10000 and 999999999.
#
#
# EXAMPLES
#
# 0)
# 12345
#
# Returns: 3
#
# 12345 is divisible by 1, 3, and 5.
#
# 1)
# 661232
#
# Returns: 3
#
# 661232 is divisible by 1 and 2.
#
# 2)
# 52527
#
# Returns: 0
#
# 52527 is not divisible by 5, 2, or 7.
#
# 3)
# 730000000
#
# Returns: 0
#
# Nothing is divisible by 0.  In this case, the number is also not divisible by 7 or 3.
#
# END KAWIGIEDIT TESTING
#Powered by KawigiEdit-pfx 2.1.9!