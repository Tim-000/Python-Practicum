def main():
    a, b, k = int(input()), int(input()), 0
    ln = len(str(a * b))
    for i in range(a):
        for j in range(1, b + 1):
            print('{:>{p}}'.format(j + k, p=ln), end=' ')
        k += b
        print()


if __name__ == "__main__":
    main()
