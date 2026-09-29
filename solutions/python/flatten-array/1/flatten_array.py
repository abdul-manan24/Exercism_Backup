

def flatten(iterable):
    flatten_array = []
    
    for element in iterable:
        if isinstance(element, list):
            flatten_array.extend(flatten(element))
        elif element is not None:
            flatten_array.append(element)
    return flatten_array