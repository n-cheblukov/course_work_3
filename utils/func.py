import json
import pathlib
from datetime import datetime
from operator import itemgetter

DATA_OPERATIONS = pathlib.Path('../data', 'operations.json')


def get_operations(data=DATA_OPERATIONS):
    """Возвращает список словарей из файла json"""
    with open(data, 'r', encoding="utf-8") as file:
        operations = json.load(file)
    return operations


def get_sorted_operation(list_operations):
    """
    Сортирует список словарей по дате
    Принимает список, переводит дату в формат datetime, сортирует и переводит дату в строку
    Возвращает новый список
    """
    new_list_operations = []
    for i in list_operations:
        if 'date' in i:
            date_string = datetime.strptime(i["date"], '%Y-%m-%dT%H:%M:%S.%f')
            i["date"] = date_string
            new_list_operations.append(i)
    new_list_operations.sort(key=itemgetter('date'), reverse=True)
    for i in new_list_operations:
        i["date"] = i['date'].strftime('%d.%m.%Y')
    return new_list_operations


def get_five_last_executed_operations(sorted_list):
    """Возвращает 5 последних выполненных операций"""
    new_list = []
    for i in sorted_list:
        if 'state' in i:
            if i['state'].lower() == "executed":
                new_list.append(i)
            if len(new_list) == 5:
                break
    return new_list


def get_fromto_operation(operation, key):
    """
    Принимает словарь и ключ
    Возвращает строку с замаскированным номером карты или номером счета в следующем формате:
    - Номер карты замаскирован и не отображается целиком в формате XXXX XX** **** XXXX
     (видны первые 6 и последние 4 цифры, разбито по блокам по 4 цифры, разделенных пробелом).
    - Номер счета замаскирован и не отображается целиком в формате **XXXX
    (видны только последние 4 цифры номера счета).
    """
    account_number = ''
    if key in operation:
        from_oper = operation[key].split()
        for i in from_oper:
            if i.isdigit():
                if len(i) == 16:
                    account_number = i[0:4] + ' ' + i[4:6] + 2 * '*' + ' ' + 4 * '*' + ' ' + i[-4:]
                if len(i) == 20:
                    account_number = '**' + i[-4:]
        from_oper[-1] = account_number
        return ' '.join(from_oper)
    return 'Неизвестно'
