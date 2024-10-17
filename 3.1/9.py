def main():
    while (s := input()) != '':
        if s[0] != '#':
            print(s[:s.find('#')] if "#" in s else s)


if __name__ == "__main__":
    main()
