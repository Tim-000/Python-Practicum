from sys import stdin


def main():
    sp = set()
    for x in stdin.readlines():
        for i in x.split():
            if i.lower() == i.lower()[::-1]:
                sp.add(i)
    for x in sorted(sp):
        print(x)


if __name__ == "__main__":
    main()
