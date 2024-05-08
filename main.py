from src.function import sorted_operation_return_last_five
from src.operations_with_bank import Bank


def main():
    operations_data = sorted_operation_return_last_five()

    for operation in operations_data:
        bank_instance = Bank(operation.state_operation, operation.date_operation,
                             operation.description_operation, operation.from_operation, operation.to_operation,
                             operation.amount_operation, operation.code_operation)
        bank_instance.formatting_string()


if __name__ == '__main__':
    main()
