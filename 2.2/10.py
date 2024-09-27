def main():
    n = input()

    a = int(n[-2]) + int(n[-1])
    b = int(n[0]) + int(n[1])
    if b > a:
        print(str(b) + str(a))
    else:
        print(str(a) + str(b))


if __name__ == "__main__":
    main()
