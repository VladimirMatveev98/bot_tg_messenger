import argparse
from tg_bot import send_message


def get_message():
    """Возвращает сообщение, прочитанное из
    командной строки после флага -m"""
    parser = argparse.ArgumentParser(description='send message to my telegram.')
    parser.add_argument('-m', type=str, help='message to send.')
    args = parser.parse_args()

    return args.m


def main():
    """Получает сообщение из cmd и отправляет его через бота"""
    message = get_message()
    send_message(message)


if __name__ == "__main__":
    main()
