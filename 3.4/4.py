def main():
    for i in range(len(s := input().split())):
        print(*s[:i + 1])


if __name__ == "__main__":
    main()
