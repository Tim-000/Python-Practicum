def main():
    a, s, c = int(input()), '', 0
    b = a
    while b > 0:
        c += 1
        b -= c
    n = 1
    ar = []
    for i in range(c):
        for j in range(i + 1):
            if n > a:
                break
            s = s + str(n) + ' '
            n += 1
        ar.append(s)
        s = ''
    ml = len(ar[-1])
    for i in range(c):
        ar[i] = f'{ar[i]:^{ml}}'
    for i in ar:
        print(i)


if __name__ == "__main__":
    main()
