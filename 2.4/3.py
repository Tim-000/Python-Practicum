def main():
    a, b, c = int(input()), 1, 1
    for i in range(a):
        for j in range(b):
            print(c, end=' ')
            c += 1
            if c > a:
                return
        print()
        b += 1


if __name__ == "__main__":
    main()
