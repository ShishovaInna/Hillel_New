def first_word(text:str)->str:
    """
    Пошук першого слова
    :param text: Рядок
    :return: Рядок
    """
    import string
    char_to_replace = string.punctuation.replace("'","")

    for char in text:
        if char in char_to_replace:
            text = text.replace(char," ")

    clean_text = text.strip().split()

    return clean_text[0]


assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')
