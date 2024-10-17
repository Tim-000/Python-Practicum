def main():
    ln = int(input()) - 3
    for i in range(int(input())):
        if ln < 0:
            break
        elif len(s := input()) >= ln:
            print(s[:ln] + '...')
        else:
            print(s)
        ln -= len(s)


if __name__ == "__main__":
    main()
