def recursive_digit_sum(numb):
    return numb % 10 + recursive_digit_sum(numb // 10) if numb else 0
