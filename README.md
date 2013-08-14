rpcalc
======
A reverse polish notation calculator written in Python 3.


## About
`rpcalc` is destined to be a reverse polish notation calculator based on the HP 11C Scientific Calculator with extended features, such as:
- Unlimited stack length
- User-extendible operators
- An advanced stack datatype


## Operation
`rpcalc` uses a stack for all operations. This document assumes the user is familiar with stack-based calculators; in the future, more thorough documentation may be written for the lay user.

### Concepts
- Numbers are pushed into the stack once `Enter` is pressed or an operation is entered
- Operations are executed as soon as they are typed; **do not** follow operations with `Enter`
- There is no artificial limit placed on stack length. Push 'till the cows come home.
- If in doubt, use the program as you would an 11C, if you are familiar with its operation.

### Operators
_The most recent and second-most recent stack entries will be denoted_ x _and_ y _respectively. You can always peek inside operators.py for a more objective explanation of these functions._

- `p` - prints the stack
- `q` - quits the program, **no matter what**
- `+ - * /` - basic arithmetic operations
- `ln` - returns the natural log of the most recent stack entry (x)
- `c` - clears the stack
- `d` - drops _x_ and pushes stack items down to compensate
- `x` - duplicates _x_ and pushes it (equivalent to `Enter` with an empty buffer)
- `s` - swaps _x_ and _y_
- `%` - returns the remainder of the division of _y_ by _x_
- `^` - returns _y_ to the _xth_ power
- `==` - returns 1 if _x_ is equal to _y_, otherwise returns 0
- `=!` - returns 0 if _x_ is equal to _y_, otherwise returns 1
- `<` - returns 1 if _y_ is less than _x_, otherwise returns 0
- `>` - returns 1 if _y_ is greater than _x_, otherwise returns 0
- `=<` - returns 1 if _y_ is less than or equal to _x_, otherwise returns 0
- `=>` - returns 1 if _y_ is greater than or equal to _x_, otherwise returns 0

Other operations can easily be added by modifying `operators.py`.

### Examples
_Results are designated with `>>>`, but these are really stored in the stack and displayed only because they are the current_ x _value._

    1 Enter 2 +
    >>> 3.0

    2 Enter Enter Enter * *
    >>> 8.0
    
    10 ln
    >>> 2.302585092994046
    
    256 ln 2 ln /
    >>> 8.0
    
    2 Enter 256 ln s ln /
    >>> 8.0
    
    2 Enter 3 ==
    >>> 0
    
    2 Enter Enter ==
    >>> 1

## Motivation
At time of writing (August 2013), no stack-based RPN existed with the features and extensibility for which the author was looking. This project is meant to be a test of git, GitHub, Python 3, and Object-Oriented Programming in general.

-[qguv](http://github.com/qguv/)
