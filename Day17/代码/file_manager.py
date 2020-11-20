import json

base_dir = './files/'


def read_file(file_name):
    try:
        with open(base_dir + file_name, 'r', encoding='utf-8') as file:
            content = file.read()
            return content
    except FileNotFoundError:
        print("文件未找到")


def read_json(file_name, default_data):
    try:
        with open(base_dir + file_name, 'r', encoding="utf-8") as data:
            return json.load(data)
    except FileNotFoundError:
        return default_data


def write_json(file_name, data):
    with open(base_dir + file_name, 'w', encoding="utf-8") as file:
        json.dump(data, file)
