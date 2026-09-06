import string
def is_pangram(sentence):
    sentence = sentence.lower()
    alphabets = list(string.ascii_lowercase)
    alphabets_not_in_sentence = [letter for letter in alphabets if letter not in sentence]

    if len(alphabets_not_in_sentence) == 0:
        return True
    return False
