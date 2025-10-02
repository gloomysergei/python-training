def length_of_last_word(string):
    words = string.split()
    if not words:
        return 0
    last_word = words[-1]
    return len(last_word)