def main():
    c, v, k = [int(input()) for _ in range(3)]
    it = c * v
    if k > it:
        print(k - it)
    else:
        print(0)


if __name__ == "__main__":
    main()
