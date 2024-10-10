def main():
    n = int(input())
    m = [0] * n
    for i in range(n):
        while (s := input()) != 'ВСЁ':
            if 'зайка' in s:
                m[i] = 1

    print(sum(m[i] for i in range(n)))


if __name__ == "__main__":
    main()
