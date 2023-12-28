import json
import datetime


def get_operations_from_json(filename):
    """
    По json файлу делает список операций
    :param filename: название файла
    :return: список операций
    """
    with open(f'{filename}', encoding="utf-8") as f:
        operation_json = f.read()

        list_of_operations = json.loads(operation_json)

        return list_of_operations


def get_new_operations(quantity):
    """
    По списку операций выводит последние quantity операций
    :param list:
    :param quantity:
    :return:
    """
    list_of_operations = get_operations_from_json('operations.json')

    return list_of_operations[quantity]


def info_about_operation(operation):
    """
    Функция которая по операции готовит вывод информации
    :param operation: словарь с данными по операции
    :return: строка в читаемом виде
    """
    pass


#  (не забыть пустую строку после)


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
    Делает по номеру карты из операции шифрованный номер для вывода
    :param operation:
    :return:
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
    Делает по номеру счета из операции шифрованный номер для вывода
    :param operation:
    :return:
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
