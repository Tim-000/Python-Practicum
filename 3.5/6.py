from sys import stdin


def main():
    lit = {
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
    d, o = '', ''
    with open("cyrillic.txt", encoding="UTF-8") as file_in:
        for line in file_in:
            d += line

    for i in d:
        if i.upper() in lit:
            o += lit[i.upper()].lower().capitalize() if i == i.upper() else lit[i.upper()].lower()
        else:
            o += i

    with open("transliteration.txt", "w", encoding="UTF-8") as file_out:
        print(o, file=file_out)


if __name__ == "__main__":
    main()
