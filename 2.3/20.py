def main():
    n = int(input())
    pr = 0
    o = - 1
    for i in range(n):
        b = int(input())
        h, r, m = b % 256, (b // 256) % 256, b // (256 ** 2)
        h1 = ((m + r + pr) * 37) % 256
        if h1 != h or h >= 100:
            o = i
            break
        pr = h
    print(o)


if __name__ == "__main__":
    main()
