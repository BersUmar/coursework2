from settings import PATH_WITH_FIXTURES
from utils import get_operations, filter_data, sort_data, operations_formated


def main():
    operations = get_operations(PATH_WITH_FIXTURES)
    operations = filter_data(operations)
    operations = sort_data(operations)
    operations = operations_formated(operations)
    print(operations)
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

