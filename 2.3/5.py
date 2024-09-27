def main():
    s = 0
    while (n := float(input())) != 0:
        if n >= 500:
            s += n * 0.9
        else:
            s += n
    print(s)


if __name__ == "__main__":
    main()
