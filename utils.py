import json
import datetime


def get_data():
    with open('operations.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    return data


def get_filtered_data(data):
    filtered_data = []
    # s = 0

    for transaction in data:
        if len(transaction) > 5:
            if transaction['state'] == 'EXECUTED':
                filtered_data.append(transaction)
                # s += 1
    # print(filtered_data)
    # print(s)
    return filtered_data


def get_sorted_data(filtered_data):
    filtered_data.sort(key=lambda d: d['date'])
    sorted_data = filtered_data[-5:]

    # print(sorted_data)
    return sorted_data


def conver_date(date):
    date_transaction = datetime.datetime.strptime(date, '%Y-%m-%dT%H:%M:%S.%f')
    return date_transaction.strftime('%d.%m.%Y')


def mask(from_transaction):
    if from_transaction[0:4] == 'Счет':
        from_transaction = from_transaction[0:4] + " " + "****************" + from_transaction[21:]
    elif from_transaction == '-':
        pass
    else:
        from_transaction = from_transaction[:-10] + "******" + from_transaction[-4:]

    return from_transaction

def mask2(to_transaction):
    if to_transaction[0:4] == 'Счет':
        to_transaction = to_transaction[0:4] + " " + "****************" + to_transaction[21:]
    elif to_transaction == '-':
        pass
    else:
        to_transaction = to_transaction[:-10] + "******" + to_transaction[-4:]

    return to_transaction

def get_formatted_data(sorted_data):
    sum_pr =''
    for transaction in sorted_data:
        date_transaction = conver_date(transaction['date'])
        from_transaction = mask(transaction.get('from', '-'))
        to_transaction = mask2(transaction.get('to', '-'))

        sum_transaction = transaction['operationAmount']["amount"]
        currency_transaction = transaction['operationAmount']["currency"]['name']

        print_information = date_transaction + ' ' + transaction['description'] + '\n' + from_transaction + ' -> ' + to_transaction + '\n' + sum_transaction + currency_transaction + '\n'+'\n'
        sum_pr = sum_pr + print_information

    print(sum_pr)
    return sum_pr
