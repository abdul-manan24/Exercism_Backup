def slices(series, length):
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if not series:
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    sub_strings = []
    
    start_index = 0
    end_index = length

    while end_index <= len(series):
        sub_strings.append(series[start_index:end_index])
        start_index += 1
        end_index += 1

    return sub_strings
