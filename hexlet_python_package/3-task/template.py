employee_numbers = [2, 9, 18, 28]
employee_names = ["Дима", "Марина", "Андрей", "Никита"]

zipped_values = zip(employee_names, employee_numbers)
print(zipped_values) # <zip object at 0x7eda2bd28dc0>

zipped_list = list(zipped_values)
print(zipped_list) #  [('Дима', 2), ('Марина', 9), ('Андрей', 18), ('Никита', 28)]

zipped_tuple = tuple(zipped_values)
print(zipped_tuple) #