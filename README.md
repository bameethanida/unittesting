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



 Test case (Constructor)         |  Expected Result    |
|------------------------|---------------------|
| Both Numerator and Denominator are integer| Fraction(`numerator`, `denominator`) in proper form    |
| Either Numerator or Denominator are not integer    |    TypeError     |


| Test case  (Operations)            |  Expected Result    |
|------------------------|---------------------|
| The string representation (`__str__`)|  String of proper fraction     |
| addition |   The sum of fractions   |
| subtraction |  The different of fractions    |
| multiplication|    The product of fractions   |
| greater than |  `True` if fraction is greater and `False` if not     |
| negation |  The  contradiction value of fraction (multiple by -1)  |
| equal to|  `True` if fraction is equal and `False` if not  |




