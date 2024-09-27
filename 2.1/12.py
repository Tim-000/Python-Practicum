def main():
    a, b = int(input()), int(input())

    s1 = (a // 100 + b // 100) % 10
    s2 = (a // 10 % 10 + b // 10 % 10) % 10
    s3 = (a % 10 + b % 10) % 10
    print(s1 * 100 + s2 * 10 + s3)


if __name__ == "__main__":
    main()
