from datetime import datetime
from src.operations_with_bank import Bank
from src.utils import get_executed_operations, sorted_operations, get_operation_instances
import pytest


def test_get_executed_operations():
    operations = [
        {
            "state": "EXECUTED",
        },
        {
            "state": "EXECUTED",
        },
        {},
        {
            "state": "CANCELED",
        }
    ]
    executed_operations = [
        {
            "state": "EXECUTED",
        },
        {
            "state": "EXECUTED",
        }
    ]
    assert get_executed_operations(operations) == executed_operations


def test_instances():
    bank = Bank(
        date_operation="2019-12-07T06:17:14.634890",
        state_operation="EXECUTED",
        description_operation="Перевод организации",
        amount_operation="48150.39",
        currency_name="USD",
        to_operation="Счет 35158586384610753655",
        from_operation="Visa Classic 2842878893689012"
    )
    bank2 = Bank(
        date_operation=None,
        state_operation="EXECUTED",
        description_operation="Перевод",
        amount_operation="48150.39",
        currency_name="USD",
        to_operation=None,
        from_operation=None
    )
    assert bank.formatting_payment(bank.from_operation) == "Visa Classic 2842 88** **** 9012"
    assert bank.formatting_payment(bank.to_operation) == "Счет **3655"
    assert bank.formatting_date() == "07.12.2019"
    assert str(bank) == (
        "07.12.2019 Перевод организации\n"
        "Visa Classic 2842 88** **** 9012 -> Счет **3655\n"
        "48150.39 USD\n"
    )

    assert bank2.formatting_date() == ""
    assert bank2.formatting_payment(bank2.from_operation) == ""
    assert bank2.formatting_payment(bank2.to_operation) == ""
    assert str(bank2) == (
        " Перевод\n"
        "\n"
        "48150.39 USD\n"
    )


def test_get_operation_instances():
    operations = [
        {
            "state": "EXECUTED",
            "date": "2018-12-23T11:47:52.403285",
            "operationAmount": {
                "amount": "450",
                "currency": {
                    "name": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "МИР 8665240839126074",
            "to": "Maestro 3000704277834087"
        },
        {
            "state": "EXECUTED",
            "date": "2018-12-23T11:47:52.403285",
            "operationAmount": {
                "amount": "400",
                "currency": {
                    "name": "USD"
                }
            },
            "description": "Перевод с карты на карту",
            "from": "МИР 8665240839126074",
            "to": "Maestro 3000704277834087"
        }
    ]
    operation_instances = get_operation_instances(operations)

    assert isinstance(operation_instances, list)
    for operation in operation_instances:
        assert isinstance(operation, Bank)

    for i, operation in enumerate(operation_instances):
        assert operation.state_operation == operations[i]["state"]
        assert operation.date_operation == operations[i]["date"]
        assert operation.description_operation == operations[i]["description"]
        assert operation.from_operation == operations[i]["from"]
        assert operation.to_operation == operations[i]["to"]
        assert operation.amount_operation == operations[i]["operationAmount"]["amount"]
        assert operation.currency_name == operations[i]["operationAmount"]["currency"]["name"]


def test_operation_instance_with_none_from_and_to():
    bank = Bank(
        date_operation="2019-12-07T06:17:14.634890",
        state_operation="EXECUTED",
        description_operation="Перевод организации",
        amount_operation="48150.39",
        currency_name="USD",
        to_operation=None,
        from_operation=None
    )

    assert bank.formatting_payment(bank.from_operation) == ""
    assert bank.formatting_payment(bank.to_operation) == ""


def test_sorted_operations():
    operations = [Bank(
        date_operation="2019-12-07T06:17:14.634890",
        state_operation="EXECUTED",
        description_operation="Перевод организации",
        amount_operation="48150.39",
        currency_name="USD",
        to_operation="Счет 35158586384610753655",
        from_operation="Visa Classic 2842878893689012"
    ),
        Bank(
            date_operation="2019-10-05T06:17:14.634890",
            state_operation="EXECUTED",
            description_operation="Перевод организации",
            amount_operation="48150.39",
            currency_name="USD",
            to_operation="Счет 35158586384610753655",
            from_operation="Visa Classic 2842878893689012"
        )
    ]
    sorted_op = sorted_operations(operations)
    for i in range(len(sorted_op) - 1):
        assert datetime.fromisoformat(sorted_op[i].date_operation) >= datetime.fromisoformat(
            sorted_op[i + 1].date_operation)
