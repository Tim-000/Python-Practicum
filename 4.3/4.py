def answer(f):
    def qwe(*args, **dops):
        return f'Результат функции: {f(*args, **dops)}'

    return qwe
