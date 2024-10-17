def main():
    st = ""
    while (s := input()) != 'ФИНИШ':
        st += s
    ln = str(st).lower().replace(" ", "")
    m, b = 0, ""

    for i in sorted(set(ln)):
        if ln.count(i) > m:
            b = i
            m = ln.count(i)
    print(b)


if __name__ == "__main__":
    main()
