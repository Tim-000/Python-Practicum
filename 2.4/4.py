def main():
    n = int(input())
    s = 0
    for i in range(n):
        s += sum(int(x) for x in str(input()))
    print(s)


if __name__ == "__main__":
    main()
