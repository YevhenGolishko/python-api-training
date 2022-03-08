import json
import os
import allure
import requests

from src.response import AssertableResponse


class ApiService(object):

    def __init__(self):
        self._base_url = os.environ["BASE_URL"]
        self._headers = {"content-type": "application/json"}

    def _post(self, url, body):
        return requests.post(f"{self._base_url}{url}", data=json.dumps(body),
                             headers=self._headers)


class UserApiService(ApiService):

    def __init__(self):
        super().__init__()

    @allure.step
    def create_user(self, user):
        return AssertableResponse(self._post("/register", user))
