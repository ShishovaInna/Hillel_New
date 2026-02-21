def popular_words(text:str, words:list) -> dict:
    """
    Текст та список слів, популярність яких необхідно визначити.

    :param text: Текст для аналізу
    :param words: масив слів, що шукаються
    :return: Словник, у якому ключами є шукані слова та значеннями, скільки разів кожнє слово зустрічаються у орігінальному тексті.
    """

    count_dict = {}
    clean_text = text.lower().replace(',', '').replace('.', '').split()

    for word in words:
        count_dict[word.lower()] = 0
    for word in count_dict:
        count_dict[word] = clean_text.count(word)

    return count_dict

assert popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }, 'Test1'
print('OK')
