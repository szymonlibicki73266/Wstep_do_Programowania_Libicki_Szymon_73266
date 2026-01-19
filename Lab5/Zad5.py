import keyword

# List of words to check
words_to_check = ['for', 'print', 'break', 'done', 'bad']

# Check if each word is a keyword
for word in words_to_check:
    if keyword.iskeyword(word):
        print(f"{word} is a keyword.")
    else:
        print(f"{word} is not a keyword.")