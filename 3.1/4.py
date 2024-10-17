def main():
    m = []
    while (s := input()) != '':
        if s[:2] == '##' and s[-3:] != '@@@':
            m.append(s[2:])
        elif s[-3:] == '@@@':
            pass
        else:
            m.append(s)
    for i in range(len(m)):
        print(m[i])


if __name__ == "__main__":
    main()
