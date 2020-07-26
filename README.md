# Readme File for Assignment for Session 3 - Numeric Types
### Created by Sriram Iyengar
## This assignment is for testing our understaning of Session3 
- Integer Data Types
    -Boolean truth values
    -Integers Numbers
    -Rational Numbers
    -Real Numbers
    -Complex Numbers
- Integer Operations
- Integer Constructors and Bases
- Rational Numbers
- Floats Internal Representation
- Floats Equality Testing
- Floats Coercing to Integer
- Floats Rounding

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Functions  
### encoded_from_base10
    '''
        '''
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
        Check in code  and  return error as below
        if base < 2 or base > 36:
        raise ValueError('invalid value for base, allowed values 2 <= base <= 36')
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
        Check in code  and  return error as below
            if len(digit_map) != base:
                raise ValueError('Number of elements in the digit_map must be equal to base')
    - It return proper encoding for all base ranges between 2 to 36 (including)
    - It return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else Value error
            if len(set(digit_map)) != base:
                raise ValueError('The elements of digit_map are repeating ')
    - the repeating character ValueError message must be relevant
    - We are not using any in-built functions in the math module
    - we are not using bin() hex() etc    
    This Function used the following functions/ operators
        - if - test a given set of logic
        - while  - It runs only when a given logic is true
        - <= / >= checks the less than or greater than based on its usage
    '''

### float_equality_testing(a, b):
    '''
        This function emulates the isclose method from the MATH module, but you can't use this function
        We are going to assume:
        - relative tolerance = 1e-12
        - absolute tolerance = 1e-05  
        This function uses the  following operator/ functions
            -abs - this function returns the abosulte value of given number
            -max -  This function retunrs the max value of given values 
            -<= / >= checks the less than or greater than based on its usage

    '''
### manual_truncation_function(f_num):
    '''
    This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point. 
    It checks f_num is of correct type before it proceed.
    By Using 
        if not isinstance(f_num, float):
        raise ValueError('f_num must be of type float')
    We  are not using inbuilt constructors like int, float, etc.
    # Input is f_num
    # Output is given as trucned floating number
    This function uses the  following operator/ functions
    - if   - test a given set of logic
    - else - This part is execute when if function returns False
    -//    - Floor division
    '''
### manual_rounding_function(f_num):
    '''
    This function emulates python's inbuild ROUND function. We  are not using to use ROUND function, emulating  one manually.
    ## Input is f_num
    ## Output is given by 
    This function makes uses  of  manual_trunction function with some basic if function with logic
    This function uses the  following operator/ functions
    - if   - test a given set of logic
    - manual_trunction function described above
    -also uses the <= operators
    ''''

### rounding_away_from_zero(f_num): This Function 
    '''
    #### This Function is Not Implemented#####
    This function implements rounding away from zero as covered in the class
    Desperately need to use INT constructor? Well you can't. 
    We will be  using  FRACTIONS and extract numerator. 
   
    '''

We are using python >3.8.3

The assignment is  tested by executing 'pytest' , from python shell in same folder