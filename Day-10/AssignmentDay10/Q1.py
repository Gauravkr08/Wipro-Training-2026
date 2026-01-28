import pytest

# Function under test
def divide(a, b):
    return a / b


# 1️⃣ Unit test using Pytest convention (test_ function)
def test_divide_success():
    assert divide(10, 2) == 5


# 2️⃣ Automatic test discovery
# Pytest will automatically discover this file because its name
# starts with test_ and the function name also starts with test_


# 3️⃣ Assert statement to validate result
def test_divide_assert():
    assert divide(20, 4) == 5


# 4️⃣ Exception test for division by zero
def test_divide_by_zero_exception():
    with pytest.raises(ZeroDivisionError):
        divide(10, 0)