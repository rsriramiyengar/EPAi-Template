import pytest
import random
import string
import session4
import os
import inspect
import re
import math
import random
from decimal import Decimal

states = [1, 0, -1]

README_CONTENT_CHECK_FOR = [
    '__and__',
    '__or__',
    '__repr__',
    '__str__',
    '__add__',
    '__eq__',
    '__float__',
    '__ge__',
    '__gt__',
    '__invertsign__',
    '__le__',
    '__lt__',
    '__mul__',
    '__sqrt__',
    '__bool__'
]

def test_readme_exists():
    assert os.path.isfile("README.md"), "README.md file missing!"

def test_readme_contents():
    readme = open("README.md", "r")
    readme_words = readme.read().split()
    readme.close()
    assert len(readme_words) >= 500, "Make your README.md file interesting! Add atleast 500 words"

def test_readme_proper_description():
    READMELOOKSGOOD = True
    f = open("README.md", "r")
    content = f.read()
    f.close()
    for c in README_CONTENT_CHECK_FOR:
        if c not in content:
            READMELOOKSGOOD = False
            pass
    assert READMELOOKSGOOD == True, "You have not described all the functions/class well in your README.md file"

def test_readme_file_for_formatting():
    f = open("README.md", "r")
    content = f.read()
    f.close()
    assert content.count("#") >= 10

def test_indentations():
    ''' Returns pass if used four spaces for each level of syntactically \
    significant indenting.'''
    lines = inspect.getsource(session4)
    spaces = re.findall('\n +.', lines)
    for space in spaces:
        assert len(space) % 4 == 2, "Your script contains misplaced indentations"
        assert len(re.sub(r'[^ ]', '', space)) % 4 == 0, "Your code indentation does not follow PEP8 guidelines"

def test_function_name_had_cap_letter():
    functions = inspect.getmembers(session4, inspect.isfunction)
    for function in functions:
        assert len(re.findall('([A-Z])', function[0])) == 0, "You have used Capital letter(s) in your function names"


def test_function_100times_eq_100q():
    TEST_100times= True
    q = q1 = session4.Qualean((random.choice(states)))
    q = 100 * float(q)
    for x in range(101):
        q1 = q1 + q1
    else:
        if math.isclose(q, q1):
            TEST_million = False

    assert TEST_100times == True, 'Check'

def test_function_decimal_sqrt_check():
    q = session4.Qualean(random.choice([1,0]))
    TEST_decimal = True
    if float(q) >= 0:
        q1 =round((q.__sqrt__()),10)
        print(q1)
        q2=float(q)
        q2=round((Decimal(q2).sqrt()),10)
        print(q2)
        if math.isclose(q1, q2,rel_tol=0.01):
            TEST_decimal = False
    else:
        TEST_decimal = False

    assert TEST_decimal == True, 'Check'

def test_function_sum_million_q_eq_zero():
    q1 = 0
    TEST_million = True
    for x in range(100001):
        q = random.choice(states)
        q = session4.Qualean(q)
        q1 = q1 + float(q)
        print(q1)
    else:
        if  math.isclose(q1, 0):
            TEST_million=False

    assert TEST_million== True, 'Check'

def test_function_q1_false_and_q2_not_defined():
    q1=q2=session4.Qualean(1)
    assert q1.__and__(q2)!= True, "check"


def test_function_q1_True_or_q2_not_defined():
    q1=session4.Qualean(0)
    assert q1.__or__(q2)!= True, "check"