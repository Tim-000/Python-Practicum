def merge(a, b):
    sp = list(a + b)
    n = len(sp)
    for i in range(0, n):
        cur_min = sp[i]
        min_ind = i
        for j in range(i, n):
            if sp[j] < cur_min:
                cur_min = sp[j]
                min_ind = j
        sp[i], sp[min_ind] = sp[min_ind], sp[i]
    return tuple(sp)
