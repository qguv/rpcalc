#!/usr/bin/env python3
# a reverse polish notation calculator
# see github.com/qguv/rpcalc for updates

DEBUG = False

import math
from getch import getch as rawGetch

# Definition of Clear function
import os
clear = lambda: os.system('cls' if os.name=='nt' else 'clear')

def getch():
    rawChar = rawGetch()
    if rawChar == '\r':
        inpChar = "@" #substitute character for <Return>
    elif rawChar == 'q': # naive escape
        print("bye.")
        if not DEBUG: clear()
        exit()
    else:
        inpChar = rawChar
    return inpChar

class Stack:
    '''
    An implementation of the RPN stack in Python3.
    Internally uses a list and negative indexes.
    The most recent input rests at the end of the stack.
    The first input is therefore at the beginning.
    for example, the x register is at [-1]
    the y register is at [-2]
    et cetera
    This is accessed as is intuitive, however:
    >>> myStack.push(5.7005)
    >>> myStack.push(4.8879)
    >>> x = myStack[0]
    >>> print(x)
    4.8879
    '''
    # note: these methods are ordered!
    # references to other methods are
    # given with a comment (ref:).

    def __init__(self, initList, name):
        self.items = initList
        self.name = name

    def __getitem__(self, key):
        backKey = -1 * (key + 1)
        return self.items[backKey]

    def __len__(self):
        return len(self.items)

    def __str__(self): #ref: len
        rep = self.name
        if self.name != '': rep += '\n'
        backList = [ self[i] for i in range(len(self)) ]
        if len(self) != 0:
            longestEntry = max( [ len(str(i)) for i in self.items ] )
        else:
            longestEntry = 3
        rep += '--' * int(math.floor(longestEntry / 2 + 1)) + '-'
        rep += '\n'
        for i in range(len(self.items)):
            rep += ' '
            rep += str(self.items[i])
            rep += '\n'
        rep += '^ ' * int(math.floor(longestEntry / 2 + 1)) + '^'
        #looks like entry point
        return rep

    def linearView(self): #ref: getitem, len
        backList = [ self[i] for i in range(len(self)) ]
        print(str(backList))

    def push(self, item):
        self.items.append(item)

    def pop(self):
        #TODO define "is empty" (re: Alan)
        if len(self) == 0:
            print("empty stack!")
        else:
            return self.items.pop()

    def canOperate(self, argLen):
        if len(self) >= argLen:
            return True
        else:
            return False

    def rpnView(self, buf):
        if not DEBUG: clear()
        if buf != '':         # if buffer exists,
            print(buf)        #   print that
        elif len(self) >= 1: # if there is an x reg,
            print(self[0])   #   print that
        else:
            print(0)          # or just default to 0

import operators as ops

def getArgReq(symbol):
    return ops.bindings[symbol][1]

def operate(symbol, stack):
    if stack.canOperate(getArgReq(symbol)):
        fn = ops.bindings[symbol][0] #get operation fn name
        fn(stack) # absolute magic
    else:
        print("too few entries for", symbol + "!")

def readCalc(stack): # third re-write!
    buf = ''
    printFlag = False #TODO gotta make this work for errors, too
    while True:
        if not printFlag: stack.rpnView(buf) # correct view for HP calcs
        if printFlag:
            # replaces normal print with a view of the stack
            if not DEBUG: clear()
            print(stack)
            printFlag = False
        buf += getch()
        if buf[-1] == '@':
            if len(buf) == 1: # if there aren't any numbers to enter
                if len(stack) != 0: # if there is an x
                    operate("x", stack) # dup X
                else:
                    stack.push(float(0))
            else: # put number in stack
                try:
                    stack.push(float(buf[:-1]))
                except TypeError:
                    print("not a number!")
            buf = ''
        elif buf == 'p': # Special "print" operator
            printFlag = True
            buf = ''
        elif any(buf[-1] in s for s in ops.bindings.keys()):
        # character just inserted is an operator
            if len(buf) != 1: # if there are any numbers to enter
                stack.push(float(buf[:-1]))
            operBuf = buf[-1] # initialize operator buffer
            buf = ''
            while operBuf not in ops.bindings.keys(): # side loop
                operBuf += getch()
                if not any(operBuf in s for s in ops.bindings.keys()):
                    print("not an operator!")
                    operBuf = ''
                    break
            else:
                operate(operBuf, stack)
                operBuf = ''
        elif buf[-1] not in ({str(i) for i in range(10)} | {".","e"}):
            print("type ? for help")
            buf = ''

# DO IT #
mainStack = Stack([], 'Test')
readCalc(mainStack)
