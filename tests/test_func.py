from course_work_for_unit_3.func import (get_operations_from_json,
                                         get_executed_operations,
                                         sort_operations_by_date,
                                         get_new_operations,
                                         get_date_of_operation,
                                         get_encrypted_from_number,
                                         get_encrypted_to_number,
                                         info_about_operation)
import pytest


@pytest.fixture
def operations():
    return [{
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
            "id": 41428829,
            "state": "CANCELED",
            "date": "2019-07-03T18:35:29.512364",
            "operationAmount": {
                "amount": "8221.37",
                "currency": {
                    "name": "USD",
                    "code": "USD"
                }
            },
            "description": "Перевод организации",
            "from": "MasterCard 7158300734726758",
            "to": "Счет 35383033474447895560"
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
            "from": "Счет 75106830613657916952",
            "to": "Visa Gold 7118320734326718"
        }]


@pytest.fixture
def operation_without_date():
    return {
        "id": 939719570,
        "state": "EXECUTED",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    }


@pytest.fixture
def operation_without_from():
    return {
        "id": 939719570,
        "state": "EXECUTED",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "to": "Счет 11776614605963066702"
    }


@pytest.fixture
def operation_without_to():
    return {
        "id": 939719570,
        "state": "EXECUTED",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
    }

@pytest.fixture
def operation_without_operationAmount():
    return {
        "id": 939719570,
        "state": "EXECUTED",
        "description": "Перевод организации",
    }




def test_get_operations_from_json():
    assert get_operations_from_json("course_work_for_unit_3/operations.json") != None


def test_get_operations_from_json__error():
    assert get_operations_from_json("course_work_for_unit_3/operatios.json") == []


def test_get_executed_operations(operations):
    assert len(get_executed_operations(operations)) == 2


def test_sort_operations_by_date(operations):
    assert sort_operations_by_date(operations)[0]['date'] > sort_operations_by_date(operations)[1]['date'] > \
           sort_operations_by_date(operations)[2]['date']


def test_get_new_operations(operations):
    assert len(get_new_operations("course_work_for_unit_3/operations.json", 1)) == 1
    assert len(get_new_operations("course_work_for_unit_3/operations.json", 5)) == 5
    assert get_new_operations("course_work_for_unit_3/operations.json", 5)[0]['date'] > \
           get_new_operations("course_work_for_unit_3/operations.json", 5)[1]['date']


def test_get_date_of_operation(operations):
    assert get_date_of_operation(operations[0]) == "26.08.2019"


def test_get_date_of_operation__error(operation_without_date):
    assert get_date_of_operation(operation_without_date) == "Дата не указана"


def test_get_encrypted_from_number(operations):
    assert get_encrypted_from_number(operations[0]) == "Maestro 1596 83** **** 5199"
    assert get_encrypted_from_number(operations[2]) == "Счет **6952"


def test_get_encrypted_from_number__error(operation_without_from):
    assert get_encrypted_from_number(operation_without_from) == "Источник не указан"


def test_get_encrypted_to_number(operations):
    assert get_encrypted_to_number(operations[0]) == "Счет **9589"
    assert get_encrypted_to_number(operations[2]) == "Visa Gold 7118 32** **** 6718"


def test_get_encrypted_to_number__error(operation_without_to):
    assert get_encrypted_to_number(operation_without_to) == "Назначение не указано"


def test_info_about_operation(operations):
    assert info_about_operation(operations[0]) == ('26.08.2019 Перевод организации' + '\n' +
                                                    'Maestro 1596 83** **** 5199 -> Счет **9589' + '\n' +
                                                    '31957.58 руб.' + '\n')
def test_info_about_operation__error(operation_without_operationAmount):
    assert info_about_operation(operation_without_operationAmount) == ('Дата не указана Перевод организации' + '\n' +
                                                    'Источник не указан -> Назначение не указано' + '\n' +
                                                    'Сумма не указана Валюта не указана' + '\n')
