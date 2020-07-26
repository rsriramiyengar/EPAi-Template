def encoded_from_base10(number, base, digit_map):
    '''
    This function returns a string encoding in the "base" for the the "number" using the "digit_map"
    Conditions that this function must satisfy:
    - 2 <= base <= 36 else raise ValueError
    - invalid base ValueError must have relevant information
    - digit_map must have sufficient length to represent the base
    - must return proper encoding for all base ranges between 2 to 36 (including)
    - must return proper encoding for all negative "numbers" (hint: this is equal to encoding for +ve number, but with - sign added)
    - the digit_map must not have any repeated character, else ValueError
    - the repeating character ValueError message must be relevant
    - you cannot use any in-built functions in the MATH module

    '''
    if base < 2 or base > 36:
        raise ValueError('invalid value for base, allowed values 2 <= base <= 36')

    if len(digit_map) != base:
        raise ValueError('Number of elements in the digit_map must be equal to base')

    if len(set(digit_map)) != base:   # set command returns only unique values
        raise ValueError('The elements of digit_map are repeating ')

    sign = 1 if number >= 0 else -1
    unsigned_number = number * sign
    encod_index = []
    if unsigned_number is 0:
        encod_index = [0]
    while unsigned_number != 0:
        encod_index.insert(0, unsigned_number % base)
        unsigned_number = unsigned_number // base

    encod_num = ''.join([digit_map[i] for i in encod_index])
    sign_char = '' if sign == 1 else '-'
    encod_num = sign_char + encod_num
    return encod_num

def float_equality_testing(a, b):
    '''
        This function emulates the ISCLOSE method from the MATH module, but you can't use this function
        We are going to assume:
        - rel_tol = 1e-12
        - abs_tol = 1e-05
    '''
    rel_tol = 1e-12
    abs_tol = 1e-05
    tol=max(rel_tol * max(abs(a), abs(b)), abs_tol)
    output=abs(a-b)<= abs(a - b) <= tol
    return output


def manual_truncation_function(f_num):
    '''
    This function emulates python's MATH.TRUNC method. It ignores everything after the decimal point. 
    It must check whether f_num is of correct type before proceed. You can use inbuilt constructors like int, float, etc
    # Input is f_num
    # Output is given as truncated floating number
    '''

    if not isinstance(f_num, float):
        raise ValueError('f_num must be of type float')
    if f_num >= 0:
        return f_num // 1
    else:
        return f_num // 1 + 1


def manual_rounding_function(f_num):
    '''
    This function emulates python's inbuild ROUND function. You are not allowed to use ROUND function, but
    expected to write your one manually.
    ## Input is f_num
    ## Output is rounded number
    '''
    f1 = manual_truncation_function(f_num)
    if f_num >= 0:
        if (f_num - f1) >= 0.50:
            f_num = f1 + 1
        else:
                f_num = f1
    else:
        if (f_num - f1) <= -0.50:
            f_num = f1 - 1
        else:
            f_num = f1
    return f_num

def rounding_away_from_zero(f_num):
    '''
    #### This Function is Not Implemented#####
    This function implements rounding away from zero as covered in the class
    Desperately need to use INT constructor? Well you can't. 
    Hint: use FRACTIONS and extract numerator. 
    '''
    from fractions import Fraction
    return 3.0