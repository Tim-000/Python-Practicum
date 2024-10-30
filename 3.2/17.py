def main():
    f = {}
    while (s := input()) != "":
        n1, n2 = s.split()
        if n1 not in f:
            f[n1] = [n2]
        else:
            f[n1].extend([n2])
        if n2 not in f:
            f[n2] = [n1]
        else:
            f[n2].extend([n1])

    f2 = {x: [] for x in set(f.keys())}
    p = []
    for i, j in f.items():
        for k in j:
            if (i, k) not in p:
                p.append((i, k))
                p.append((k, i))
                f2[i].extend(f[k])
                f2[k].extend(f[i])

    for i in f2:
        f2[i] = [x for x in set(f2[i]) if x != i and x not in f[i]]

    for i in sorted(f2):
        print(f"{i}: ", end="")
        print(*(sorted(f2[i])), sep=", ")


if __name__ == "__main__":
    main()
