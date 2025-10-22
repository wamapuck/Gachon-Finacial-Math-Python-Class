def add_dot(s):
    dotAdded = '...' + s + '...'
    print(dotAdded)
    return dotAdded

def upper2(s):
    upperAdded = s[:2].upper() + s[2:]
    print(upperAdded)
    return upperAdded

def change_word(word):
    if word[0] == 'a':
        word = add_dot(word)
    else:
        word = upper2(word)
    return word

