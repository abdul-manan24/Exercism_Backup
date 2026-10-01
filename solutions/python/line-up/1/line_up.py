def line_up(name, number):
    if number % 10 == 1 and (number % 100) != 11:
        number = str(number) + 'st'
    elif number % 10 == 2 and (number % 100) != 12:
        number = str(number) + 'nd'
    elif number % 10 == 3 and (number % 100) != 13:
        number = str(number) + 'rd'
    else:
        number = str(number) + 'th'

    return f"{name}, you are the {number} customer we serve today. Thank you!" 