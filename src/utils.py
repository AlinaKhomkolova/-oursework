import json

from settings import OPERATIONS_PATH
from src.operations_with_bank import Bank


def load_operations(path: str = OPERATIONS_PATH) -> list[dict]:
    """
    Загружает файл из json
    :param path: Путь к файлу json
    :return: Список словарей
    """
    with open(path, "r", encoding="utf-8") as file:
        return json.load(file)


def get_executed_operations(operations: list[dict]) -> list[dict]:
    """
    Из всех операций выбирает только выполненные операции
    :param operations: список словарей
    :return: операции EXECUTED
    """
    return [
        operation
        for operation in operations
        if operation.get('state') == 'EXECUTED'
    ]


def get_operation_instances(operations: list[dict]) -> list[Bank]:
    """
    Создает экземпляр класса и возвращает список операций
    :param operations: Список словарей операций
    :return: Список экземпляров класса
    """
    operation_instances = []
    for item in operations:
        date_operation = item.get('date')
        description_operation = item.get('description')
        from_operation = item.get('from')
        to_operation = item.get('to')
        state_operation = item.get('state')

        amount_operation = item.get('operationAmount', {}).get('amount')
        code_operation = item.get('operationAmount', {}).get('currency', {}).get(
            'name')
        operation = Bank(state_operation, date_operation,
                         description_operation, from_operation,
                         to_operation, amount_operation, code_operation)
        operation_instances.append(operation)
    return operation_instances


def sorted_operations(operations: list[Bank]) -> list[Bank]:
    """
    Сортирует операции по дате
    :param operations: Список экземпляров класса
    :return: Отсортированный список экземпляров класса
    """
    return sorted(operations, reverse=True)
