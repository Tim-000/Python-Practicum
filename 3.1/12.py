def main():
    m = ['Манная', 'Гречневая', 'Пшённая', 'Овсяная', 'Рисовая']
    for i in range(n := int(input())):
        ind = i % 5
        print(m[ind])


if __name__ == "__main__":
    main()
