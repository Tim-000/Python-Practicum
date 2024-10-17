def main():
    l, m = int(input()), []
    for i in range(n := int(input())):
        m.append(s[:l - 3] + '...' if len(s := input()) > l else s)
    for i in range(n):
        print(m[i])


if __name__ == "__main__":
    main()
