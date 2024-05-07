import json
from datetime import datetime

from src.classes import Bank
from src.settings import OPERATIONS_PATH


def load_operations(path: str = OPERATIONS_PATH):
    with open(path, "r", encoding="utf-8") as file:
        data_file = json.load(file)
        operations = []
        for item in data_file:
            date_operation = item.get('date')
            # Сортировка операций по дате (если есть операции с датами)
            if date_operation is not None:
                description_operation = item.get('description')
                from_operation = item.get('from')
                to_operation = item.get('to')
                state_operation = item.get('state')

                operation_amount_operation = item.get('operationAmount')
                amount_operation = item.get('operationAmount', {}).get('amount') if operation_amount_operation else ""
                code_operation = item.get('operationAmount', {}).get('currency', {}).get(
                    'code') if operation_amount_operation else ""

                operation = Bank(state_operation, date_operation,
                                 description_operation, from_operation,
                                 to_operation, amount_operation, code_operation)

                operations.append(operation)

        return operations


def sorted_operation_return_last_five():
    last_five = []
    operations = load_operations()
    sorted_operations = sorted(operations, key=lambda x: datetime.strptime(x.date_operation, "%Y-%m-%dT%H:%M:%S.%f"))
    sorted_operations.reverse()
    for operation in sorted_operations:
        if operation.state_operation == "EXECUTED":
            last_five.append(operation)
            if len(last_five) == 5:
                break
    return last_five


operations_data = sorted_operation_return_last_five()

for operation in operations_data:
    bank_instance = Bank(operation.state_operation, operation.date_operation,
                         operation.description_operation, operation.from_operation, operation.to_operation,
                         operation.amount_operation, operation.code_operation)
    bank_instance.formatting_string()
