def main():
    print('Как Вас зовут?')
    n = input()
    print('Здравствуйте,', n + '!')
    print('Как дела?')
    o = input()
    if o == 'хорошо':
        print('Я за вас рада!')
    else:
        print('Всё наладится!')


if __name__ == "__main__":
    main()
