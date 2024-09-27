def main():
    p, v, t = [int(input()) for _ in range(3)]

    d = {'Петя': p, 'Вася': v, 'Толя': t}
    d = sorted(d.items(), key=lambda item: item[1])[::-1]

    print('{:^24}'.format(f'{d[0][0]}'))
    print('{:^8}'.format(f'{d[1][0]}'))
    print(' ' * 16 + '{:^8}'.format(f'{d[2][0]}'))
    print('{:^8}'.format('II') + '{:^8}'.format('I') + '{:^8}'.format('III'))


if __name__ == "__main__":
    main()
