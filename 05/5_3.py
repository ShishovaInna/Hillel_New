import string
hashtag_str = input('Enter a phrase: ').title()
clean_hashtag = '#'
for char in hashtag_str:
    if char not in string.punctuation and char.isalnum():
        clean_hashtag += char
hashtag_str = clean_hashtag[:140]
print(hashtag_str)
