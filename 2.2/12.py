def main():
    a, b, c = [int(input()) for _ in range(3)]

    if a + b > c and a + c > b and b + c > a:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()
