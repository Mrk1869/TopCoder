import math
import string

class Quipu:
    def readKnots(self, knots):

        last_val = "o"
        res = ""
        num_count = 0

        for val in knots:

            if val == "-":
                if num_count != 0:
                    res = res + str(num_count)
                    num_count = 0
                if last_val == "-":
                    res = res + "0"

            elif val == "X":
                num_count += 1

            last_val = val

        return int(res)

# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pfx 2.1.9
import sys
import time
def KawigiEdit_RunTest(testNum, p0, hasAnswer, p1):
    sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str("\"") + str(p0) + str("\""))
    print(str("]"))
    obj = Quipu()
    startTime = time.clock()
    answer = obj.readKnots(p0)
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
p0 = "-XX-XXXX-XXX-"
p1 = 243
all_right = KawigiEdit_RunTest(0, p0, True, p1) and all_right
# ------------------

# ----- test 1 -----
p0 = "-XX--XXXX---XXX-"
p1 = 204003
all_right = KawigiEdit_RunTest(1, p0, True, p1) and all_right
# ------------------

# ----- test 2 -----
p0 = "-X-"
p1 = 1
all_right = KawigiEdit_RunTest(2, p0, True, p1) and all_right
# ------------------

# ----- test 3 -----
p0 = "-X-------"
p1 = 1000000
all_right = KawigiEdit_RunTest(3, p0, True, p1) and all_right
# ------------------

# ----- test 4 -----
p0 = "-XXXXXXXXX--XXXXXXXXX-XXXXXXXXX-XXXXXXX-XXXXXXXXX-"
p1 = 909979
all_right = KawigiEdit_RunTest(4, p0, True, p1) and all_right
# ------------------

if (all_right):
    print(str("You're a stud (at least on the example cases)!"))
else:
    print(str("Some of the test cases had errors."))

# PROBLEM STATEMENT
#
# The Incas used a sophisticated system of record keeping consisting of bundles of knotted cords.
# Such a bundle of cords is called a quipu.  Each individual cord represents a single number.
# Surprisingly, the Incas used a base-10 positional system, just like we do today.  Each digit of a number
# is represented by a cluster of adjacent knots, with spaces between neighboring clusters.  The digit is
# determined by the number of knots in the cluster.
# For example, the number 243 would be represented by a cord with knots tied in the following pattern
#
#
#      -XX-XXXX-XXX-
#
# where each uppercase 'X' represents a knot and each '-' represents an unknotted segment of cord (all quotes for clarity only).
#
#
# Unlike many ancient civilizations, the Incas were aware of the concept of zero, and used it in their quipus.
# A zero is represented by a cluster containing no knots.
# For example, the number 204003 would be represented by a cord with knots tied in the following pattern
#
#
#      -XX--XXXX---XXX-
#         ^^    ^^^
#         ^^    ^^^
#         ^^    two zeros between these three segments
#         ^^
#         one zero between these two segments
#
# Notice how adjacent dashes signal the presence of a zero.
#
#
# Your task is to translate a single quipu cord into an integer.  The cord will be given as a string knots
# containing only the characters 'X' and '-'.  There will be a single '-' between each cluster
# of 'X's, as well as a leading '-' and a trailing '-'.  The first cluster will not be empty.
#
#
# DEFINITION
# Class:Quipu
# Method:readKnots
# Parameters:string
# Returns:integer
# Method signature:def readKnots(self, knots):
#
#
# CONSTRAINTS
# -knots contains between 3 and 50 characters, inclusive.
# -knots contains only the characters 'X' and '-'.  Note that 'X' is uppercase.
# -The first and last characters of knots are '-'s.  The second character is 'X'.
# -knots does not contain 10 consecutive 'X's.
# -knots will represent a number between 1 and 1000000, inclusive.
#
#
# EXAMPLES
#
# 0)
# "-XX-XXXX-XXX-"
#
# Returns: 243
#
# The first example above.
#
# 1)
# "-XX--XXXX---XXX-"
#
# Returns: 204003
#
# The second example above.
#
# 2)
# "-X-"
#
# Returns: 1
#
# 3)
# "-X-------"
#
# Returns: 1000000
#
# 4)
# "-XXXXXXXXX--XXXXXXXXX-XXXXXXXXX-XXXXXXX-XXXXXXXXX-"
#
# Returns: 909979
#
# END KAWIGIEDIT TESTING
#Powered by KawigiEdit-pfx 2.1.9!
