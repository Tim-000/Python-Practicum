from sys import stdin


def o4(x):
    x = x.replace('\n', ' ')
    while '  ' in x:
        x = x.replace('  ', ' ')
    return x


def main():
    n = input()
    fl = False
    sp = [x.strip() for x in stdin]
    for x in sp:
        with open(x, encoding="UTF-8") as f_in:
            rec = ''.join(f_in.readlines()).lower()
            if n.lower() in o4(rec):
                print(x)
                fl = True
    if not (fl):
        print("404. Not Found")


if __name__ == "__main__":
    main()
