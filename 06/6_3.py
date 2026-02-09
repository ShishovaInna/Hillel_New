number = input('Введіть число: ')
number_list = list(number)
multiplication_number = 10

while multiplication_number > 9:
    multiplication_number = 1
    for el in number_list:
        multiplication_number *= int(el)
    number_list = list(str(multiplication_number))

print(f'{number} => {multiplication_number}')
