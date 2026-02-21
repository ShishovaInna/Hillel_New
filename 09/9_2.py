def difference(*args):
    """
    знайти різницю між найбільшим (максимум) і найменшим (мінімум) елементом

    :param args: Змінна кількість аргументів як числа (int, float)
    :return: Різниця між максимумом і мінімумом як число (int, float)
    """
    if len(args) in [0,1]:
        return 0
    else:
        min_arg = min(args)
        max_arg = max(args)
        return round((max_arg - min_arg),2)

assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')
