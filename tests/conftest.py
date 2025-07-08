import pytest
import requests

def pytest_addoption(parser):
    parser.addoption(
        '--status_code',
        action = 'store',
        default = 200,
        type = int,
        help = 'Expected status code 200'
    )
    parser.addoption(
        '--url',
        action='store',
        default = 'https://ya.ru',
        help = 'Testing URL'
    )

@pytest.fixture
def url(request):
    return request.config.getoption('--url')

@pytest.fixture
def expected_status_code(request):
    return request.config.getoption('--status_code')
