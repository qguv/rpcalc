Changelog
=========

## _NEXT RELESASE_

## Version 0.3.3

### Fixes:
- fixed duplication bug

## Version 0.3.2

### Fixes:
- fixed some oddities in documentation after public feedback
- added a comprehensive developer commit checklist `develop.md`

## Version 0.3.1

### Additions:
- documentation improvements

### Modifications:
- changed `x` to be a shortcut for `*`

## Version 0.3

### Additions:
- new constants, accessed through a `k` prefix: `kpi` and `ke`
- new sequence operators: stack summation is `S`, stack product is `P`.
- new statistics operators: arithmetic mean is `mean`, median is `med`
- new factorial operator: `!`
- new stack length button: `#` (does not push anything to the stack)

### Fixes:
- fixed backspace not working on all systems
- fixed ambiguous 'e': now detects whether e denotes a power of ten or an operator
- fixed `KeyboardInterrupt` on operators that take a _looong_ time
- sped up some time-consuming functions

## Version 0.2.2

### Fixes:
- when typing an operator, the partial-operator matches properly 
- domain errors now catch with natural log function (`ln`)

## Version 0.2.1

### Fixes:
- inverse trig functions (`asin`, `acos`, `atan`) now handle domain errors properly

### Modifications:
- operators now handle potential erros with if/else clauses rather than catching them with escapes

## Version 0.2

### Modifications:

- changed quit command to `Q` (from `q`)
- changed x-y swap command to `w` (from `s`)
- changed random command to `rand` (from `r`)
- changed drop command to `D` (from `d`)

### Additions:

- added absolute value function `abs`
- added trigonometric functions: `sin`, `cos`, `tan`, `asin`, `acos`, `atan`, `deg`, `rad`
- added square root function `sqrt`
