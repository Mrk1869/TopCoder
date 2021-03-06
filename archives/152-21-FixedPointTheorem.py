import math
import string

class FixedPointTheorem:
    def cycleRange(self, R):
        x = 0.25
        for i in range(200000):
            x = self.cal(R, x)
        min = x
        max = x
        for i in range(200000, 201001):
            x = self.cal(R, x)
            if x > max:
                max = x
            if x < min:
                min = x
        return max - min

    def cal(self, R, x):
        return R * x * (1 - x)

# BEGIN KAWIGIEDIT TESTING
# Generated by KawigiEdit-pfx 2.1.9
import sys
import time
def KawigiEdit_RunTest(testNum, p0, hasAnswer, p1):
    sys.stdout.write(str("Test ") + str(testNum) + str(": [") + str(p0))
    print(str("]"))
    obj = FixedPointTheorem()
    startTime = time.clock()
    answer = obj.cycleRange(p0)
    endTime = time.clock()
    res = True
    print(str("Time: ") + str((endTime - startTime)) + str(" seconds"))
    if (hasAnswer):
        print(str("Desired answer:"))
        print(str("\t") + str(p1))

    print(str("Your answer:"))
    print(str("\t") + str(answer))
    if (hasAnswer):
        res = answer == answer and abs(p1 - answer) <= 1e-9 * max(1.0, abs(p1))

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
p0 = 0.1
p1 = 0.0
all_right = KawigiEdit_RunTest(0, p0, True, p1) and all_right
# ------------------

# ----- test 1 -----
p0 = 3.05
p1 = 0.14754098360655865
all_right = KawigiEdit_RunTest(1, p0, True, p1) and all_right
# ------------------

# ----- test 2 -----
p0 = 3.4499
p1 = 0.4175631735867292
all_right = KawigiEdit_RunTest(2, p0, True, p1) and all_right
# ------------------

# ----- test 3 -----
p0 = 3.55
p1 = 0.5325704489850351
all_right = KawigiEdit_RunTest(3, p0, True, p1) and all_right
# ------------------

# ----- test 4 -----
p0 = 3.565
p1 = 0.5454276003030636
all_right = KawigiEdit_RunTest(4, p0, True, p1) and all_right
# ------------------

# ----- test 5 -----
p0 = 3.5689
p1 = 0.5489996297493569
all_right = KawigiEdit_RunTest(5, p0, True, p1) and all_right
# ------------------

# ----- test 6 -----
p0 = 3.00005
p1 = 0.004713996108955176
all_right = KawigiEdit_RunTest(6, p0, True, p1) and all_right
# ------------------

if (all_right):
    print(str("You're a stud (at least on the example cases)!"))
else:
    print(str("Some of the test cases had errors."))

# PROBLEM STATEMENT
# The fixed-point theorem is one of those cornerstones of mathematics that reaches towards all disciplines, and oddly enough it is also closely related to the ability of any program to Quine itself (or to print out its own source code). Put simply, the fixed-point theorem states that with certain restrictions on a real-valued function F, there is always a point such that X=F(X). Taking the fixed-point theorem further, you can show that any function that meets certain restrictions will start to cycle through values if you keep on feeding it its own output (doing this with programs and their output is one way of producing programs that Quine themselves).
#  One simple function that does this is the logistic function F(X)=R*X*(1-X) in the interval [0,1] for certain values of R. For example, if you start with the value X=.25 and feed it into F to get a new X, then feed that value into F to get yet another X, and so on, the values of X that are produced will converge to a small set of values that will eventually repeat forever, called a cycle.
#
# Your program will be given a float R between 0.1 and 3.569 inclusive. Starting with X=.25, generate the first 200,000 iterations of F using the given value of R, which will stabilize values of X. Then generate 1000 more values, and return the range of these values (highest value - lowest value).  In other words, you will be finding the range of the values produced between iterations 200,001 and 201,000 inclusive.
#
# DEFINITION
# Class:FixedPointTheorem
# Method:cycleRange
# Parameters:float
# Returns:float
# Method signature:def cycleRange(self, R):
#
#
# NOTES
# -Don't worry about overflow. With the given values it'll never happen.
#
#
# CONSTRAINTS
# -R will be a value between 0.1 and 3.569 inclusive.
# -R will always be a value such that the process stated above will produce a result accurate to 1e-9 (absolute or relative).
#
#
# EXAMPLES
#
# 0)
# 0.1
#
# Returns: 0.0
#
# At low numbers, there exists only one point in the cycle, so the answer is 0.0.
#
# 1)
# 3.05
#
# Returns: 0.14754098360655865
#
# 2)
# 3.4499
#
# Returns: 0.4175631735867292
#
# 3)
# 3.55
#
# Returns: 0.5325704489850351
#
# 4)
# 3.565
#
# Returns: 0.5454276003030636
#
# 5)
# 3.5689
#
# Returns: 0.5489996297493569
#
# 6)
# 3.00005
#
# Returns: 0.004713996108955176
#
# Make sure you're iterating 200,000 times.
#
# END KAWIGIEDIT TESTING
#Powered by KawigiEdit-pfx 2.1.9!
