def main():
    p, v, t = int(input()), int(input()), int(input())

    m = max(p, v, t)
    if m == p:
        print('Петя')
    if m == v:
        print('Ваня')
    if m == t:
        print('Толя')


if __name__ == "__main__":
    main()
