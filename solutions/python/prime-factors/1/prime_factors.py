def factors(value):
    factors = []
    divisor = 2

    while value > 1:
        if value % divisor != 0:
            divisor += 1
            continue
        value = value / divisor
        factors.append(divisor)

    return factors
