def prime_generator(end):
    """
    функція повертатиме прості числа - алгоритм Решето Эратосфена
    :param end: верхня межа діапазону
    :return: послідовність з чисел (список)
    """
    if end < 2:
        return  # Ничего не возвращаем, если предел меньше 2
    # 1. Создаем список-решето. Индекс = число, значение = простое оно или нет.
    # [True, True, True, True...]
    primes = [True] * (end + 1)
    primes[0] = primes[1] = False  # 0 и 1 не простые

    for number in range(2, end + 1):
        if primes[number]:
            # Если число простое, выдаем его
            yield number

            # 2. А теперь САМОЕ ВАЖНОЕ:
            # Нужно "вычеркнуть" все числа, кратные этому number.
            # Нам нужен еще один цикл, который пойдет от (number * 2)
            # до (end + 1) с шагом (number).

            for multiple in range(number * number, end + 1, number):
                primes[multiple] = False
#Все составные числа, которые меньше, чем number * number, уже были "пойманы" и
#вычеркнуты более мелкими простыми числами (2, 3 и т.д.). Начиная с квадрата, мы просто
#не делаем лишнюю работу. Это экономит нам тысячи операций на больших диапазонах!

from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
