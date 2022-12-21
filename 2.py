#  Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности. Не использовать множества.
# Постарайтесь решить за одно условие

# [1,1,1,1,2,2,2,3,3,3,4] -> [1,2,3,4]


import random

def get_number_list(n=20, min=10, max=99) -> list:
    number_list = [random.randint(min, max)]
    for i in range (1, n):
        number_list.append(random.randint(min, max)) 
    return number_list

def get_nonrepeating_elemens(list) -> list:
    """
    Возвращает список неповторяющихся элементов исходной последовательности
    
    Args: 
    list - список целых чисел

    Returns:
    list -список целых чисел
    """
    new_list = [list[0]]
    for i in range(1, len(list)):
        for j in range(len(new_list)):
            if list[i] == new_list[j]:
                break
            elif j == len(new_list)-1:
                new_list.append(list[i])
    return new_list

random_list = get_number_list(20, 10, 50)
finite_list = get_nonrepeating_elemens(random_list)
print(f'{random_list} ->')
print(finite_list)