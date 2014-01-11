#!/usr/bin/env python3
# I/O functions for rpcalc
# for more info, see github.com/qguv/rpcalc

# definition of Clear function
import os
clear = lambda: os.system("cls" if os.name=="nt" else "clear")

# Getch function written by Danny Yoo
# http://code.activestate.com/recipes/134892/
class _Getch:
    '''Gets a single character from standard input.  Does not echo to the
    screen.'''
    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()
    def __call__(self): return self.impl()

class _GetchUnix:
    def __init__(self):
        import tty, sys
    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

class _GetchWindows:
    def __init__(self):
        import msvcrt
    def __call__(self):
        import msvcrt
        byteLiteral = msvcrt.getch()
        return byteLiteral.decode("latin1")

getch = _Getch()
