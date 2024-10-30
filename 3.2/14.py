def main():
    sp, p, otv = [], [], []
    for i in range(int(input())):
        sp.append(input())
    for i in range(int(input())):
        r = input()
        for j in range(int(input())):
            p.append(input())
        if all(x in sp for x in p):
            otv.append(r)
        p = []
    otv = sorted(otv)
    if len(otv) == 0:
        print('Готовить нечего')
    else:
        for i in range(len(otv)):
            print(otv[i])


if __name__ == "__main__":
    main()
