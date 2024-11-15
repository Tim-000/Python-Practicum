def main():
    o = []
    for i in range(int(input())):
        o.extend(input().split(', '))
    o = sorted(o)
    for i in range(len(o)):
        print(f'{i + 1}. {o[i]}')


if __name__ == "__main__":
    main()
