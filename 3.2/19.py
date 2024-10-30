def main():
    otv = []
    for i in range(int(input())):
        _, b = input().split(": ")
        otv.extend(set(b.split(", ")))
    otv = [x for x in otv if otv.count(x) == 1]
    print(*(sorted(otv)), sep="\n")


if __name__ == "__main__":
    main()
