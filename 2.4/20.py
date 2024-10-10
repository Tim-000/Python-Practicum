def cc(n, m):
    s = ''
    while n:
        s = str(n % m) + s
        n //= m

    return sum(int(x) for x in s)


def main():
    n, mx, mc = int(input()), 0, 0
    for i in range(2, 11):
        if cc(n, i) > mx:
            mx = cc(n, i)
            mc = i
    print(mc)


if __name__ == "__main__":
    main()
