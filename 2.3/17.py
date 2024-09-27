def main():
    n = int(input())
    d = [int(x) for x in str(n) if int(x) % 2 != 0]
    s = ''
    for i in range(len(d)):
        s += str(d[i])
    print(s)


if __name__ == "__main__":
    main()
