def main():
    n = int(input())
    m = []
    for i in range(n):
        m.append(input())
    m = sorted(m)
    print(m[0])


if __name__ == "__main__":
    main()
