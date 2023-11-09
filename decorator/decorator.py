from settings.config import Settings


# Класс-декоратор для оборачивания класса и передачи ему строки запроса
class QueryConstructor:
    __config = Settings
    __base_url = __config.api_url
    __api_key = __config.api_key

    def __init__(self, url: str, params=None, headers=None,):
        """
        Конструктор класса

        :param url: корень эндпойнтов API сайта
        :param params: эндпойнты API сайта
        :param headers: заголовки запроса
        """

        self.url = self.__base_url + url
        self.params = params

        if headers is None:
            headers = {"X-API-KEY": self.__api_key}
            self.headers = headers
        else:
            raise ValueError("Expected APIKEY")

    def __call__(self, cls):
        """
        Магический метод для вызова класса как функции

        :param cls: оборачиваемый класс
        :return: результат вызова оборачиваемого класса
        """

        self.cls = cls
        return self.cls(url=self.url, headers=self.headers, params=self.params)
