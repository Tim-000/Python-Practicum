def main():
    k = 0
    for i in range(n := int(input())):
        if (s := input())[0] in 'АБВабв':
            k += 1
    if k == n:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()
