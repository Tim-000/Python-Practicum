def main():
    a, b, c = [int(input()) for _ in range(3)]
    m = [a, b, c]
    a = max(m)
    m.remove(a)
    b = m[0]
    c = m[1]
    if a ** 2 == (b ** 2 + c ** 2):
        print('100%')
    elif a ** 2 > (b ** 2 + c ** 2):
        print('велика')
    else:
        print('крайне мала')


if __name__ == "__main__":
    main()
