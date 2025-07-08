import requests

class JsonPlaceHolder:

    URL = 'https://jsonplaceholder.typicode.com'

    def __init__(self, timeout: 5):
        # session object
        self.session = requests.Session()
        self.session.headers.update({
            'Accept': 'application/json'
        })
        self.timeout = timeout

    def get_id(self, id = 1) -> requests.Response:
        # id
        url = f'{self.URL}/posts/{id}'
        return self.session.get(url, timeout=self.timeout)
    
    def get_comments(self, post_id = 1) -> requests.Response:
        # comments
        url = f'{self.URL}/comments?postId={post_id}'
        return self.session.get(url, timeout=self.timeout)
