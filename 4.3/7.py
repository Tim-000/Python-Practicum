def same_type(f):
    def qwe(*args):
        if len({type(x) for x in args}) != 1:
            print("Обнаружены различные типы данных")
            return False
        return f(*args)

    return qwe
