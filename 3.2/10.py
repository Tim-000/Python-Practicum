def main():
    zn = {
        'А': 'A', 'Б': 'B', 'В': 'V',
        'Г': 'G', 'Д': 'D', 'Е': 'E',
        'Ё': 'E', 'Ж': 'ZH', 'З': 'Z',
        'И': 'I', 'Й': 'I', 'К': 'K',
        'Л': 'L', 'М': 'M', 'Н': 'N',
        'О': 'O', 'П': 'P', 'Р': 'R',
        'С': 'S', 'Т': 'T', 'У': 'U',
        'Ф': 'F', 'Х': 'KH', 'Ц': 'TC',
        'Ч': 'CH', 'Ш': 'SH', 'Щ': 'SHCH',
        'Ы': 'Y', 'Э': 'E', 'Ю': 'IU',
        'Я': 'IA', 'Ь': '', 'Ъ': '',
    }
    for x in (s := input()):
        if x.upper() in zn:
            print(zn[x.upper()].lower().capitalize() if x == x.upper() else zn[x.upper()].lower(), end='')
        else:
            print(x, end='')


if __name__ == "__main__":
    main()
