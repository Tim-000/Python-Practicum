def main():
    k, n = 0, int(input())
    for i in range(n):
        s = input()
        if 'зайка' in s:
            k += 1
    print(k)


if __name__ == "__main__":
    main()
