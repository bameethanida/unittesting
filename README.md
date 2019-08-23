# Unit Testing Assignment

by Thanida Jongarnon.


# Test Cases for unique


| Test case              |  Expected Result    |
|------------------------|---------------------|
| empty list             |  empty list         |
| one item               |  list with 1 item   |
| one item with duplication    |  list with 1 item   |
| 2 items               |  list with 2 items   |
| 2 items, with duplication, many orders | 2 item list, items in same order  |
| multiple items         |  list with multiple items   |
| multiple items, with duplication, many orders        |  multiple items list, items in same order   |
| list with one nested list               | list with one nested list   |
| list with one nested list with duplication              | list with one nested list, items in same order   |
| list with multiple nested lists           | list with multiple nested lists  |
| list with multiple nested lists with duplication         | list with multiple nested lists, items in same order  |
| argument not a list        |  TypeError|

# Test Cases for Fraction

## Test Cases for `__init__`

 Test case              |  Expected Result    |
|------------------------|---------------------|
| Both Numerator and Denominator are integer| Fraction(`numerator`, `denominator`) in proper form    |
| Either Numerator or Denominator are not integer    |    TypeError     |

## Test Cases for `__str__`

| Test case              |  Expected Result    |
|------------------------|---------------------|
|  Both Numerator and Denominator (not 0 or 1) are integer  |    `numerator` / `denominator` in proper form   |
| Numerator is zero, non-zero int Denominator |      0   |
|  Non-zero int Numerator, Denominator is 1 |  `numerator`  |
| Negative int Numerator and Denominator is zero  | -1/0  |
|  	Positive int Numerator and Denominator is zero  | 1/0  |
| Numerator and Denominator are zero  | 0/0  |

## Test Cases for `__add__`
## Test Cases for `__sub__`
## Test Cases for `__mul__`
## Test Cases for `__gt__`
## Test Cases for `__neg__`
## Test Cases for `__eq__`

