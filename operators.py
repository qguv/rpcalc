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
    null = stack.pop()

def Clear(stack):
    for i in range(len(stack.items)):
        Drop(stack)

def DupX(stack):
    a = stack.pop()
    stack.push(a)
    stack.push(a)

def SwapXY(stack):
    x = stack.pop()
    y = stack.pop()
    stack.push(x)
    stack.push(y)


#### Arithmetic ####

def Add(stack):
    b = stack.pop()
    a = stack.pop()
    stack.push(a + b)

def Subtract(stack):
    b = stack.pop()
    a = stack.pop()
    stack.push(a - b)

def Multiply(stack):
    b = stack.pop()
    a = stack.pop()
    stack.push(a * b)

def Divide(stack):
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
    a = stack.pop()
    stack.push(-1 * a)

def Modulus(stack):
    b = stack.pop()
    a = stack.pop()
    stack.push(a % b)

def Floor(stack):
    a = stack.pop()
    stack.push(math.floor(a))

def Ln(stack):
    a = stack.pop()
    if a < 0: 
        return "can't ln a negative!"
    else:
        r = math.log(a)
        stack.push(r) # push the answer

def Power(stack):
    b = stack.pop()
    a = stack.pop()
    stack.push(a ** b)

def SqRoot(stack):
    a = stack.pop()
    if (a < 0):
        return "imaginary numbers not supported!"
    else:
        r = math.sqrt(a)
        stack.push(r)

def Absolute(stack):
    a = stack.pop()
    r = abs(a)
    stack.push(r)


#### Constants ####

def ConstPi(stack):
    r = math.pi
    stack.push(r)

def ConstE(stack):
    r = math.e
    stack.push(r)


#### Logic ####

def EqTest(stack):
    b = stack.pop()
    a = stack.pop()
    r = 1 if a == b else 0
    stack.push(r)

def NotTest(stack):
    b = stack.pop()
    a = stack.pop()
    r = 1 if a != b else 0
    stack.push(r)

def LtTest(stack):
    b = stack.pop()
    a = stack.pop()
    r = 1 if a < b else 0
    stack.push(r)

def GtTest(stack):
    b = stack.pop()
    a = stack.pop()
    r = 1 if a > b else 0
    stack.push(r)

def LtEqTest(stack):
    b = stack.pop()
    a = stack.pop()
    r = 1 if a <= b else 0
    stack.push(r)

def GtEqTest(stack):
    b = stack.pop()
    a = stack.pop()
    r = 1 if a >= b else 0
    stack.push(r)


#### Trigonometry ####

def TrigRoundFix(roughAnswer):
# Not an operator, but a helpful
# function that fixes rounding
# errors in Trig functions which
# prevent the expected answers:
# 1, 0, and -1.
    r = roughAnswer
    if abs(r) < 1e-15:
        r = 0.0
    elif abs(r-1) < 1e-15:
        r = 1.0
    elif abs(r+1) < 1e-15:
        r = -1.0
    return r

def Sine(stack):
    a = stack.pop()
    r = math.sin(a)
    r = TrigRoundFix(r)
    stack.push(r)

def Cosine(stack):
    a = stack.pop()
    r = math.cos(a)
    r = TrigRoundFix(r)
    stack.push(r)

def Tangent(stack):
    a = stack.pop()
    r = math.tan(a)
    r = TrigRoundFix(r)
    stack.push(r)

def Arcsine(stack):
    a = stack.pop()
    if (a > 1) or (a < -1):
        return "out of domain!"
    else:
        r = math.asin(a)
        r = TrigRoundFix(r)
        stack.push(r)

def Arccosine(stack):
    a = stack.pop()
    if (a > 1) or (a < -1):
        return "out of domain!"
    else:
        r = math.acos(a)
        r = TrigRoundFix(r)
        stack.push(r)

def Arctangent(stack):
    a = stack.pop()
    r = math.atan(a)
    r = TrigRoundFix(r)
    stack.push(r)

def ToDegrees(stack):
    a = stack.pop()
    r = math.degrees(a)
    stack.push(r)

def ToRadians(stack):
    a = stack.pop()
    r = math.radians(a)
    stack.push(r)


#### Others ####

def Random(stack):
    stack.push(random())

# Bindings cannot include any of the following
# characters for technical reasons: q @ |
# Bindings must not begin with the name of
# another binding. For instance, =< was chosen
# over <= because it does not begin with (and
# therefore does not conflict with) <.
bindings = {
    # Key is the arithmetic keypress
    # Value[0] is the paired function
    # Value[1] is the argument requirement
        #### Stack
        'D' :   [Drop      , 1],
        'C' :   [Clear     , 1],
        'x' :   [DupX      , 1],
        'w' :   [SwapXY    , 2],
        #### Arithmetic
        '+' :   [Add       , 2],
        '-' :   [Subtract  , 2],
        '*' :   [Multiply  , 2],
        '/' :   [Divide    , 2],
        'n' :   [Negate    , 1],
        '%' :   [Modulus   , 2],
        'f' :   [Floor     , 1],
        'ln':   [Ln        , 1],
        '^' :   [Power     , 2],
        'sqrt': [SqRoot    , 1],
        'abs' : [Absolute  , 1],
        #### Constants
        'ke':   [ConstE    , 0],
        'kpi' : [ConstPi   , 0],
        #### Logic
        '==':   [EqTest    , 2],
        '=!':   [NotTest   , 2],
        '<' :   [LtTest    , 2],
        '>' :   [GtTest    , 2],
        '=<':   [LtEqTest  , 2],
        '=>':   [GtEqTest  , 2],
        #### Trigonometry
        'sin' : [Sine      , 1],
        'cos' : [Cosine    , 1],
        'tan' : [Tangent   , 1],
        'asin': [Arcsine   , 1],
        'acos': [Arccosine , 1],
        'atan': [Arctangent, 1],
        'deg' : [ToDegrees , 1],
        'rad' : [ToRadians , 1],
        #### Others
        'rand': [Random    , 0],
        }
