# Тестовое задание на поиск всех вариантов перестановок, их подсчёт и замер времени, 
# в зависимости от данных введёных пользователем в консоли.

import sys
import itertools
from time import perf_counter

def timer(func):
    """Декоратор для подсчёта времени"""
    def wrapper(*args, **kwargs):
        start = perf_counter()
        result = func(*args, **kwargs)
        print(f'Время выполнения функции - {perf_counter() - start}')
        return result
    return wrapper

# Принимаем аргумент в виде числа
number = int(sys.argv[1])

@timer
def find_counts_str(number):
    """Функция ищет все перестановки и записывает их в файл"""
    result_number = '0' * number + ''.join([str(i+1) for i in range(number)])
    reshuffling = itertools.permutations(result_number)
    
    with open('reshuffling.txt', 'w') as f:
        [f.write(''.join(i) + '\n') for i in reshuffling]

find_counts_str(number)

# Для 5: Время выполнения функции - 5.601658073981525 сек
# Для 4: Время выполнения функции - 0.023882384004537016 сек
# Для 3: Время выполнения функции - 0.0008538159891031682 сек
# Для 2: Время выполнения функции - 0.0006921689782757312 сек
# Для 1: Время выполнения функции - 0.0004425979859661311 сек
