import math
import string

class TireRotation:
    def getCycle(self, initial, current):

        tires = [x for x in initial]
        for i in xrange(4):
            if "".join(tires) == current:
                return i + 1
            tires = self.change(tires)
            print tires
        return -1

    def change(self, vals):
        tmp = vals[0]
        vals[0] = vals[3]
        vals[3] = vals[1]
        vals[1] = vals[2]
        vals[2] = tmp
        return vals

# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pfx 2.1.9
import sys
import time
def KawigiEdit_RunTest(testNum, p0, p1, hasAnswer, p2):
    sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str("\"") + str(p0) + str("\"") + str(",") + str("\"") + str(p1) + str("\""))
    print(str("]"))
    obj = TireRotation()
    startTime = time.clock()
    answer = obj.getCycle(p0, p1)
    endTime = time.clock()
    res = True
    print(str("Time: ") + str((endTime - startTime)) + str(" seconds"))
    if (hasAnswer):
        print(str("Desired answer:"))
        print(str("\t") + str(p2))

    print(str("Your answer:"))
    print(str("\t") + str(answer))
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
p0 = "ABCD"
p1 = "ABCD"
p2 = 1
all_right = KawigiEdit_RunTest(0, p0, p1, True, p2) and all_right
# ------------------

# ----- test 1 -----
p0 = "ABCD"
p1 = "DCAB"
p2 = 2
all_right = KawigiEdit_RunTest(1, p0, p1, True, p2) and all_right
# ------------------

# ----- test 2 -----
p0 = "ABCD"
p1 = "CDBA"
p2 = 4
all_right = KawigiEdit_RunTest(2, p0, p1, True, p2) and all_right
# ------------------

# ----- test 3 -----
p0 = "ABCD"
p1 = "ABDC"
p2 = -1
all_right = KawigiEdit_RunTest(3, p0, p1, True, p2) and all_right
# ------------------

# ----- test 4 -----
p0 = "ZAXN"
p1 = "XNAZ"
p2 = 4
all_right = KawigiEdit_RunTest(4, p0, p1, True, p2) and all_right
# ------------------

if (all_right):
    print(str("You're a stud (at least on the example cases)!"))
else:
    print(str("Some of the test cases had errors."))

# PROBLEM STATEMENT
#
# Note to plugin users: there is an image in this problem statement.  Please view the statement in the applet to see the image
#
#
#
# Tire rotation is a simple but effective part of vehicle preventive maintenance.  Without it, the tires of a car may wear out thousands of miles early.  The idea is to have each tire spend part of its life on each wheel of the car.  To accomplish this, the tire on each wheel is moved to another wheel according to a pattern.  First, we assume the wheel positions are numbered left to right, front to rear.  Then we establish a rotation pattern:
#
#
#
#
#
#
#
# From the diagram, we see that for each phase of the rotation cycle, a tire is moved from one wheel position to another, according to the following chart:
#
#
#
# starting      ending
#  wheel        wheel
#    1 ---------> 3
#    2 ---------> 4
#    3 ---------> 2
#    4 ---------> 1
#
#
#
# Therefore, if our four tires are represented by A, B, C, and D, there are four valid phases of the rotation cycle:
#
#
#
# Phase:   1        2        3        4
# Tires:  A B ---> D C ---> B A ---> C D
#         C D      A B      D C      B A
#          ^                          |
#          |__________________________|
#
#
#
# Write a method will take a string initial and a string current, which will both represent the tires on a car.  Each character will be a capital letter ('A'-'Z') and will represent a serial number that identifies a tire.  initial will be the starting locations of the tires, and current will be the current locations.  The position of a character represents the wheel that the tire is on.  The characters represent the wheels in the order: 1, 2, 3, 4 (from the diagram above).  Using the rotation pattern above, your method should return a 1, 2, 3, or 4 if the tires are in the 1st, 2nd, 3rd, or 4th phase of the rotation cycle.  If the tires have been rotated improperly (that is, they are not in any phase), your method should return -1.
#
#
# DEFINITION
# Class:TireRotation
# Method:getCycle
# Parameters:string, string
# Returns:integer
# Method signature:def getCycle(self, initial, current):
#
#
# CONSTRAINTS
# -initial will only contain capital letters ('A' - 'Z', inclusive), and will be exactly 4 characters long.
# -initial will not have any repeated characters.
# -current will be exactly 4 characters long, and will contain the same characters that are in initial.
# -current will not have any repeated characters.
#
#
# EXAMPLES
#
# 0)
# "ABCD"
# "ABCD"
#
# Returns: 1
#
# These tires have not been rotated yet.
#
# 1)
# "ABCD"
# "DCAB"
#
# Returns: 2
#
# The initial locations of the tires are:
#
#
# A B
# C D
# After one rotation, the locations of the tires are:
# D C
# A B
#
# 2)
# "ABCD"
# "CDBA"
#
# Returns: 4
#
# Continuing the rotation, we get the following for phase 3:
#
# B A
# D C
# And finally, on phase 4:
#
#
# C D
# B A
#
# 3)
# "ABCD"
# "ABDC"
#
# Returns: -1
#
#
# Here, the rear two tires were moved incorrectly, and the front two were not moved at all.
#
#
# 4)
# "ZAXN"
# "XNAZ"
#
# Returns: 4
#
# END KAWIGIEDIT TESTING
#Powered by KawigiEdit-pfx 2.1.9!
