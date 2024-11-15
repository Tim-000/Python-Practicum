from itertools import permutations


def main():
    sp = []
    for i in range(n := int(input())):
        sp.append(input())
    sp = sorted(sp)
    for x in permutations(sp, 3):
        print(', '.join(x))


if __name__ == "__main__":
    main()
