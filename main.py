from settings import OPERATIONS_COUNT
from src.utils import load_operations, get_operation_instances, \
    get_executed_operations, sorted_operations


def main():
    operations = load_operations()
    executed_operations = get_executed_operations(operations)
    operation_instances = get_operation_instances(executed_operations)
    sort_operations = sorted_operations(operation_instances)
    for op in sort_operations[:OPERATIONS_COUNT]:
        print(op)


if __name__ == '__main__':
    main()
