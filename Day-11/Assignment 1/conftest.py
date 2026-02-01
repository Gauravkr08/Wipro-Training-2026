import pytest

def pytest_addoption(parser):
    # 1. Register the Command Line Argument (--env)
    parser.addoption(
        "--env", action="store", default="dev", help="Environment: dev/staging/prod"
    )

    # 2. Register the .ini file option (THIS IS THE MISSING PIECE)
    # This tells pytest that 'env_name' is a valid configuration key.
    parser.addini("env_name", help="Default environment name from config", default="staging")

@pytest.fixture
def env_config(request):
    return request.config.getoption("--env")