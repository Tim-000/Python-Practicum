def main():
    n, m = int(input()), int(input())
    ln = len(str(m * n))
    b = n
    for i in range(1, n + 1):
        t = i
        for j in range(1, m + 1):
            if t == i:
                print('{:>{p}}'.format(t, p=ln), end=' ')
            else:
                print('{:>{p}}'.format(t + b - n, p=ln), end=' ')
            t += b
        print()


if __name__ == "__main__":
    main()
