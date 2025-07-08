import pytest
from src.open_brewery_bd import OpenBrewery

@pytest.fixture(scope = 'module')
def client():
    # Creating a session
    client = OpenBrewery(timeout=5)
    yield client
    client.session.close()


# Testing method get_single_brewery
def test_get_single_brewery_status_code(client):
    # Check the status code 
    response = client.get_single_brewery()
    assert response.status_code == 200, f'Status_code is not 200, got {response.status_code}'

@pytest.mark.parametrize('uuid',[
    'b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0',
    '5128df48-79fc-4f0f-8b52-d06be54d0cec',
    '9c5a66c8-cc13-416f-a5d9-0a769c87d318',
    '34e8c68b-6146-453f-a4b9-1f6cd99a5ada'
])
def test_get_single_brewery_data(client, uuid):
    # Check the message
    response_data = client.get_single_brewery(uuid).json()
    keys = [
        'id', 'name', 'brewery_type', 'address_1', 'address_2', 'address_3',
        'city', 'state_province', 'postal_code', 'country', 'longitude',
        'latitude', 'phone', 'website_url', 'state', 'street'
    ]
    assert response_data['id'] == uuid
    for key in keys:
        assert key in response_data


# Testing method get_by_city
def test_get_by_city_status_code(client):
    # Check status_code
    response = client.get_by_city()
    assert response.status_code == 200, f'Status_code is not 200, got {response.status_code}'

@pytest.mark.parametrize('city', [
    'Denver', 'Chicago', 'Tucson'
])
def test_get_by_city_data(client, city):
    # Check the message
    response_data = client.get_by_city(city).json()
    assert isinstance(response_data, list), f'Expected "message" to be a list, but got {type(response_data).__name__}'
    assert response_data[0]['city'] == city, f'city name in message is not {city}, got {response_data[0]['city']}'


# Testing method get_by_country
def test_get_by_country_status_code(client):
    # Check status_code
    response = client.get_by_country()
    assert response.status_code == 200, f'Status_code is not 200, got {response.status_code}'

def test_get_by_country_headers(client):
    # Check headers
    response = client.get_by_country()
    response_headers = response.headers
    assert response_headers.get('Content-Type') == 'application/json', f'content-type is not application/json, got {response_headers.get("Content-Type")}'
