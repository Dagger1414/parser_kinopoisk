from typing import Optional

from requests import request, Response, RequestException


class RequestToAPI:
    # Класс для выполнения запроса к API сайта
    def __call__(
            self,
            url: Optional[str] = None,
            headers: Optional[dict] = None,
            params: Optional[str] = None
    ) -> Response:

        """
        Магический метод для вызова класса как функции
        :param args: кортеж параметров (url, params, headers)
        :return: статус-код ответа API сайта, тело ответа API сайта
        """

        try:
            # TODO отловить статус коды 400+
            response = request("GET", url=url, params=params, headers=headers)
            return response
        except RequestException as ex:
            print(ex)


if __name__ == '__main__':
    r = RequestToAPI()
    print(r(url="https://api.kinopoisk.dev/v1/movie/random", headers={"X-API-KEY": "2B1MDTT-Y4MMW9X-JW4B4QV-DTB7WNV"}))
