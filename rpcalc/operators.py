#!/usr/bin/env python3
# rpcalc operators using stack datatype
# for more info, see github.com/qguv/rpcalc

# If an error is thrown in a binary operation,
# the erroneous operator is discarded and the
# proper operator is kept.

# If an error is thrown in a unary operation,
# the operator is discarded.

import math
from random import random

# Add your own here! Make sure to add a binding too.


#### Stack ####

def Drop(stack):
    '''
    Discards the most recent stack entry.
    '''
    null = stack.pop()

def Clear(stack):
    '''
    Discards all stack items, emptying the stack.
    '''
    stack.items = list()

def Length(stack):
    '''
    Displays the entries in the stack.
    '''
    stackLength = len(stack)
    if stackLength == 1:
        return stack.name + " has 1 entry."
    elif stackLength == 0:
        return stack.name + " is empty."
    else:
        return stack.name + " has " + str(stackLength) + " entries."

def DupX(stack):
    '''
    Pushes a copy of the newest entry to the stack.
    '''
    a = stack.pop()
    stack.push(a)
    stack.push(a)

def SwapXY(stack):
    '''
    Swaps the values of the most recently entered stack item
    and the second-most recently entered stack item.
    '''
    x = stack.pop()
    y = stack.pop()
    stack.push(x)
    stack.push(y)


#### Arithmetic ####

def Add(stack):
    '''
    Combines the most recent two stack entries by summing.
    '''
    b = stack.pop()
    a = stack.pop()
    stack.push(a + b)

def Subtract(stack):
    '''
    Combines the most recent two stack entries by subtracting
    the more recent from the older.
    '''
    b = stack.pop()
    a = stack.pop()
    stack.push(a - b)

def Multiply(stack):
    '''
    Combines the most recent two stack entries by multiplying.
    '''
    b = stack.pop()
    a = stack.pop()
    stack.push(a * b)

def Divide(stack):
    '''
    Combines the most recent two stack entries by dividing
    the older by the more recent.
    '''
    b = stack.pop()
    a = stack.pop()
    if b == 0:
        stack.push(a) # return dividend to stack
        # divisor (0) gets the boot
        return "can't divide by 0!"
    else:
        r = a / b
        stack.push(r)

def Negate(stack):
    '''
    Multiplies the most recent entry by -1.
    '''
    a = stack.pop()
    stack.push(-1 * a)

def Modulus(stack):
    '''
    Replaces the most recent two stack items with the remainder
    given by dividing the older entry by the more recent.
    '''
    b = stack.pop()
    a = stack.pop()
    stack.push(a % b)

def Floor(stack):
    '''
    Rounds the most recent stack entry down to an integer.
    '''
    a = stack.pop()
    stack.push(math.floor(a))

def Ln(stack):
    '''
    Finds the natural logarithm of the most recent stack
    entry and replaces the entry with the result.
    '''
    a = stack.pop()
    if a <= 0: 
        return "out of domain!"
    else:
        r = math.log(a)
        stack.push(r) # push the answer

def Power(stack):
    '''
    Replaces the most recent two stack items with the value
    of the older to the newer's power.
    '''
    b = stack.pop()
    a = stack.pop()
    stack.push(a ** b)

def SqRoot(stack):
    '''
    Finds the square root of the most recent stack entry
    and replaces the entry with the result.
    '''
    a = stack.pop()
    if (a < 0):
        return "imaginary numbers not supported!"
    else:
        r = math.sqrt(a)
        stack.push(r)

def Absolute(stack):
    '''
    If the most recent stack entry is negative, it is
    replaced with the entry multiplied by -1.
    '''
    a = stack.pop()
    r = abs(a)
    stack.push(r)

def Factorial(stack):
    '''
    Finds the factorial of the most recent stack entry
    and replaces the entry with the result.
    '''
    a = stack.pop()
    if (a < 0):
        return "out of domain!"
    elif (int(a) != a):
        return "not integral!"
    else:
        r = math.factorial(int(a))
        stack.push(r)


#### Sequence Operators ####

def MakeList(stack):
# another utility function,
# this time for sequences
    r = [ stack.pop() for null in range(len(stack)) ]
    return r

def Summation(stack):
    '''
    Sums all stack entries, clears the stack, and
    pushes the result.
    '''
    r = math.fsum(MakeList(stack))
    stack.push(r)

def Product(stack):
    '''
    Sums all stack entries, clears the stack, and
    pushes the result.
    '''
    seq = MakeList(stack)
    r = 1
    for element in seq:
        r = r * element
    stack.push(r)


#### Statistics ####

def Mean(stack):
    '''
    Finds the arithmetic mean of all stack entries,
    clears the stack, and pushes the result.
    '''
    seq = MakeList(stack)
    r = sum(seq) / len(seq)
    stack.push(r)

def Median(stack):
    '''
    Finds the median of all stack entries, clears
    the stack, and pushes the result.
    '''
    ord = sorted(MakeList(stack))
    if len(ord) % 2 == 1:
    # if only one middle number, return that
        choose = math.floor(len(ord) / 2)
        r = ord[choose]
    else:
    # if two middle numbers, return average
        iE = int(len(ord) / 2 + 1)
        iS = iE - 2
        r = sum(ord[iS:iE]) / 2
    stack.push(r)


#### Constants ####

def ConstPi(stack):
    '''
    Pushes "Pi" to the stack.
    '''
    r = math.pi
    stack.push(r)

def ConstE(stack):
    '''
    Pushes "Euler's Number" to the stack.
    '''
    r = math.e
    stack.push(r)


#### Logic ####

def CloseEnough(a, b, epsilon=1e-12):
    '''
    Not an operator, but a utility function which compares floats and checks
    for close-equality. This corrects for internal float rounding error.
    '''
    from math import fabs
    return fabs(a - b) < epsilon

def EqTest(stack):
    '''
    Returns 1 if the most recent two stack
    entries are identical. Otherwise returns 0.
    '''
    b = stack.pop()
    a = stack.pop()
    r = 1 if CloseEnough(a, b) else 0
    stack.push(r)

def NotTest(stack):
    '''
    Returns 0 if the most recent two stack
    entries are identical. Otherwise returns 1.
    '''
    b = stack.pop()
    a = stack.pop()
    r = 0 if CloseEnough(a, b) else 1
    stack.push(r)

def LtTest(stack):
    '''
    Returns 1 if the second-newest stack entry is
    less than the newest. Otherwise returns 0.
    '''
    b = stack.pop()
    a = stack.pop()
    if CloseEnough(a, b):
        r = 0
    elif a < b:
        r = 1
    else:
        r = 0
    stack.push(r)

def GtTest(stack):
    '''
    Returns 1 if the second-newest stack entry is
    greater than the newest. Otherwise returns 0.
    '''
    b = stack.pop()
    a = stack.pop()
    if CloseEnough(a, b):
        r = 0
    elif a > b:
        r = 1
    else:
        r = 0
    stack.push(r)

def LtEqTest(stack):
    '''
    Returns 1 if the second-newest stack entry is
    no greater than the newest. Otherwise returns 0.
    '''
    b = stack.pop()
    a = stack.pop()
    if CloseEnough(a, b):
        r = 1
    elif a < b:
        r = 1
    else:
        r = 0
    stack.push(r)

def GtEqTest(stack):
    '''
    Returns 1 if the second-newest stack entry is
    no less than the newest. Otherwise returns 0.
    '''
    b = stack.pop()
    a = stack.pop()
    if CloseEnough(a, b):
        r = 1
    elif a > b:
        r = 1
    else:
        r = 0
    stack.push(r)


#### Trigonometry ####

def TrigRoundFix(roughAnswer):
    '''
    Not an operator, but a utility function that fixes
    rounding errors in trigonometric functions which
    prevent tne expected answers 1, 0, and -1.
    '''
    r = roughAnswer
    if abs(r) < 1e-15:
        r = 0.0
    elif abs(r-1) < 1e-15:
        r = 1.0
    elif abs(r+1) < 1e-15:
        r = -1.0
    return r

def Sine(stack):
    '''
    Returns the trigonometric "sin()" of the most recent
    stack entry, in radians.
    '''
    a = stack.pop()
    r = math.sin(a)
    r = TrigRoundFix(r)
    stack.push(r)

def Cosine(stack):
    '''
    Returns the trigonometric "cos()" of the most recent
    stack entry, in radians.
    '''
    a = stack.pop()
    r = math.cos(a)
    r = TrigRoundFix(r)
    stack.push(r)

def Tangent(stack):
    '''
    Returns the trigonometric "tan()" of the most recent
    stack entry, in radians.
    '''
    a = stack.pop()
    r = math.tan(a)
    r = TrigRoundFix(r)
    stack.push(r)

def Arcsine(stack):
    '''
    Returns the trigonometric "arcsin()" of the most recent
    stack entry, in radians.
    '''
    a = stack.pop()
    if (a > 1) or (a < -1):
        return "out of domain!"
    else:
        r = math.asin(a)
        r = TrigRoundFix(r)
        stack.push(r)

def Arccosine(stack):
    '''
    Returns the trigonometric "arccos()" of the most recent
    stack entry, in radians.
    '''
    a = stack.pop()
    if (a > 1) or (a < -1):
        return "out of domain!"
    else:
        r = math.acos(a)
        r = TrigRoundFix(r)
        stack.push(r)

def Arctangent(stack):
    '''
    Returns the trigonometric "arctan()" of the most recent
    stack entry, in radians.
    '''
    a = stack.pop()
    r = math.atan(a)
    r = TrigRoundFix(r)
    stack.push(r)

def ToDegrees(stack):
    '''
    Converts a stack entry from radians to degrees.
    '''
    a = stack.pop()
    r = math.degrees(a)
    stack.push(r)

def ToRadians(stack):
    '''
    Converts a stack entry from degrees to radians.
    '''
    a = stack.pop()
    r = math.radians(a)
    stack.push(r)


#### Others ####

def Random(stack):
    '''
    Returns a pseudo-random number from 0 to 1.
    '''
    stack.push(random())

def DebugIter(stack):
    '''
    A debug function. May break rpcalc.
    '''
    a = stack.pop()
    a = int(math.floor(a))
    if a > 1:
        for i in range(1, (a + 1)):
            stack.push(i)
        return "pushed " + str(a) + " entries."
    elif a == 1:
        stack.push(1)
        return "pushed 1 entry."
    elif a == 0:
        return "pushed 0 entries."
    elif a < 0:
        return "xkcd.com/1245 !"

def Help(stack):
    '''
    Displays interactive help for on-board and
    extended functions.
    '''
    import rpcalc.help
    rpcalc.help.main()
    return "returning to " + stack.name + '.'

def ExitHelp(stack):
    return "use Shift+Q (capital Q) to quit. type ? for help."

# Bindings cannot include any of the following
# characters for technical reasons: Q p
# Bindings must not begin with the name of
# another binding. For instance, =< was chosen
# over <= because it does not begin with (and
# therefore does not conflict with) <.

# Key is the arithmetic keypress
# Value[0] is the paired function
# Value[1] is the argument requirement

from collections import OrderedDict
bindings = OrderedDict((
#### Stack
    ('D', (Drop, 1)),
    ('C', (Clear, 0)),
    ('#', (Length, 0)),
    ('w', (SwapXY, 2)),
#### Arithmetic
    ('+', (Add, 2)),
    ('-', (Subtract, 2)),
    ('*', (Multiply, 2)),
    ('x', (Multiply, 2)),
    ('/', (Divide, 2)),
    ('n', (Negate, 1)),
    ('%', (Modulus, 2)),
    ('f', (Floor, 1)),
    ('ln', (Ln, 1)),
    ('^', (Power, 2)),
    ('sqrt', (SqRoot, 1)),
    ('abs', (Absolute, 1)),
    ('!', (Factorial, 1)),
#### Sequence Operators
    ('S', (Summation, 1)),
    ('P', (Product, 1)),
#### Statistics
    ('mean', (Mean, 1)),
    ('med', (Median, 1)),
#### Constants
    ('ke', (ConstE, 0)),
    ('kpi', (ConstPi, 0)),
#### Logic
    ('==', (EqTest, 2)),
    ('=!', (NotTest, 2)),
    ('<', (LtTest, 2)),
    ('>', (GtTest, 2)),
    ('=<', (LtEqTest, 2)),
    ('=>', (GtEqTest, 2)),
#### Trigonometry
    ('sin', (Sine, 1)),
    ('cos', (Cosine, 1)),
    ('tan', (Tangent, 1)),
    ('asin', (Arcsine, 1)),
    ('acos', (Arccosine, 1)),
    ('atan', (Arctangent, 1)),
    ('deg', (ToDegrees, 1)),
    ('rad', (ToRadians, 1)),
#### Others
    ('rand', (Random, 0)),
    ('debug', (DebugIter, 1)),#DEBUG
    ('?', (Help, 0)),
    ('', (ExitHelp, 0)),
))

