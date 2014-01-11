#!/usr/bin/env python
# rpcalc interactive help file
# for more info, see github.com/qguv/rpcalc

from rpcalc.inout import getch, clear
import rpcalc.operators as ops

intro = '''interactive rpcalc help:

type a command followed by "Return" or
"Enter" for an explanation of its function

or type:
? - list commands
q - leave help
Q - quit rpcalc
'''

pause = "Press any key to continue..."

def getHelp(symbol):
    fn = ops.bindings[symbol][0] # get operation fn name
    print(fn.__doc__)

def main():
    while True:
        clear()
        print(intro)
        sym = input("] ")
        if sym is 'Q':
            clear()
            print("bye.")
            exit()
        elif sym is 'q':
            break
        elif sym is '?':
            for key in ops.bindings.keys():
                print(key)
            null = input(pause)
        elif sym in ops.bindings.keys():
            getHelp(sym)
            null = input(pause)
        else:
            print("not available!")
            null = input(pause)
