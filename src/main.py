from utils import func

# вызов функций получения списка операций, сортировки и получения 5 последних операций
list_operations = func.get_operations()
sorted_list = func.get_sorted_operation(list_operations)
last_five_operations = func.get_five_last_executed_operations(sorted_list)

# Выводим результат
for i in last_five_operations:
    print(f"""{i['date']} {i['description']}
{func.get_fromto_operation(i, 'from')} -> {func.get_fromto_operation(i, 'to')}
{i['operationAmount']['amount']} {i['operationAmount']['currency']['name']}\n""")
