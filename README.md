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

### Installation & Execution
You will need Python 3.3 to run `rpcalc`. As there are currently no `rpcalc` binaries, simply download the necessary files from the [git repository](http://github.com/qguv/rpcalc/). Switch to the `rpcalc/` directory, and run the following from a command shell:

    python3 rpn.py

It is possible that your system calls your Python 3.3 binary something different, such as `python` (ArchLinux) or `py33.exe` (some Windows). If this is the case, replace `python3` in the above example with the proper executable. Google is your friend here.

### Concepts
- Numbers are pushed into the stack once `Enter` is pressed or an operation is entered
- Operations are executed as soon as they are typed; **do not** follow operations with `Enter`
- There is no artificial limit placed on stack length. Push 'till the cows come home.
- If in doubt, use the program as you would an 11C, if you are familiar with its operation.

### Operators
_The most recent and second-most recent stack entries will be denoted_ x _and_ y _respectively. You can always peek inside operators.py for a more objective explanation of these functions._

#### Program
- `p` - prints the stack
- `Q` - quits the program, **no matter what**

#### Stack
- `D` - drops _x_ and pushes stack items to compensate
- `C` - clears the stack
- `x` - duplicates _x_ and pushes it (equivalent to `Enter` with an empty buffer)
- `w` - swaps _x_ and _y_

#### Arithmetic
- `+ - * /` - basic arithmetic operations
- `n` - returns (_x_ * -1)
- `%` - returns the remainder of the division of _y_ by _x_
- `f` - floor-rounds _x_ to an integer
- `ln` - returns the natural log of the most recent stack entry (_x_)
- `^` - returns _y_ to the _xth_ power
- `sqrt` - returns the square root of _x_
- `abs` - returns the absolute value of _x_
- `!` - returns the factorial of _x_

#### Sequence Operators
- `S` - returns the sum of all stack entries
- `P` - returns the product of all stack entries

#### Constants
_in `rpcalc`, constant operators begin with `k` to prevent conflicts with other operators_

- `ke` - returns [Euler's number](http://en.wikipedia.org/wiki/E_%28mathematical_constant%29): the base of the natural logarithm and the exponential function
- `kpi` - returns [pi](http://en.wikipedia.org/wiki/Pi): the ratio of a circle's circumference to its diameter

#### Logic
- `==` - returns 1 if _x_ is equal to _y_, otherwise returns 0
- `=!` - returns 0 if _x_ is equal to _y_, otherwise returns 1
- `<` - returns 1 if _y_ is less than _x_, otherwise returns 0
- `>` - returns 1 if _y_ is greater than _x_, otherwise returns 0
- `=<` - returns 1 if _y_ is less than or equal to _x_, otherwise returns 0
- `=>` - returns 1 if _y_ is greater than or equal to _x_, otherwise returns 0

#### Trigonometry
- `deg` - converts _x_ (radians) to degrees
- `rad` - converts _x_ (degrees) to radians
- `sin` - returns the sine of _x_ (radians)
- `cos` - returns the cosine of _x_ (radians)
- `tan` - returns the tangent of _x_ (radians)
- `asin` - returns the arcsine of _x_ (radians)
- `acos` - returns the arccosine of _x_ (radians)
- `atan` - returns the arctangent of _x_ (radians)

#### Other
- `rand` - returns a random number between 0 and 1

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

### Known Issues
- In-program help (`?`) is not yet supported.

## FAQ
> **How do I do log base _x_?**

A `log` function is not scheduled to be implemented because the functionality is _already there_ and because there is no reason to memorize which stack item will be the base and on which item the log will operate.

You will need to use the _change of base formula_:

![Logarithmic Change of Base Formula](resources/logCOB.png)

    256 ln 2 ln /

> **I have a bug! Let me email that to you...**

Thank you, but please don't email me the bug! Make sure it's not a [known issue](#known-issues), and write me a bug report [here](https://github.com/qguv/rpcalc/issues/new) or if you're familiar with git: fork, fix, and file a pull request.

## Motivation
At time of writing (August 2013), no stack-based RPN existed with the features and extensibility for which the author was looking. This project is meant to be a test of git, GitHub, vim, my workflow, Python 3, and Object-Oriented Programming in general.

-[Quintus](http://github.com/qguv/)
