import pytest
from src.json_place_holder import JsonPlaceHolder

@pytest.fixture(scope = 'module')
def client():
    # Creating a session
    client = JsonPlaceHolder(timeout=5)
    yield client
    client.session.close()

# Testing method get_id

@pytest.mark.parametrize('id, expected_user_id', [
    (1, 1), (10, 1),
    (11, 2), (20, 2),
    (21, 3), (30, 3),
    (81, 9), (90, 9),
    (91, 10), (100, 10)
],)
def test_get_id_message(client, id, expected_user_id):
    # Check the message
    response_data = client.get_id(id).json()
    assert response_data['id'] == id, f'id in message !=  {id}, got {response_data['id']}'
    assert response_data['userId'] == expected_user_id, f'userId in message != {expected_user_id}, got {response_data['userId']}'

# Testing method get_comments

@pytest.mark.parametrize('post_id',[
    1, 20, 100
],)
def test_get_comments_message(client, post_id):
    # Check the message
    response_data = client.get_comments(post_id).json()
    assert len(response_data) == 5, f'message length != 5, got {len(response_data)}'
    assert isinstance(response_data, list), f'Expected "message" to be a list, but got {type(response_data).__name__}'

    for comment in response_data:
        assert comment['postId'] == post_id, f'postId in comment != {post_id}, got {comment['postId']}'

    first_id = (post_id - 1) * 5 + 1
    for expected_id, comment in enumerate(response_data, start=first_id):
        assert comment['id'] == expected_id, f'id in comment != {expected_id}, got {comment['id']}'
