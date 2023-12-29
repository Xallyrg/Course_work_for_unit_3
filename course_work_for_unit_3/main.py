from func import get_new_operations, info_about_operation

# Достаем информацию о 5 последних операциях из файла operations.json
list_of_operations = get_new_operations('operations.json', 5)

# Выводим информацию по последним 5 операциям
for operation in list_of_operations:
    print(info_about_operation(operation))
