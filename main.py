import json

import requests

from utils.fabric import Fabric


def main():
    input_command = int(input("Input command: "))
    kinopoisk = Fabric()
    match input_command:
        case 1:
            response = kinopoisk.get_random()
            print(response)
            with open("response.json", "w", encoding="UTF-8") as file:
                string_json = json.dumps(response[1], ensure_ascii=False, indent=4)
                file.write(string_json)
        case _:
            print("Case error")


if __name__ == '__main__':
    main()
