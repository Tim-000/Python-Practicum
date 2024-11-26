from sys import stdin


def main():
    s = 0
    for x in stdin:
        s += sum(int(k) for k in x.split())
    print(s)


if __name__ == "__main__":
    main()
