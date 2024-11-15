def main():
    sp = []
    for i in range(2):
        sp.append(input().split(', '))
    if len(sp[0]) == len(sp[1]):
        for i in range(len(sp[0])):
            print(sp[0][i], '-', sp[1][i])
    else:
        for i in range(min(len(sp[0]), len(sp[1]))):
            print(sp[0][i], '-', sp[1][i])


if __name__ == "__main__":
    main()
