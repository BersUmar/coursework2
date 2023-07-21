from utils import get_operations, filter_data, sort_data, operations_formated
import pytest


def test_get_operations():
    data = get_operations('operations.json')
    assert isinstance(data, list)

    with pytest.raises(FileNotFoundError):
        get_operations('error_operations.json')

def test_filter_data(item1):
    assert filter_data(item1) == [
        {
            "id": 441945886,
            "state": "EXECUTED",
            "date": "2019-08-26T10:50:58.294041",
            "operationAmount": {
                "amount": "31957.58",
                "currency": {
                    "name": "руб.",
                    "code": "RUB"
                }
            },
            "description": "Перевод организации",
            "from": "Maestro 1596837868705199",
            "to": "Счет 64686473678894779589"
        },
        {
            "id": 939719570,
            "state": "EXECUTED",
            "date": "2018-06-30T02:08:58.425572",
            "operationAmount": {
                "amount": "9824.07",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
        }
    ]

def test_sort_data(item2):
    dates = [x['date'] for x in sort_data(item2)]
    assert dates == ['2019-08-26T10:50:58.294041', '2019-07-03T18:35:29.512364', '2018-06-30T02:08:58.425572']

def test_operations_formated(item2):
    assert operations_formated(item2) == ['30.06.2018 Перевод организации\nMaestro  159 83** **** 5199 -> Счет **9589\n31957.58 руб.\n\n', '03.07.2019 Перевод организации\nMasterCard  715 30** **** 6758 -> Счет **5560\n8221.37 USD\n\n', '26.08.2019 Перевод организации\nMasterCard  715 30** **** 6758 -> Счет **5560\n9824.07 USD\n\n']

# Перевод организации
# Maestro  159 83** **** 5199 -> Счет **9589
# 31957.58 руб.
#
# 03.07.2019 Перевод организации
# MasterCard  715 30** **** 6758 -> Счет **5560
# 8221.37 USD
#
# 26.08.2019 Перевод организации
# MasterCard  715 30** **** 6758 -> Счет **5560
# 9824.07 USD