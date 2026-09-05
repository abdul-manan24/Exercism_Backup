def convert(number):
    is_divisible_by_3 = number % 3 == 0
    is_divisible_by_5 = number % 5 == 0
    is_divisible_by_7 = number % 7 == 0

    raindrop = ''

    if is_divisible_by_3:
        raindrop += 'Pling'
    if is_divisible_by_5:
        raindrop += 'Plang'
    if is_divisible_by_7:
        raindrop += 'Plong'
    if len(raindrop) == 0:
        raindrop = str(number)

    return raindrop