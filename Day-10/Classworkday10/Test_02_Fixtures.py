
import pytest
'''
How fixture works (Execution Flow)

1️⃣ pytest sees @pytest.fixture
2️⃣ It runs that function before the test
3️⃣ Passes its return value to the test
4️⃣ Test runs
5️⃣ pytest handles cleanup automatically

'''
@pytest.fixture
def data():
    return [1,2,3]

def test_one(data):
    assert 2 in data
    print(data)

def test_two(data):
    assert len(data)==3
    print(len(data))