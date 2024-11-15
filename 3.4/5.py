def main():
    sp = []
    for i in range(3):
        sp.extend(input().split(', '))
    sp = sorted(sp)
    for i in range(len(sp)):
        print(f'{i + 1}.', sp[i])


if __name__ == "__main__":
    main()
