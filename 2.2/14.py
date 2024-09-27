def main():
    import itertools

    n = input()

    otv = set()
    for x in itertools.permutations(n, 2):
        s = ''.join(x)
        if s[0] != '0':
            otv.add(int(s))
    print(min(otv), max(otv))


if __name__ == "__main__":
    main()
