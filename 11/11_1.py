def prime_generator(end):
    """
    функція повертатиме прості числа.
    :param end: верхня межа діапазону
    :return: послідовність з чисел (список)
    """
    if end < 2:
        return  # 0 и 1 не є простими числами
    for number in range(2,end+1):
        for i in range (2,number):
            if number % i == 0:
                break
        else:
            yield number

from inspect import isgenerator

gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')
