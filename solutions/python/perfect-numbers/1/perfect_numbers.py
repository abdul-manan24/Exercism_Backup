def classify(number):
    """ A perfect number equals the sum of its positive divisors.

    :param number: int a positive integer
    :return: str the classification of the input integer
    """
    if number < 1:
        raise ValueError("Classification is only possible for positive integers.")

    factors = set([])

    for num in range(1, int(number ** 0.5) + 1):
        if number % num == 0:
            factors.add(num)
            factors.add(number//num)

    factors.remove(number)

    if sum(factors) == number:
        return "perfect"
    if sum(factors) > number:
        return "abundant"

    return "deficient"
