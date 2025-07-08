import pytest
from src.dog_api import DogApi

@pytest.fixture(scope='module')
def client():
    # Creating a session
    client = DogApi(timeout=5)
    yield client
    client.session.close()


# Testing method get_single_random_image_status_code
def test_get_single_random_image_status_code(client):
    # Check the status code 
    response = client.get_single_random_image()
    assert response.status_code == 200, f'Status_code is not 200, got {response.status_code}'

def test_get_single_random_image_data(client):
    # Check the message 
    response_data = client.get_single_random_image().json()

    assert response_data['status'] == 'success', f'status is not success, got {response_data['status']}'


# Testing method get_multiple_random_image
def test_get_multiple_random_image_status_code(client):
    # Check the status code 
    response = client.get_multiple_random_image()
    assert response.status_code == 200, f'Status_code is not 200, got {response.status_code}'

@pytest.mark.parametrize('count', [1, 2, 3])
def test_get_multiple_random_image_data(client, count):
    # Check the message 
    response_data = client.get_multiple_random_image(count).json()
    assert response_data['status'] == 'success', f'status is not success, got {response_data['status']}'
    assert isinstance(response_data['message'], list), f'Expected "message" to be a list, but got {type(response_data["message"]).__name__}'
    assert len(response_data['message']) == count, f'len message is not{count}, got {len(response_data['message'])}'

    for url in response_data['message']:
        assert isinstance(url, str), f'Expected each URL to be a str, but got {type(url).__name__!r}: {url!r}'
        assert url.startswith(('http://', 'https://')), f'URL does not start with "http://" or "https://": {url!r}'
        assert url.lower().endswith(('.jpg', '.jpeg', '.png')), f'URL does not end with a valid image extension (.jpg/.jpeg/.png): {url!r}'


# Testing method get_breeds_list
def test_get_breeds_list_status_code(client):
    # Check the status code 
    response = client.get_breeds_list()
    assert response.status_code == 200, f'Status_code is not 200, got {response.status_code}'

@pytest.mark.parametrize('dog_breed',[
    'affenpinscher',
    'akita',
    'terrier'
])
def test_get_breeds_list_data(client, dog_breed):
    # Check the message 
    response_data = client.get_breeds_list(dog_breed).json()
    assert response_data['status'] == 'success', f'status is not success, got {response_data['status']}'
    assert isinstance(response_data['message'], str), f'Expected "message" to be a str, but got {type(response_data["message"]).__name__}'
    assert response_data['message'].startswith(('http://', 'https://')), f'URL does not start with "http://" or "https://": {response_data["message"]!r}'
    assert response_data['message'].lower().endswith(('.jpg', '.jpeg', '.png')), f'URL does not end with a valid image extension (.jpg/.jpeg/.png): {response_data["message"]!r}'

    dog_breed = dog_breed.replace('/', '-')
    assert dog_breed in response_data['message'], f'dog_breed not in "message", but got {response_data["message"]}'
