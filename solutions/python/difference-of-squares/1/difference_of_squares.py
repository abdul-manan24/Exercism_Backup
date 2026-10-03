def square_of_sum(number):
    total = sum([i for i in range(1, number+1)])
    return total ** 2


def sum_of_squares(number):
    total = sum([i**2 for i in range(1,number+1)])
    return total


def difference_of_squares(number):
    difference = square_of_sum(number) - sum_of_squares(number)
    return difference
