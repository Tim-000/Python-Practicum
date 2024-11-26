from sys import stdin


def main():
    n, o = input(), []
    with open(n, 'r') as f:
        for ln in f:
            o.extend([int(x) for x in ln.split()])

    print(len(o))
    print(len([x for x in o if x > 0]))
    print(min(o))
    print(max(o))
    print(sum(o))
    print(f'{sum(o) / len(o):.2f}')


if __name__ == "__main__":
    main()
