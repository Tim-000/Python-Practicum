def main():
    k, sp = 0, {}
    for i in range(n := int(input())):
        if (s := input()) not in sp:
            sp[s] = 1
        else:
            sp[s] += 1
    for i in sp.values():
        if i > 1:
            k += i
    print(k)


if __name__ == "__main__":
    main()
