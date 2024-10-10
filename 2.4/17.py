def main():
    k = 0
    for i in range(int(input())):
        if (s := input()) == s[::-1]:
            k += 1
    print(k)


if __name__ == "__main__":
    main()
