'''
What is pytest?

pytest is a Python testing framework used to write and run automated test cases.
'''

import pytest

def test_add():  #mandatory to start the method name with "test"
    assert 2+3==5

def sub():    # here it is not going to count this as test , because method name is not starting with the "test"
    assert 10-5==5

def test_sub():
    assert 10-5==5
    # assert 10-5==2 #if logic is wrong it throws an error