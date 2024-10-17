def main():
    m = []
    for i in range(n := int(input())):
        m.append(s := int(input()))
    p = int(input())
    for i in range(len(m)):
        print(m[i] ** p)


if __name__ == "__main__":
    main()
