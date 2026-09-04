def is_armstrong_number(number):
    digits = list(str(number))
    sum_of_digits = 0

    for digit in digits:
        sum_of_digits += int(digit) ** len(digits)

    is_armstrong = number == sum_of_digits

    return is_armstrong