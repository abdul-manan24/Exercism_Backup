from string import ascii_lowercase
def rotate(text, key):
    alphabets = list(ascii_lowercase)
    cipher = ''

    for letter in text:
        if letter.isupper():
            index = alphabets.index(letter.lower())
            index += key
            if index >= 26:
                index = index - 26
            ciphered_letter = alphabets[index].upper()
            cipher += ciphered_letter
            
        elif letter in alphabets:
            index = alphabets.index(letter)
            index += key
            if index >= 26:
                index = index - 26
            ciphered_letter = alphabets[index]
            cipher += ciphered_letter
        else:
            cipher += letter

    return cipher
