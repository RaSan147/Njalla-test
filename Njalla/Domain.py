import requests
from .API import NjallaAPI

class NjallaDomain:
    def __init__(self, api_key):
        self.api_key = NjallaAPI(api_key)
        self.base_url = "https://njal.la/api/1/"

        # will be added later on