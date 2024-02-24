""" Модуль с фабрикой"""

from decorator.decorator import QueryConstructor
from utils.req_to_api import RequestToAPI


class Fabric:
    __endpoints = {
        1: "/v1/movie/random",
        2: "/v1/movie/",
        3: "/v1/season",
        4: "/v1/review",
    }

    def __init__(
            self,
            decor=QueryConstructor,
            req_to_api=RequestToAPI,
            params=None
    ):
        self._decor = decor
        self._req_to_api = req_to_api

        if params is None:
            self._params = ""
        else:
            self._params = params

    def abstract_call(self, ):

    def get_random_movie(self):
        url_enpoint = self.__endpoints.get(1) + self._params
        return self._decor(url=url_enpoint)(self._req_to_api())

    def get_info(self, film_id: str):
        self._params = film_id
        url_enpoint = self.__endpoints.get(2) + self._params
        return self._decor(url=url_enpoint)(self._req_to_api())

    def get_season(self):
        url_enpoint = self.__endpoints.get(3) + self._params
        return self._decor(url=url_enpoint)(self._req_to_api())

    def get_review(self):
        url_enpoint = self.__endpoints.get(4) + self._params
        return self._decor(url=url_enpoint)(self._req_to_api())


if __name__ == '__main__':
    pass
