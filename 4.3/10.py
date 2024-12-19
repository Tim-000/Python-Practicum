def make_linear(mass):
    new_list = []
    for i in mass:
        if isinstance(i, list):
            new_list.extend(make_linear(i))
        else:
            new_list.append(i)
    return new_list
