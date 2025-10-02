def length_of_last_word(str):
    dct = str.split()
    slice = dct[(len(dct) - 1)::]
    return len(''.join(slice))

result  = length_of_last_word('hello\t\nworld!') 
print(result)