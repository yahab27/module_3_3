def print_params(a = 1, b = 'строка', c = True):# 1.	Создайте функцию print_params
    print (a,b,c)
print_params() #выводим параметры функции
print('--------------------------------')
print_params(2, 'столбик', False)
print_params(3, '', 2.145) #Вызовите функцию print_params с разным количеством аргументов,
# включая вызов без аргументов.
print ("Вывод функции без ргументов:")
print_params("","","")  # Вывод функции без аргументов
print_params(b = 25)
print_params(c = [1,2,3])
print('--------------------------------')
#3.	Передаем values_list и values_dict в функцию print_params, используя распаковку параметров
# (* для списка и ** для словаря) и распаковываем отдельные параметры:
values_list = (22,'Список 1',True)
values_dict = {"a":77,"b":'Список 2', "c":False}
values_list_2 = (54.32, 'Строка')
print_params(*values_list)
print_params(**values_dict)
print('--------------------------------')
print_params(*values_list_2, 42)  # Проверяем, работает ли print_params(*values_list_2, 42)
