import keyword
str_variable = input('Введіть назву змінної: ')
if (str_variable.isidentifier()
    and not any(char.isupper() for char in str_variable)
    and '__' not in str_variable
    and not keyword.iskeyword(str_variable)):
    print('True')
else:
    print('False')
