#!/usr/bin/env python3
# rpcalc exceution script
# for more info, see github.com/qguv/rpcalc

"""rpcalc, a reverse polish notation calculator

Usage:
  rpcalc [-s N]
  rpcalc [-s N] -i <NUM>...
  rpcalc -e -i <NUM>...
  rpcalc (-h | --help)
  rpcalc --version

Options:
  -h --help     Show this screen.
  -s N          Limit length of stack to N elements.
  -i            Push following numbers to stack.
  -e            Limit stack length to amount of elements given with -i.
  --version     Display version.

rpcalc is written in Python 3 by Quint Guvernator and licensed by the GPLv3.
For more information, see <http://qguv.github.io/rpcalc>.
"""

VERSION = '0.7.1'

from docopt import docopt

if __name__ == '__main__':
    args = docopt(__doc__, version=VERSION)

import sys, rpcalc

def panic(code, message):
    '''Gives a pretty error message and exits with an error code.'''
    print("\nerror!", message, "\n")
    sys.exit(code)

# Complain if length of stack is less than amount of initial values
if args["-s"] and args["-i"] and args["-s"] < len(args["<NUM>"]):
    panic(2, "too many initial values for allocated stack size")

# Determining length of stack
if args["-e"]:
    stackLength = len(args["<NUM>"])
else:
    try:
        stackLength = int(args["-s"]) or None
    except ValueError:
        stackLength = None

# Determining stack values
if args["-i"]:
    try:
        values = [ float(x) for x in args["<NUM>"] ]
    except ValueError:
        panic(2, "-i (--initial-values) only accepts numbers")
else:
    values = []

# If the stack is limited, pad the values we found above with zeroes to make
# the stack of the desired length
if stackLength:
    if len(values) < stackLength:
        padding = stackLength - len(values)
        padding *= [0.0]
        values = padding + values

sys.exit(rpcalc.main(limit=stackLength, values=values))

