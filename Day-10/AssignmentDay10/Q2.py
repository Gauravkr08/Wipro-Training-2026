import pytest

# =================================================
# Calculator Functions
# =================================================

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b


# =================================================
# xUnit Style Setup & Teardown
# =================================================

def setup_module(module):
    print("\nsetup_module: Starting calculator test module")

def teardown_module(module):
    print("\nteardown_module: Ending calculator test module")

def setup_function(function):
    print("\nsetup_function: Before each test")

def teardown_function(function):
    print("\nteardown_function: After each test")


# =================================================
# Fixtures (Normally in conftest.py)
# =================================================

@pytest.fixture(scope="function")
def sample_numbers():
    print("\nFixture setup (function scope)")
    return (10, 5)


@pytest.fixture(scope="module")
def calculator_resource():
    print("\nFixture setup (module scope)")
    yield "Calculator Ready"
    print("\nFixture teardown (module scope)")


# =================================================
# Test Cases Using Fixtures
# =================================================

def test_add(sample_numbers, calculator_resource):
    a, b = sample_numbers
    assert add(a, b) == 15


def test_subtract(sample_numbers):
    a, b = sample_numbers
    assert subtract(a, b) == 5


def test_multiply(sample_numbers):
    a, b = sample_numbers
    assert multiply(a, b) == 50


def test_divide(sample_numbers):
    a, b = sample_numbers
    assert divide(a, b) == 2


def test_divide_by_zero_exception():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)