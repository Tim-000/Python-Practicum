def main():
    sp = []
    for i in range(n := int(input())):
        s = input().split()
        sp.append([nm := s[0], p := s[1:]])
    k, otv = input(), []
    for i in range(n):
        if k in sp[i][1]:
            otv.append(sp[i][0])

    if len(otv) != 0:
        for i in range(len(otv)):
            print(sorted(otv)[i])
    else:
        print('Таких нет')


if __name__ == "__main__":
    main()
