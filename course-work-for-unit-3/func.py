import json


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


def get_new_operations(list, quantity):
    """
    По списку операций выводит последние quantity операций
    :param list:
    :param quantity:
    :return:
    """
    pass


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
    :param operation:
    :return:
    """
    pass


def get_encrypted_card_number(operation):
    """
    Делает по номеру карты из операции шифрованный номер для вывода
    :param operation:
    :return:
    """
    pass


def get_encrypted_account_number(operation):
    """
    Делает по номеру счета из операции шифрованный номер для вывода
    :param operation:
    :return:
    """
    pass
