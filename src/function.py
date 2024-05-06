import json
from src.classes import Bank

from src.settings import OPERATIONS_PATH


def load_operations(path: str = OPERATIONS_PATH):
    with open(path, "r", encoding="utf-8") as file:
        data_file = json.load(file)
        operations = []
        for item in data_file:
            id_operation = item['id']
            date_operation = item['date']
            description_operation = item['description']
            from_operation = item['from']
            to_operation = item['to']
            state_operation = item['state']
            operation_amount_operation = item['operationAmount']

            amount_operation = operation_amount_operation['amount']
            code_operation = operation_amount_operation['currency']['code']

            operation = Bank(id_operation, state_operation, date_operation,
                                     description_operation, from_operation,
                                     to_operation, amount_operation, code_operation)
            operations.append(operation)
        return operations


operations_data = load_operations()
for i in range(2):
    print(operations_data)
