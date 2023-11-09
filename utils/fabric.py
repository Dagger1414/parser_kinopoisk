""" Модуль с фабрикой"""

from decorator.decorator import QueryConstructor
from utils.req_to_api import RequestToAPI


class Fabric:
    __req_func = {
        1: "/v1/movie/random",
    }

    def __init__(self, decor=QueryConstructor, req_to_api=RequestToAPI):
        self.decor = decor
        self.req_to_api = req_to_api

    def get_random(self):
        return self.decor(self.__req_func.get(1))(self.req_to_api())

    def get_info(self, film_id):
        pass

    def get_season(self):
        pass

    def get_review(self):
        pass


if __name__ == '__main__':
    input_command = int(input("Input command: "))
    kinopoisk = Fabric()
    match input_command:
        case 1:
            print(kinopoisk.get_random())
        case _:
            print("Case error")

