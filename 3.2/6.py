def main():
    o, sp, k = [], [], 0
    for i in range((n := int(input())) + (m := int(input()))):
        if (s := input()) not in o:
            o.append(s)
        else:
            sp.append(s)
    for i in range(len(sp)):
        while sp[i] in o:
            o.remove(sp[i])
        else:
            ...

    o = sorted(o)
    if len(o) != 0:
        for i in range(len(o)):
            print(o[i])
    else:
        print('Таких нет')


if __name__ == "__main__":
    main()
