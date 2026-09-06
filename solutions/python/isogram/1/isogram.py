def is_isogram(phrase):
    phrase = phrase.lower().replace("-", "").replace(" ", "")
    is_isogram_word = len(set(phrase)) == len(phrase)
    return is_isogram_word