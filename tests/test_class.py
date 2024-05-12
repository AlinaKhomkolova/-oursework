from src.operations_with_bank import Bank
from src.utils import get_executed_operations


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
        },
    ]
    assert get_executed_operations(operations) == executed_operations


def test_get_operation_instances():
    bank = Bank(
        date_operation="2019-12-07T06:17:14.634890",
        state_operation="EXECUTED",
        description_operation="Перевод организации",
        amount_operation="48150.39",
        currency_name="USD",
        to_operation="Счет 35158586384610753655",
        from_operation="Visa Classic 2842878893689012"
    )

    assert bank.formatting_from() == "Visa Classic 2842 87** **** 9012 -> "
    assert bank.formatting_to() == "Счет ****************3655"
    assert bank.formatting_date() == "07.12.2019"
    assert str(bank) == (
        "07.12.2019 Перевод организации\n"
        "Visa Classic 2842 87** **** 9012 -> Счет ****************3655\n"
        "48150.39 USD\n"
    )

def test_operation_instance_with_none_from():
    bank = Bank(
        date_operation="2019-12-07T06:17:14.634890",
        state_operation="EXECUTED",
        description_operation="Перевод организации",
        amount_operation="48150.39",
        currency_name="USD",
        to_operation="Счет 35158586384610753655",
        from_operation=None
    )

    assert bank.formatting_from() == ""