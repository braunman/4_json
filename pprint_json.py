# -*- coding: utf-8 -*-
import json
import sys
import os


def load_data(filepath):
    with open(filepath, encoding="utf8") as data_file:
        bars_data = json.load(data_file)
    return bars_data

def pretty_print_json(data):
    print (json.dumps(data, indent=4))


if __name__ == '__main__':
    try:
        json_file = sys.argv[1]
        if not os.path.exists(json_file):
            print("Переданный файл не существует")
            exit(1)
    except IndexError:
        print ("Вы не передали скрипту файл json")
        exit(1)
    json_data = load_data(json_file)
    pretty_print_json(json_data)
