def main():
    s1, s2, s3 = [input() for _ in range(3)]

    m = [s1, s2, s3]
    m = sorted(m)

    for i in range(3):
        if 'зайка' in m[i]:
            print(m[i], len(m[i]))
            break


if __name__ == "__main__":
    main()
