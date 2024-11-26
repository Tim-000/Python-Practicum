def g(p):
    ct, nt = 0, 0
    for x in p:
        if int(x) % 2 == 0:
            ct += 1
        else:
            nt += 1
    if ct > nt:
        return 0
    elif nt > ct:
        return 1
    return 2


def main():
    a, b, c, d = [input() for _ in range(4)]
    m, k = [], 0
    with open(a, encoding="UTF-8") as file_in:
        for ln in file_in:
            m.append([x for x in ln.split()])
    for t in b, c, d:
        with open(t, "w", encoding="UTF-8") as file_out:
            for i in range(len(m)):
                for j in m[i]:
                    if g(j) == k:
                        print(j, end=' ', file=file_out)
                print('', file=file_out)
        k += 1


if __name__ == "__main__":
    main()
