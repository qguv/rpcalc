#!/usr/bin/env python3
# a reverse polish notation calculator
# for more info, see github.com/qguv/rpcalc

import math
from stack import Stack
from inout import clear

errors = ''

# Getch operations
from inout import getch as rawGetch
def getch():
    rawChar = rawGetch()
    if rawChar == 'Q': # naive escape
        clear()
        print("bye.")
        exit()
    else:
        inpChar = rawChar
    return inpChar

# operator management functions
import operators as ops

def getArgReq(symbol):
    return ops.bindings[symbol][1]

def operate(symbol, stack):
    global errors
    if stack.canOperate(getArgReq(symbol)):
        fn = ops.bindings[symbol][0] # get operation fn name
        try:
            errors = fn(stack) # absolute magic
        except OverflowError:
            errors = "answer too large to compute!"
    else:
        errors = "too few entries for " + symbol + "!"

def isNum(string):
    try:
        float(string)
    except ValueError:
        return False
    else:
        return True

# the big guns
def readCalc(stack): # third re-write!
    global errors
    buf = ''
    printFlag = False
    nonErrors = { '', None, '\n' }
    while True:
        if not printFlag:
            clear()
            if errors not in nonErrors:
                print(errors)
            stack.rpnView(buf) # correct view for HP calcs
            errors = ''
        if printFlag:
            # replaces normal print with a view of the stack
            clear()
            print(stack)
            printFlag = False
        buf += getch()
        if buf[-1] == '\r': # return
            if len(buf) == 1: # if there aren't any numbers to enter
                if len(stack) != 0: # if there is an x
                    operate("x", stack) # dup X
                else:
                    stack.push(float(0))
            else: # put number in stack
                try:
                    stack.push(float(buf[:-1]))
                except (TypeError, ValueError):
                    errors="not a number!"
            buf = ''
        elif ( buf[-1] == '\x08' ) or \
             ( buf[-1] == '\x7f' ) or \
             ( buf[-1] == '\b'   ): # handling backspace
            buf = buf[:-2] 
        elif buf == 'p': # Special "print" operator
            printFlag = True
            buf = ''
        elif any( s.startswith(buf[-1]) for s in ops.bindings.keys() ):
        # character just inserted is at least a partial operator
            if len(buf) != 1: # if there are any numbers to enter
                stack.push(float(buf[:-1]))
            operBuf = buf[-1] # initialize operator buffer
            buf = ''
            while operBuf not in ops.bindings.keys(): # side loop
                operBuf += getch()
                if not any(operBuf in s for s in ops.bindings.keys()):
                    errors = "not an operator!"
                    operBuf = ''
                    break
            else:
                operate(operBuf, stack)
                operBuf = ''
        elif (buf[-1] == 'e') and (not isNum(buf[:-1])):
            errors = "not an operator!"
            buf = ''
        elif buf[-1] not in ({str(i) for i in range(10)} | {".","e"}):
            errors = "not an operator!"
            buf = ''

# DO IT #
mainStack = Stack([], 'Stack\nContents')
readCalc(mainStack)
