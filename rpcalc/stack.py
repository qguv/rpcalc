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

    def __init__(self, initList, name, limit=None):
        self.items = initList
        self.name = name
        self.limit = limit

    def __getitem__(self, key):
        '''Implements slicing.'''
        backKey = -1 * (key + 1)
        return self.items[backKey]

    def __len__(self):
        '''Implements len().'''
        return len(self.items)

    def __str__(self):
        '''Implements str().'''
        rep = self.name
        if self.name != '':
            rep += '\n'
        if self.limit:
            rep += "limited to " + str(self.limit) + " entries\n"
        backList = [self[i] for i in range(len(self))]
        if len(self) != 0:
            longestEntry = max([len(str(i)) for i in self.items])
        else:
            longestEntry = 3
        rep += "--" * int(math.floor(longestEntry / 2 + 1)) + '-'
        rep += '\n'
        for i in range(len(self.items)):
            rep += ' '
            rep += str(self.items[i])
            rep += '\n'
        rep += '\n'
        rep += "^ " * int(math.floor(longestEntry / 2 + 1)) + '^'
        return rep

    def linearView(self):
        '''Displays stack visually on a single line. Newer entries are on the
        right.'''
        return self.items

    def clear(self):
        '''Clears stack. If there's a limit, fill with 0s. Otherwise, deletes
        all entries.'''
        if self.limit:
            self.items = self.limit * [0.0]
        else:
            self.items = list()

    def push(self, item):
        '''Push a value to the stack. If there is a stack size limit and the
        stack is overfull, this erases the oldest entry.'''
        self.items.append(item)
        if self.limit:
            if len(self) > self.limit:
                self.items = self.items[1:]

    def pop(self):
        '''Pops most recent item from stack. If there is a stack size limit,
        this duplicates the oldest entry.'''
        if len(self) == 0:
            raise IndexError("empty stack!")
        elif self.limit:
            toReturn = self.items.pop()
            newList = [self.items[0]]
            newList.extend(self.items)
            self.items = newList
            return toReturn
        elif not self.limit:
            return self.items.pop()

    def canOperate(self, argLen):
        '''Tests whether stack is greater than or equal to a certain size.'''
        if len(self) >= argLen:
            return True
        else:
            return False

    def rpnView(self, buf):
        '''If buffer exists, print it.
        If there is an x register, print it.
        Print 0 as a last resort.'''
        if buf != '':
            print(buf)
        elif len(self) >= 1:
            print(self[0])
        else:
            print(0)
