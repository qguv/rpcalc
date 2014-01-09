#!/usr/bin/env python3
# rpcalc exceution script
# for more info, see github.com/qguv/rpcalc

"""rpcalc, a reverse polish notation calculator

Usage:
  rpcalc [-s N] [-i X ...]
  rpcalc [-e] -i X ...
  rpcalc (-h | --help)
  rpcalc --version

Options:
  -h --help     Show this screen.
  -s N          Limit length of stack to N elements.
  -i X ...      Push following elements to stack.
  -e            Limit stack length to amount of elements given with -i.
  --version     Display version.

rpcalc is written in Python 3 by Quint Guvernator and licensed by the GPLv3.
For more information, see <http://qguv.github.io/rpcalc>.
"""

VERSION = '0.7.1'

from docopt import docopt

if __name__ == '__main__':
    args = docopt(__doc__, version=VERSION)
    print(args)

import sys, rpcalc

def panic(code, message):
    '''Gives a pretty error message and exits with an error code.'''
    print("\nerror!", message, "\n")
    sys.exit(code)

# Get version and exit if --version is called
if args.version:
    print(VERSION)
    sys.exit()

# Complain if -e given without -i or with -s
if args.exclusive and not args.initial_values:
    panic(2, "-e (--exclusive) can only be used with -i (--initial-values)")
elif args.exclusive and args.stack_size:
    panic(2, "-e (--exclusive) can not be used with -s (--stack-size)")

# Complain if length of stack is less than amount of initial values
if args.stack_size and args.initial_values:
    if args.stack_size < len(args.initial_values):
        panic(2, "too many initial values for allocated stack size")

# Determining length of stack
if args.exclusive:
    stackLength = len(args.initial_values)
else:
    stackLength = args.stack_size or None

# Determining stack values
if args.initial_values:
    try:
        values = [ float(x) for x in args.initial_values ]
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

