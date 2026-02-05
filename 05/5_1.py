import keyword
str_variable = input('Введіть назву змінної: ')

if (str_variable.replace('_', '') == ''):
    if (str_variable == '_'):
      underline = True
    else:
      underline = False
else:
    underline = True

if (str_variable.isidentifier()
    and underline
    and not any(char.isupper() for char in str_variable)
    and not keyword.iskeyword(str_variable)):
    print('True')
else:
    print('False')
