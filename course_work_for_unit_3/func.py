import json
import datetime
import operator


def get_operations_from_json(filename):
    """
    По json файлу делает список словарей (операций)
    :param filename: название файла
    :return: список операций
    """
    with open(f'{filename}', encoding="utf-8") as f:
        operation_json = f.read()

        list_of_operations = json.loads(operation_json)

        return list_of_operations


def get_executed_operations(operations):
    """
    Функция оставляет только совершенные операции, из списка всех операций
    :param operations: список операций
    :return: список свершенных операций
    """
    operation_list = []
    for operation in operations:
        if operation.get('state') == 'EXECUTED':
            operation_list.append(operation)
    return operation_list


def sort_operations_by_date(operations):
    """
    Функция сортирует по дате полученный массив операций
    :param operations: список операций
    :return: список операций отсортированный по дате
    """
    sorted_operations = sorted(operations, key=lambda x: x['date'], reverse=True)

    return sorted_operations


def get_new_operations(filename, quantity):
    """
    Берет список операций из файла, удаляет не исполненные операции, сортирует оставшиеся операции по дате и выводит quantity последних операций
    :param filename: название файла откуда берем данные
    :param quantity: количество операций, которые надо вывести
    :return: Возвращает quantity последних операций, отсортированных по дате
    """
    list_of_operations = get_operations_from_json(filename)
    executed_operations = get_executed_operations(list_of_operations)
    s_sorted = sort_operations_by_date(executed_operations)

    return s_sorted[0:quantity]


def get_date_of_operation(operation):
    """
    Преращает дату из операции в вид ДД.ММ.ГГГГ
    :param operation: операция
    :return: дата операции в нужном формате
    """
    date = operation.get('date')

    if date:
        date_time_obj = datetime.datetime.strptime(date, "%Y-%m-%dT%H:%M:%S.%f")
        return date_time_obj.strftime("%d.%m.%Y")
    else:
        return 'Дата не указана'


def get_encrypted_from_number(operation):
    """
    Делает по номеру from из операции шифрованный номер для вывода
    :param operation: операция
    :return: номер карты/счера откуда перевод в нужном формате
    """
    from_info = operation.get('from')

    if from_info:
        if from_info[0:4] == 'Счет':
            encrypted_from_info = ('Счет **' + from_info[-4:])
        else:
            encrypted_from_info = (from_info[0:-16] +
                                   from_info[-16:-12] + ' ' +
                                   from_info[-12:-10] + '**' + ' ' +
                                   '****' +
                                   from_info[-4:])

        return encrypted_from_info
    else:
        return 'Источник не указан'


def get_encrypted_to_number(operation):
    """
    Делает по номеру to из операции шифрованный номер для вывода
    :param operation: операция
    :return: номер карты/счера куда перевод в нужном формате
    """
    to_info = operation.get('to')

    if to_info:
        if to_info[0:4] == 'Счет':
            encrypted_from_info = ('Счет **' + to_info[-4:])
        else:
            encrypted_from_info = (to_info[0:-16] +
                                   to_info[-16:-12] + ' ' +
                                   to_info[-12:-10] + '**' + ' ' +
                                   '****' +
                                   to_info[-4:])

        return encrypted_from_info
    else:
        return 'Назначение не указано'


def info_about_operation(operation):
    """
    Функция которая по операции готовит вывод информации
    :param operation: операция
    :return: строка в нужном виде
    """
    operation_decription = operation.get('description') if operation.get('description') else "Нет описания перевода"

    operation_operationAmount = operation.get('operationAmount')
    if operation_operationAmount:
        operation_operationAmount_amount = operation_operationAmount.get('amount') if operation_operationAmount.get(
            'amount') else "Сумма не указана"

        operation_operationAmount_currency = operation_operationAmount.get("currency")
        if operation_operationAmount_currency:
            operation_operationAmount_currency_name = operation_operationAmount_currency.get(
                "name") if operation_operationAmount_currency.get("name") else "Валюта не указана"
        else:
            operation_operationAmount_currency_name = "Валюта не указана"
    else:
        operation_operationAmount_amount = "Сумма не указана"
        operation_operationAmount_currency_name = "Валюта не указана"

    info_str = (get_date_of_operation(operation) + ' ' + operation_decription + '\n' +
                get_encrypted_from_number(operation) + ' -> ' + get_encrypted_to_number(operation) + '\n' +
                operation_operationAmount_amount + ' ' + operation_operationAmount_currency_name + '\n')

    return info_str
