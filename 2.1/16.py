def main():
    a, b, c = int(input()), int(input()), int(input())

    t = abs(b - a) / c
    print(format(t, '.2f'))


if __name__ == "__main__":
    main()
