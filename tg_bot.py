import requests
import json
from typing import Tuple
from pathlib import Path


TEST_MESSAGE = "Test_bot_message. If u read this, all fine."


def read_config(path: str | Path = "config.json") -> Tuple[str, str]:
    """Используется для чтения конфигурационного файла"""

    with open(path, 'r') as json_file:
        param = json.load(json_file)

    TOKEN = param["TOKEN"]
    CHAT_ID = param["CHAT_ID"]

    return TOKEN, CHAT_ID


def send_message(message: str):
    """Отправляет боту url с текстом сообщения"""
    TOKEN, CHAT_ID = read_config()
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={CHAT_ID}&text={message}"
    requests.get(url).json()


def read_messages() -> dict:
    """Возвращает структуру данных с информацией о присланных
    боту сообщениях"""
    TOKEN, _ = read_config()
    request = f"https://api.telegram.org/bot{TOKEN}/getUpdates"
    return requests.get(request).json()


if __name__ == "__main__":
    print(read_messages())
    print("-" * 45)
    print(send_message(TEST_MESSAGE))
