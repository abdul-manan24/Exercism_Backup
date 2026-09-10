def value(colors):
    resistence_values = {
        'black':0,
        'brown':1,
        'red':2,
        'orange':3,
        'yellow':4,
        'green':5,
        'blue':6,
        'violet':7,
        'grey':8,
        'white':9
    }

    number_value = ''

    for i in range(2):
        number_value += str(resistence_values[colors[i]])

    return int(number_value)
