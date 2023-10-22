"""Модуль с классом запроса на API"""
import json
import requests

from typing import Any

from parser_kinopoisk.settings.config import Settings


class RequestToAPI:
    """Класс запроса к API"""

    def __init__(
            self,
            endpoint: str = "",
            api_key: str = Settings.api_key
    ) -> None:
        self.url = Settings.api_url + endpoint
        self.__api_key = api_key

    def __call__(self, *args: Any, **kwds: Any) -> requests.Response():

        response = requests.get(url=self.url, headers={"X-API-KEY": self.__api_key})
        return response


if __name__ == "__main__":

    endpoint = "/v1/movie/random"
    response = RequestToAPI(endpoint=endpoint)
    json_body = response().json()
    prep = json.dumps(json_body, ensure_ascii=False, indent=4)

    with open("random_movie.json", "w", encoding='utf-8') as file:
        file.write(prep)

