def main():
    for i in range(1, n := int(input()) + 1):
        print(*[f'{x * i}' for x in range(1, n)], end=' ')
        print()


if __name__ == "__main__":
    main()
