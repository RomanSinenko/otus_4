import requests

class DogApi:

    URL = 'https://dog.ceo/api'

    def __init__(self, timeout: 5):
        # session object
        self.session = requests.Session()
        self.session.headers.update({
            'Accept': 'application/json'
        })
        self.timeout = timeout

    def get_single_random_image(self) -> requests.Response:
        # single random image
        url = f'{self.URL}/breeds/image/random'
        return self.session.get(url, timeout=self.timeout)
    
    def get_multiple_random_image(self, count = 5) -> requests.Response:
        # multiple random image
        url = f'{self.URL}/breeds/image/random/{count}'
        return self.session.get(url, timeout=self.timeout)

    def get_breeds_list(self, dog_breed = 'terrier/russell') -> requests.Response:
       # breeds list
       url = f'{self.URL}/breed/{dog_breed}/images/random'
       return self.session.get(url, timeout=self.timeout)
    