import json

from utils.fabric import Fabric


def input_integer(default_start=1, default_end=5, default_name="команду") -> int:
    input_command = 0
    try:

        input_command = int(input(f"Введите {default_name}: "))
    except ValueError:
        print(f"Введите значение от {default_start} до {default_end}\n")
    else:
        if default_start > input_command > default_end:
            raise ValueError
    return input_command


def main():
    main_text = f"\n1 - Получить произвольный фильм\n"\
                f"2 - Получить всю информацию о фильме по id\n"\
                f"3 - Получить все сезоны и эпизоды\n"\
                f"4 - Отзывы пользователей\n"\
                f"5 - Выход из программы\n"

    kinopoisk = Fabric()
    response = None

    while True:
        print(main_text)
        command = input_integer()
        match command:
            case 1:
                response = kinopoisk.get_random_movie()
            case 2:
                movie_id = input_integer(default_start=250, default_end=7_000_000, default_name="id фильма")
                response = kinopoisk.get_info(film_id=str(movie_id))
            case 3:
                response = kinopoisk.get_season()
            case 4:
                response = kinopoisk.get_review()
            case 5:
                exit()

            case _:
                print("Case error\nВведите значение от 1 до 5\n")

        if response:
            print(response.json())
            with open("response.json", "w", encoding="UTF-8") as file:
                string_json = json.dumps(response.json(), ensure_ascii=False, indent=4)
                file.write(string_json)


if __name__ == '__main__':
    main()
