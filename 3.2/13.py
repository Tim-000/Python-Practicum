def main():
    sp, otv = {}, []
    for i in range(n := int(input())):
        sp[(s := input())] = 0
    for i in range(m := int(input())):
        for j in range(int(input())):
            sp[(s := input())] += 1
    for i in sp.items():
        if i[1] == 0:
            otv.append(i[0])
    otv = sorted(otv)
    if len(otv) == 0:
        print('Готовить нечего')
    else:
        for i in range(len(otv)):
            print(otv[i])


if __name__ == "__main__":
    main()
