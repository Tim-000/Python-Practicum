def main():
    m = []
    for i in range(int(input())):
        m.append(s.find('зайка') + 1 if (s := input()).find('зайка') != -1 else 'Заек нет =(')
    for i in range(len(m)):
        print(m[i])


if __name__ == "__main__":
    main()
