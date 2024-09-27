def main():
    e, g, c = [int(input()) for _ in range(3)]

    if e // 10 == g // 10 == c // 10:
        print(e // 10)
    else:
        print(e % 10)


if __name__ == "__main__":
    main()
