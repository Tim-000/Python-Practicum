from sys import stdin


def main():
    sp = []
    for x in stdin.readlines():
        sp.append(x.rstrip("\n"))
    p = sp.pop(-1).lower()
    for i in sp:
        if p in i.lower():
            print(i)


if __name__ == "__main__":
    main()
