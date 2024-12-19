def result_accumulator(f):
    res = []

    def qwe(*args, method="accumulate"):
        res.append(f(*args))
        if method == "drop":
            temp = res.copy()
            res.clear()
            return temp

    return qwe
