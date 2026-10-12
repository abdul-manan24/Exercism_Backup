def abbreviate(words):
    acronym = words[0].upper()
    
    for letter in range(len(words)):
        if words[letter - 1] in [" ", "-", "_"] and words[letter].isalpha():
            acronym += words[letter].upper()

    return acronym