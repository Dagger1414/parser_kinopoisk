from functools import update_wrapper
from typing import Any


class Endpoint:
    """Класс декоратор для оборачивания класса запроса, с передачей в класс эндпоинтов
    """
    def __init__(self, cls) -> None:
        pass
    
    def __call__(self, *args: Any, **kwds: Any) -> Any:
        pass
    
