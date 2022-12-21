#  Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

# N = 20 -> [2,5]
# N = 30 -> [2, 3, 5]


# number = int(input("Введите число: "))
# def get_list(num):
#     i = 2 # первое простое число
#     lst = []
#     while i <= number:
#         if number % i == 0:
#             lst.append(i)
#             number//= i
#             i = 2
#         else:
#             i += 1
# print(f"Простые множители числа {number} приведены в списке: {get_list(num)}")



def get_prime_factors(num: int) -> list:
    """
    Принимает - целое число (args)
    Возвращает - список простых множителей числа (list)
    """
    list = []
    for i in range(2,num + 1):
        while not num % i:
            if not list.count(i):
                list.append(i)
            num //= i
        else:
            i += 1
    return list 

num = int(input('Введите целое число N: '))
prime_factors = get_prime_factors(num)
print(f'Простые множители числа {num} -> {prime_factors}')