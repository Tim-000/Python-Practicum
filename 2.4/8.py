def main():
    mn, mx = '', 0
    for i in range(int(input())):
        n, x = input(), int(input())
        if sum(int(a) for a in str(x)) >= mx:
            mx = sum(int(a) for a in str(x))
            mn = n
    print(mn)


if __name__ == "__main__":
    main()
