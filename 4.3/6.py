def merge(left, right):
    res = []
    while len(left) > 0 and len(right) > 0:
        if left[0] <= right[0]:
            res.append(left[0])
            left = left[1:]
        else:
            res.append(right[0])
            right = right[1:]
    if len(left) > 0:
        res += left
    if len(right) > 0:
        res += right
    return res


def merge_sort(massiv):
    n = len(massiv)

    if n <= 1:
        return massiv
    else:
        mid = int(len(massiv) / 2)
        left = merge_sort(massiv[:mid])
        right = merge_sort(massiv[mid:])
        return merge(left, right)
