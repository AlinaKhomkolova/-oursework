import json
from src.classes import Bank
from src.settings import OPERATIONS_PATH


def load_operations(path: str = OPERATIONS_PATH):
    with open(path, "r", encoding="utf-8") as file:
        data_file = json.load(file)
        operations = []
        for item in data_file:
            date_operation = item.get('date')
            description_operation = item.get('description')
            from_operation = item.get('from')
            to_operation = item.get('to')
            state_operation = item.get('state')

            operation_amount_operation = item.get('operationAmount')
            amount_operation = item.get('operationAmount', {}).get('amount')
            code_operation = item.get('operationAmount', {}).get('currency', {}).get('code')

            operation = Bank(state_operation, date_operation,
                             description_operation, from_operation,
                             to_operation, amount_operation, code_operation)

            operations.append(operation)
        return operations


operations_data = load_operations()

for operation in operations_data:
    bank_instance = Bank(operation.state_operation, operation.date_operation,
                         operation.description_operation, operation.from_operation, operation.to_operation,
                         operation.amount_operation, operation.code_operation)
    bank_instance.formatting_string()
