import os


def main():
    r = os.path.getsize(input())
    if r >= 1024 ** 3:
        r = int(r / 1024 ** 3) + 1
        d = 'ГБ'
    elif r >= 1024 ** 2:
        r = int(r / 1024 ** 2) + 1
        d = 'МБ'
    elif r >= 1024:
        r = int(r / 1024) + 1
        d = 'КБ'
    else:
        d = 'Б'
    print(str(r) + d)


if __name__ == "__main__":
    main()
