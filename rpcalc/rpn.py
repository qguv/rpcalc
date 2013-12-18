#!/usr/bin/env python3
# a reverse polish notation calculator
# for more info, see github.com/qguv/rpcalc

import math
from rpcalc.stack import Stack
from rpcalc.inout import clear

# Getch operations
from rpcalc.inout import getch as rawGetch
def getUserChar():
    '''Gets a single character of user input. Q always quits the program.'''
    rawChar = rawGetch()
    if rawChar == 'Q': # naive escape
        clear()
        print("bye.")
        exit()
    else:
        inpChar = rawChar
    return inpChar

# operator management functions
import rpcalc.operators as ops

def getArgReq(symbol):
    '''Determines amount of arguments required for an operator.'''
    return ops.bindings[symbol][1]

def operate(symbol, stack):
    '''Takes a symbol and a stack, performs the associated operation on the
    stack, and returns any errors.'''
    if stack.canOperate(getArgReq(symbol)):
        # Find associated function
        fn = ops.bindings[symbol][0]
        try:
            return fn(stack)
        except (OverflowError, KeyboardInterrupt):
            return "answer too large to compute!"
    else:
        return "too few entries for " + symbol + "!"

def isNum(string):
    '''Tests whether a string can be converted to a float. Output is
    boolean.'''
    try:
        float(string)
    except ValueError:
        return False
    else:
        return True

def displayView(stack, buf, errors):
    '''If there are errors, display those. Then show the "screen" of the
    calculator.'''
    clear()
    nonErrors = { '', None, '\n' }
    if errors not in nonErrors:
        print(errors)
    stack.rpnView(buf)

def showStack(stack, buf):
    '''Visual representation of the stack.'''
    clear()
    try:
        print(stack)
    except KeyboardInterrupt:
        clear()
        print('too large to display!')
        stack.rpnView(buf)

def operHandler(stack, buf):
    '''Catches input, handles numbers, and detects operators. Executes the
    associated operator if it is a match.'''

    # Initialize operator buffer
    operBuf = buf[-1]

    # Initialize numeric buffer
    buf = buf[:-1]

    # Loops until user finishes typing operator name.
    while operBuf not in ops.bindings.keys():
        operBuf += getUserChar()

        # if e is being used as a power of ten handler
        if (operBuf[0] == 'e') and (operBuf[-1] in \
                {str(i) for i in range(10)} | {"+","-"}):
            # This input is a number; pass back to calling expression
            buf = buf + operBuf
            operBuf = ''
            return (buf,'',False)

        if not any(operBuf in s for s in ops.bindings.keys()):
            # Enter numbers to stack if necessary
            if len(buf) != 0:
                stack.push(float(buf))
            operBuf = ''
            return ('','not an operator! type ? for help.',False)

    else:
        # Enter numbers to stack if necessary
        if len(buf) != 0
            stack.push(float(buf))
        newErrors = operate(operBuf, stack)
        operBuf = ''
        if newErrors is None:
            return ('','',False)
        else:
            return ('',newErrors,False)

def keyHandler(stack, buf, errors):
        '''A series of tests for the most recent buffer entry.  Keys tested
        are: return, backspace, p. Sequences tested are: operators, numbers.'''
        if buf[-1] == '\r': # 'return' key

            # If there aren't any numbers to enter
            if len(buf) == 1:
                # If there is an x register, duplicate x value
                if len(stack) != 0: # if there is an x
                    ops.DupX(stack)
                    return ('','',False)
                # If there is no x register, push 0
                else:
                    stack.push(float(0))
                    return ('','',False)
            # Push numbers in buffer to stack
            else:
                if isNum(buf:[-1]):
                    stack.push(float(buf[:-1]))
                    return ('','',False)
                else:
                    return ('',"not a number!",False)

        elif buf[-1] in ('\x08', '\x7f', '\b'): # backspace
            return (buf[:-2],'',False)
        elif buf == 'p': # Special "print" operator
            return ('','',True)
        elif any( s.startswith(buf[-1]) for s in ops.bindings.keys() ):
        # character just inserted begins an operator
            return operHandler(stack, buf)
        elif (buf[-1] == 'e') and (not isNum(buf[:-1])):
            return ('','not an operator! type ? for help.',False)
        elif buf[-1] not in ({str(i) for i in range(10)} | {".","e"}):
            return ('','not an operator! type ? for help.',False)
        else:
            return (buf,'',False)

def stackLoop(stack, buf, errors, printFlag):
    '''Runs the main loop for an individual stack.  Stack-switching can be
    implemented in the future with another function which is called by main()
    and calls this function.'''
    while True:
        if printFlag:
            # replaces normal print with a view of the stack
            # TODO: this is really ugly
            showStack(stack, buf)
            printFlag = False
        else:
            displayView(stack, buf, errors)
            errors = ''
        buf += getUserChar()
        buf, errors, printFlag = keyHandler(stack, buf, errors)

def main(limit=None, values=None):
    '''Creates a generic stack and runs rpcalc. Takes parameters limit and
    value, which both default to None.'''
    stack = Stack([], 'stack view', limit=limit)
    buf, errors, printFlag = '', '', False
    if values:
        for n in values:
            stack.push(n)
    stackLoop(stack, buf, errors, printFlag)

if __name__ == "__main__":
    main()

