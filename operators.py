#!/usr/bin/env python3
# rpcalc operators using stack datatype
# for more info, see github.com/qguv/rpcalc

import math
from random import random

# Add your own! Make sure to add a binding too.
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
    try:
        r = a / b
    except ZeroDivisionError:
        # return operators to stack
        stack.push(a)
        stack.push(b)
        return "can't divide by 0!"
    else:
        stack.push(r)

def Negate(stack):
    a = stack.pop()
    stack.push(-1 * a)

def Random(stack):
    stack.push(random())

def Floor(stack):
    a = stack.pop()
    stack.push(math.floor(a))

def Ln(stack):
    a = stack.pop()
    try:
        r = math.log(a)
    except ValueError:
        return "can't ln a negative!"
        stack.push(a) # return the number
    else:
        stack.push(r) # push the answer

def Clear(stack):
    for i in range(len(stack.items)):
        Drop(stack)

def Drop(stack):
    null = stack.pop()

def DupX(stack):
    a = stack.pop()
    stack.push(a)
    stack.push(a)

def SwapXY(stack):
    x = stack.pop()
    y = stack.pop()
    stack.push(x)
    stack.push(y)

def Power(stack):
    b = stack.pop()
    a = stack.pop()
    stack.push(a ** b)

def Modulus(stack):
    b = stack.pop()
    a = stack.pop()
    stack.push(a % b)

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

# Bindings cannot include any of the following
# characters for technical reasons: q @
# Bindings must not begin with the name of
# another binding. For instance, =< was chosen
# over <= because it does not begin with (and
# therefore does not conflict with) <.
bindings = {
    # Key is the arithmetic keypress
    # Value[0] is the paired function
    # Value[1] is the argument requirement
        '+' :   [Add       , 2],
        '-' :   [Subtract  , 2],
        '*' :   [Multiply  , 2],
        '/' :   [Divide    , 2],
        'n' :   [Negate    , 1],
        'r' :   [Random    , 0],
        'f' :   [Floor     , 1],
        'ln':   [Ln        , 1],
        'd' :   [Drop      , 1],
        'c' :   [Clear     , 1],
        'x' :   [DupX      , 1],
        's' :   [SwapXY    , 2],
        '%' :   [Modulus   , 2],
        '^' :   [Power     , 2],
        '==':   [EqTest    , 2],
        '=!':   [NotTest   , 2],
        '<' :   [LtTest    , 2],
        '>' :   [GtTest    , 2],
        '=<':   [LtEqTest  , 2],
        '=>':   [GtEqTest  , 2],
        }
