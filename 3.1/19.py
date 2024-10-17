def z(a, b, c):
    if c == '*':
        return a * b
    elif c == '+':
        return a + b
    elif c == '-':
        return a - b
    return a // b


def main():
    s, l1, l2 = input(), [], []
    for x in s.split():
        if x not in '*-/+':
            l2.append(int(x))
        elif len(l2) >= 2:
            if len(l2) == 2:
                l2[0] = z(l2[0], l2[1], x)
                l2.pop(1)
            else:
                l2[len(l2) - 2] = z(l2[len(l2) - 2], l2[len(l2) - 1], x)
                l2.pop(len(l2) - 1)
    print(*l2)


if __name__ == "__main__":
    main()
