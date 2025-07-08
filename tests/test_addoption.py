import pytest
import requests


def test_url(url):
    response = requests.get(url)
    requested = response.request.url
    assert requested == url, f'Expected response.url to be {url!r}, but got {response.url!r}'

def test_expected_status_code(url, expected_status_code):
    response = requests.get(url)
    assert response.status_code == expected_status_code, f"Expected status {expected_status_code}, but got {response.status_code}"
