def main():
    sp = {}
    while (s := input()) != '':
        st = s.split()
        for i in range(len(st)):
            if st[i] not in sp:
                sp[st[i]] = 1
            else:
                sp[st[i]] += 1
    for i in sp.items():
        print(*i)


if __name__ == "__main__":
    main()
