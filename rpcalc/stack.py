#!/usr/bin/env python3
# the stack class for rpcalc
# for more info, see github.com/qguv/rpcalc

import math
from rpcalc.inout import clear

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
    def __init__(self, initList, name, limit=None):
        self.items = initList
        self.name = name
        self.limit = limit

    def __getitem__(self, key):
        backKey = -1 * (key + 1)
        return self.items[backKey]

    def __len__(self):
        return len(self.items)

    def __str__(self): #ref: len
        rep = self.name
        if self.name != '': rep += '\n'
        if self.limit:
            rep += "limited to " + str(self.limit) + " entries\n"
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
        rep += '\n'
        rep += '^ ' * int(math.floor(longestEntry / 2 + 1)) + '^'
        #looks like entry point
        return rep

    def linearView(self): #ref: getitem, len
        backList = [ self[i] for i in range(len(self)) ]
        print(str(backList))

    def clear(self):
        if self.limit:
            self.items = self.limit * [0.0]
        else:
            self.items = list()

    def push(self, item):
        self.items.append(item)
        # If there is a stack size limit and the stack is overfull, erase the
        # oldest entry
        if self.limit:
            if len(self) > self.limit:
                self.items = self.items[1:]

    def pop(self):
        #TODO define "is empty"
        if len(self) == 0:
            print("empty stack!") #FIXME does this do anything?
        elif self.limit:
            # With a limited stack, we duplicate the topmost (oldest) entry
            # when the pop operation is called
            toReturn = self.items.pop()
            newList = [ self.items[0] ]
            newList.extend(self.items)
            self.items = newList
            return toReturn
        elif not self.limit:
            # With an unlimited stack, we simply call the appropriate pop
            # method on the underlying list
            return self.items.pop()

    def canOperate(self, argLen):
        if len(self) >= argLen:
            return True
        else:
            return False

    def rpnView(self, buf):
        if buf != '':         # if buffer exists,
            print(buf)        #   print that
        elif len(self) >= 1: # if there is an x reg,
            print(self[0])   #   print that
        else:
            print(0)          # or just default to 0

