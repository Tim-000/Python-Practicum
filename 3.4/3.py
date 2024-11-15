def main():
    a, b, c = map(float, input().split())
    while a <= b:
        print("{:.2f}".format(a, 2))
        a += c


if __name__ == "__main__":
    main()
