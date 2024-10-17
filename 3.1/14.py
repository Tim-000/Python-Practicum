def main():
    m = list(map(int, input().split()))
    c = int(input())
    for i in m:
        print(i ** c, end=' ')


if __name__ == "__main__":
    main()
