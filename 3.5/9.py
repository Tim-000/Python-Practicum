def clean(n):
    n = n.replace('\t', '')
    while '  ' in n:
        n = n.replace('  ', ' ')
    return n.lstrip().rstrip()


def main():
    a, b = input(), input()
    o = []
    with open(a, 'r', encoding="UTF-8") as f:
        ln = f.readlines()
        for x in ln:
            if x != '\n':
                o.append(clean(x.rstrip()))
    with open(b, 'w', encoding="UTF-8") as file_out:
        for x in o:
            print(x, file=file_out)


if __name__ == "__main__":
    main()
