def main():
    ln = int(input())
    s = [input() for _ in range(int(input()))]

    t = ln
    for i in s:
        if t <= 3:
            break
        print(i[:t:] if (t - len(i)) > 3 else i[:t - 3:] + "...")
        t -= len(i)


if __name__ == "__main__":
    main()
