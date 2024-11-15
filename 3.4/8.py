def main():
    sp = [input() for _ in range(int(input()))]
    for i in range(int(input())):
        print(*sp[i % len(sp):i % len(sp) + 1])


if __name__ == "__main__":
    main()
