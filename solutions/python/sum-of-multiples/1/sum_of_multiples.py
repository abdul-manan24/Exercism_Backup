def sum_of_multiples(limit, multiples):
    unique_multiples = set()
    
    for item in multiples:
        if item <= 0:
            continue
        multiple = item
        while multiple < limit:
            unique_multiples.add(multiple)
            multiple += item

    return sum(unique_multiples)