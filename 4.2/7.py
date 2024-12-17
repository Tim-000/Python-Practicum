res = tuple()


def enter_results(*args):
    global res
    res += args


def get_sum():
    return round(sum(res[::2]), 2), round(sum(res[1::2]), 2)


def get_average() -> tuple[float, float]:
    return round(2 * get_sum()[0] / len(res), 2), round(2 * get_sum()[1] / len(res), 2)
