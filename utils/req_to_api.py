# Класс для выполнения запроса к API сайта
from typing import Any

import requests


class RequestToAPI:
    def __call__(self,
                 url: str = "",
                 headers: Any = None,
                 params: Any = None
                 ) -> tuple[int, requests.Response.json]:
        """
        Магический метод для вызова класса как функции
        :param args: кортеж параметров (url, params, headers)
        :return: статус-код ответа API сайта, тело ответа API сайта
        """

        self.url = url
        self.headers = headers
        self.params = params

        response = requests.request(
            "GET",
            url=self.url,
            params=self.params,
            headers=self.headers
        )
        return response.status_code, response.json()

