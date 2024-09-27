def main():
    n = int(input())
    i = 2
    s = ''
    while n > 1:
        while n % i == 0:
            s += str(i) + ' * '
            n //= i
        i += 1
    print(s[:-3])


if __name__ == "__main__":
    main()
