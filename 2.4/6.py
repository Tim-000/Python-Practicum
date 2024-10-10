def main():
    import math
    a = []
    for i in range(int(input())):
        a.append(int(input()))
    print(math.gcd(*a))


if __name__ == "__main__":
    main()
