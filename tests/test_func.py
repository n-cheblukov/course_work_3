from utils import func
import pathlib


def test_get_operations():
    assert func.get_operations(pathlib.Path('../utils', 'test_operations.json')) == [{'id': 441945886, 'state': 'EXECUTED'}]

def test_get_sorted_operation():
    assert func.get_sorted_operation([{1: 'asd', 2: 'kolya', 3: 'nothing'}]) == []
    assert func.get_sorted_operation([{'date': '2019-08-26T10:50:58.294041'}, {"date": "2018-05-05T01:38:56.538074"}, {"date": "2019-04-18T11:22:18.800453"}]) == [{'date': '26.08.2019'}, {'date': '18.04.2019'}, {'date': '05.05.2018'}]
    assert func.get_sorted_operation([{'date': '2019-08-26T10:50:58.294041'}, {}]) == [{'date': '26.08.2019'}]


def test_get_five_last_executed_operations():
    assert func.get_five_last_executed_operations([{}, {'state': 'asd'}, 'soft', {'state': 'ExeCuted'}]) == [{'state': 'ExeCuted'}]
    assert func.get_five_last_executed_operations([{'state': 'ExeCuted'}, {'state': 'ExeCuted'}, {'state': 'ExeCuted'}, {'state': 'ExeCuted'}, {'state': 'EXECUTED'}]) == [{'state': 'ExeCuted'}, {'state': 'ExeCuted'}, {'state': 'ExeCuted'}, {'state': 'ExeCuted'}, {'state': 'EXECUTED'}]

def test_get_fromto_operation():
    assert func.get_fromto_operation({'from': '1234567812345678'}, 'from') == '1234 56** **** 5678'
    assert func.get_fromto_operation({'to': '12345678901234567890'}, 'to') == '**7890'
    assert func.get_fromto_operation({'to': '1234567812678'}, 'from') == 'Неизвестно'

