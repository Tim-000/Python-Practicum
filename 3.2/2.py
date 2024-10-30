def main():
    a = input()
    for i in (set(s := input())):
        if i in a:
            print(i, end='')


if __name__ == "__main__":
    main()
