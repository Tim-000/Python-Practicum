def main():
    m = []
    for i in range(n := int(input())):
        m.append((s := input()))
    p = input().lower()
    for i in range(len(m)):
        s = m[i].lower()
        if p in s:
            print(m[i])


if __name__ == "__main__":
    main()
