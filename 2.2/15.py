def main():
    a, b = input(), input()

    m = [int(x) for x in str(a) + str(b)]

    mx, mn = max(m), min(m)
    m.remove(mx)
    m.remove(mn)

    s = str(mx) + str(sum(m) % 10) + str(mn)
    print(s)


if __name__ == "__main__":
    main()
