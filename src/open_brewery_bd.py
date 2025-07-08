import requests

class OpenBrewery:

    URL = 'https://api.openbrewerydb.org/v1/breweries'

    def __init__(self, timeout:5):
        # session object
        self.session = requests.Session()
        self.session.headers.update({
            "Accept": "application/json"
        })
        self.timeout = timeout

    def get_single_brewery(self, uuid = 'b54b16e1-ac3b-4bff-a11f-f7ae9ddc27e0') -> requests.Response:
        # single_brewery
        url = f'{self.URL}/{uuid}'
        return self.session.get(url, timeout=self.timeout)
    
    def get_by_city(self, city = 'san_diego') -> requests.Response:
        # by_city
        url = f'{self.URL}?by_city={city}&per_page=1'
        return self.session.get(url, timeout=self.timeout)
    
    def get_by_country(self, country = 'france') -> requests.Response:
        # by_country
        url = f'{self.URL}/?by_country={country}&per_page=1'
        return self.session.get(url, timeout=self.timeout)
    