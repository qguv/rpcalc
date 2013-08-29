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
    '''
    Takes a symbol and a stack, performs the associated
    operation on the stack, and returns any errors.
    '''
    global errors
    if stack.canOperate(getArgReq(symbol)):
        fn = ops.bindings[symbol][0] # get operation fn name
        try:
            return fn(stack) # absolute magic
        except (OverflowError, KeyboardInterrupt):
            return "answer too large to compute!"
    else:
        return "too few entries for " + symbol + "!"

def isNum(string):
    try:
        float(string)
    except ValueError:
        return False
    else:
        return True

def showCalc(stack, buf, errors):
    clear()
    nonErrors = { '', None, '\n' }
    if errors not in nonErrors:
        print(errors)
    stack.rpnView(buf) # correct view for HP calcs

def showStack(stack, buf):
    clear()
    try:
        print(stack)
    except KeyboardInterrupt:
        clear()
        print('too large to display!')
        stack.rpnView(buf)

def operHandler(stack, buf):
    operBuf = buf[-1] # initialize operator buffer
    buf = buf[:-1] # only keep numbers in buffer now
    while operBuf not in ops.bindings.keys(): # side loop
        operBuf += getch()
        if (operBuf[0] == 'e') and (operBuf[-1] in \
                {str(i) for i in range(10)} | {"+","-"}):
        # if e is being used as a power of ten handler
            buf = buf + operBuf # reunite buffer and move on
            operBuf = ''
            return (buf,'',False)
        if not any(operBuf in s for s in ops.bindings.keys()):
            if len(buf) != 0: # if there are any numbers to enter
                stack.push(float(buf))
            operBuf = ''
            return ('','not an operator!',False)
    else:
        if len(buf) != 0: # if there are any numbers to enter
            stack.push(float(buf))
        newErrors = operate(operBuf, stack)
        operBuf = ''
        if newErrors is None:
            return ('','',False)
        else:
            return ('',newErrors,False)

def keyHandler(stack, buf, errors):
        '''
        A series of tests for the most recent buffer entry.
        Keys tested are: return, backspace, p
        Sequences tested are: operators, numbers
        '''
        if buf[-1] == '\r': # return
            if len(buf) == 1: # if there aren't any numbers to enter
                if len(stack) != 0: # if there is an x
                    ops.DupX(stack) # duplicate x
                    return ('','',False)
                else:
                    stack.push(float(0))
                    return ('','',False)
            else: # put number in stack
                try:
                    stack.push(float(buf[:-1]))
                except (TypeError, ValueError):
                    return (buf,"not a number!",False)
                else:
                    return ('','',False)
        elif ( buf[-1] == '\x08' ) or \
             ( buf[-1] == '\x7f' ) or \
             ( buf[-1] == '\b'   ): # handling backspace
            buf = buf[:-2] 
            return (buf[:-2],'',False)
        elif buf == 'p': # Special "print" operator
            return ('','',True)
        elif any( s.startswith(buf[-1]) for s in ops.bindings.keys() ):
        # character just inserted is at least a partial operator
            return operHandler(stack, buf)
        elif (buf[-1] == 'e') and (not isNum(buf[:-1])):
            return ('','not an operator!',False)
        elif buf[-1] not in ({str(i) for i in range(10)} | {".","e"}):
            return ('','not an operator!',False)
        else:
            return (buf,'',False)

# the big guns
def readCalc(stack): # fourth re-write!
    global errors #TODO there has to be a better way
    buf,printFlag = '',False
    while True:
        if printFlag:
            # replaces normal print with a view of the stack
            showStack(stack, buf)
            printFlag = False
        else:
            showCalc(stack, buf, errors)
            errors = ''
        buf += getch() # reads from getch in
        buf, errors, printFlag = keyHandler(stack, buf, errors)


# DO IT #
mainStack = Stack([], 'mainstack')
readCalc(mainStack)
