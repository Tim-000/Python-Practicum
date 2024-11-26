def main():
    f, n = input(), int(input())
    o = []
    with open(f, encoding="UTF-8") as file_in:
        for ln in file_in:
            o.append(ln.strip())
    for x in o[-n:]:
        print(x)


if __name__ == "__main__":
    main()
