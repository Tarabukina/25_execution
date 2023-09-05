import json
from pathlib import Path
JSON_FILE = Path(__file__).resolve().parent / 'operations.json'

def load_json(file_path):
    with open(file_path, encoding="utf-8") as f:
        data = json.load(f)
        return data


file_json = load_json(JSON_FILE)


def date_last(UP):
    '''функция сортирует все значения по дате от наименьшего к наибольшему'''
    sorted_data_1 = sorted(UP, key=lambda x: x.get('date'), reverse=True)
    return sorted_data_1


sorted_data = date_last(file_json)
print(sorted_data)

# создаем пустой список для записи первых 5 значений
five_str_load = []


def load_str(resorted):
    '''функция записи последних элементов со статусом "EXECUTED",
    если статус ==EXECUTED, то переменная счетчик увеличивается на 1
    и происходит запись в словарь, как только переменная счетчик будет равна 5, цикл автоматом вырубается'''
    count = 0

    for state_status in resorted:
        state = state_status.get('state', '')