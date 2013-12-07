#!/usr/bin/env python3
# rpcalc exceution script
# for more info, see github.com/qguv/rpcalc

import sys, rpcalc, argparse

longComment = '''
there will be five ways to execute rpcalc:

    rpcalc
        does what you'd expect

    rpcalc -s l
        sets a stack length restriction of n

    rpcalc -i n
        pushes a list of comma-separated initial values in the stack

    rpcalc -s l -i n
    rpcalc -i n -s l
        as long as len(n) is less than l, sets the stack length to l and initializes n

    rpcalc -ei n
        sets the stack length to len(n) and initializes n
'''

parser = argparse.ArgumentParser(prog='rpcalc',
    description="A reverse polish notation calculator written in Python 3.",
    epilog="For more information, see qguv.github.io/rpcalc")

parser.add_argument("-s", "--stack-size",
    help="Limits the stack to a certain number of entries",
    action="store_true")

parser.add_argument("-i", "--initial-values",
    help="Initializes the stack with certain values already pushed. Accepts numbers separated by commas. Values are pushed in order.",
    action="append")

sys.exit(rpcalc.main())

