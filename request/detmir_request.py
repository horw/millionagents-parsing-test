from headers.detmir_headers import DetmirCategoryHeaders
from urls.detmir_url import DetmirCategoryURL
import requests


class DetmirCategoryRequest:

    def __init__(self, city: str = 'MOW', offset: int = 0):
        self.offset = offset
        self.city = city
        self.url = DetmirCategoryURL.get(city, offset)
        self.headers = DetmirCategoryHeaders.get()

    def request(self):
        response = requests.session().get(self.url, headers=self.headers)
        try:
            items = response.json()['items']
            return items
        except ValueError as e:
            print('Bad response')

        return {}

    def __iter__(self):
        return self

    def __next__(self):
        items = self.request()
        if items:
            self.offset += 100
            self.url = DetmirCategoryURL.get(self.city, self.offset)
            return items
        else:
            raise StopIteration
