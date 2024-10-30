def main():
    sp = {}
    for i in range(int(input())):
        if (s := input()) not in sp:
            sp[s] = 1
        else:
            sp[s] += 1
    sp = sorted(sp.items())
    if all(x[1] <= 1 for x in sp):
        print('Однофамильцев нет')
    else:
        for i in sp:
            if i[1] > 1:
                print(i[0], '-', i[1])


if __name__ == "__main__":
    main()
