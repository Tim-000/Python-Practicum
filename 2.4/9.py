def main():
    s = ''
    for i in range(int(input())):
        s = s + str(max(int(x) for x in input()))
    print(s)


if __name__ == "__main__":
    main()
