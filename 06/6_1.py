import string

str_letters = string.ascii_letters
letters = input('Введіть дві букви через дефіс: ').split('-')
i = str_letters.find(letters[0])
letter_new = ''

while i <= str_letters.find(letters[1]):
    letter_new += str_letters[i]
    i += 1
print(letter_new)
