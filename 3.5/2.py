from sys import stdin


def main():
    s, k = 0, 0
    for x in stdin:
        n, p, v = x.split()
        s += int(v) - int(p)
        k += 1
    print(round(s / k))


if __name__ == "__main__":
    main()
