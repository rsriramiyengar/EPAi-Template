# Readme File for Assignment for Session 4 - Numeric Types II
### Created by Sriram Iyengar
## Session 4 - Numeric Types II
- Floats: Coercing to Integer
- Floats: Rounding
- Decimals
- Decimals: Constructors and Contexts
- Decimals: Math Operations
- Decimals: Performance Considerations
- Complex Numbers
- Booleans
- Booleans: Precedence and Short-Circuiting
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Class
### Qualean
    '''      
    Write a Qualean class that is inspired by Boolean+Quantum concepts. 
    We can assign it only 3 possible real states. True, False, and Maybe (1, 0, -1)
    but it internally picks an imaginary state. The moment you assign it a real number,
    it immediately finds an imaginary number random.uniform(-1, 1) and multiplies with 
    it and stores that number internally after using Bankers rounding to 10th decimal place
    '''

### for  __and__ and __or__
  - This is not implemented as it is a `bitwise &` operation not the `logical and` operation and the base datatype is of `Decimal` class.
    A rejected PEP-335 (https://www.python.org/dev/peps/pep-0335/) does not allow the overloading of `logical and` operator.

###__repr__
- This method returns the representation of the Qualean object and the value it contains in a nicely formatted string.
###__str__
- This method returns the `str` object of value of the Qualean object mentioned.
###__add__
- This method overrides the basic implementation of `addition +` operator for the `Qualean` class. It also extends to `int` objects.
###__eq__
- This method overrides the equality checking `==` for the user defined `Qualean ` objects.
###__float__
- This method returns the float conversion of the `Qualean` object.
###__ge__
- This method overrides the greater than or equal to checking `>=` for the user defined `Qualean ` objects.
###__gt__
- This method overrides the greater than checking `>` for the user defined `Qualean ` objects.
###__invertsign__
- This method returns the opposite sign of value of the calling `Qualean` object.
###__le__
- This method overrides the lesser than or equal to checking `<=` for the user defined `Qualean ` objects.
###__lt__
- This method overrides the lesser than checking `<` for the user defined `Qualean ` objects.
###__mul__
- This method overrides the basic implementation of `multiplication *` operator for the `Qualean` class. It also extends to `int` objects.
###__sqrt__
- This method implements the mathematical Square root operation on the `Qualean` object. 
  It is implemented using `Context` class from the `decimal` module which contains the `sqrt` 
  functionality with precision of 10 decimal places and rounded using `decimal.ROUND_HALF_EVEN`.
###__bool__
-  This dunder method returns the `bool` value for the `Qualean` object.

We are using python >3.8.3

The assignment is  tested by executing 'pytest' , from python shell in same folder