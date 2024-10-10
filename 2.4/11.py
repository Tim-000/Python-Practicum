def f(x):
    d = set()
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            d |= {x, x // i}
    return len(d) == 0 and x != 1


def main():
    k, n = 0, int(input())
    for i in range(n):
        if f(s := int(input())):
            k += 1
    print(k)


if __name__ == "__main__":
    main()
