"""
PYTEST FUNCTIONAL TEST SUITE

Covers:
1. End-to-end functional testing
2. Parallel execution support
3. HTML & JUnit reports
4. Execution history (CI friendly)
5. Scalable pytest design

RUN:
pytest -n auto --html=report.html --self-contained-html --junitxml=report.xml
"""

import pytest

def register_user(username, password):
    if username and password:
        return "registered"
    return "failed"


def login_user(username, password):
    if username == "Abhi" and password == "1234":
        return "login success"
    return "login failed"



@pytest.fixture
def test_user():
    return {
        "username": "Abhi",
        "password": "1234"
    }


def test_user_register_and_login_e2e(test_user):
    register_result = register_user(
        test_user["username"],
        test_user["password"]
    )
    assert register_result == "registered"

    login_result = login_user(
        test_user["username"],
        test_user["password"]
    )
    assert login_result == "login success"


"""
PYTEST SCALABILITY:
- Fixtures reduce duplication
- Tests run in parallel with pytest-xdist
- Reports support CI/CD trend analysis
- Easy to extend for API / UI / DB testing
"""