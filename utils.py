import json
from datetime import datetime

from settings import PATH_WITH_FIXTURES


def get_operations(path: str):
    with open(path, 'r', encoding='utf-8') as file:
        return json.load(file)

def filter_data(data):
    filtered_data = [x for x in data if 'state' in x and x['state'] == 'EXECUTED']
    return filtered_data

def sort_data(data):
    data = sorted(data, key=lambda x: x['date'], reverse=True)
    return data[:5]

def operations_formated(operations):
    main_str = []
    for x in operations:
        date = datetime.strptime(x['date'], "%Y-%m-%dT%H:%M:%S.%f").strftime("%d.%m.%Y")

        description = x['description']

        if "from" in x:
            from_list = list(x['from'])
            if x["from"].startswith('Счет'):
                latest_four_num = "".join(from_list[-4:])
                from_ = f'Счет **{latest_four_num}'
            else:
                name = "".join(from_list[:-16])
                from_ = f'{name} {"".join(from_list[-16: -13])} {"".join(from_list[-12: -10])}** **** {"".join(from_list[-4:])}'
        else:
            from_ = ''

        to_list = list(x["to"])
        if x["to"].startswith('Счет'):
            latest_four_num = "".join(to_list[-4:])
            to_ = f'Счет **{latest_four_num}'
        else:
            name = "".join(to_list[:-16])
            to_ = f'{name} {"".join(to_list[-16: -13])} {"".join(to_list[-12: -10])}** **** {"".join(to_list[-4:])}'

        amount = x["operationAmount"]["amount"]

        name = x["operationAmount"]["currency"]["name"]

        operations_str = (f'{date} {description}\n{from_} -> {to_}\n{amount} {name}\n\n')
        main_str.append(operations_str)

    return main_str