def main():
    o = set()
    for i in range(n := int(input())):
        for x in (s := input().split()):
            o.add(x)
    print(*o, sep='\n')


if __name__ == "__main__":
    main()
