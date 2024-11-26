def main():
    f_in = [input() for _ in range(2)]
    ot = input()
    o = [set(), set()]
    for i in range(len(f_in)):
        with open(f_in[i], 'r', encoding="UTF-8") as file_in:
            for ln in file_in:
                o[i].update({x for x in ln.strip().split()})
    o = sorted([x for x in o[0].symmetric_difference(o[1])])
    with open(ot, 'w', encoding="UTF-8") as file_out:
        for x in o:
            print(x, file=file_out)


if __name__ == "__main__":
    main()
