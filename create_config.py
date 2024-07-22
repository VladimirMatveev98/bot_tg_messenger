import json


def create_template_config():
    """Создаёт шаблон конфиг-файла"""
    template = {'TOKEN': '<your_token>', 'CHAT_ID': '<your_chat_id>'}

    with open('config_template.json', 'w') as file:
        json.dump(template, file)


if __name__ == "__main__":
    create_template_config()