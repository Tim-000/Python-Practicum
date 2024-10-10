def main():
    n = int(input())
    for i in range(1, n + 1):
        for j in range(i + 2, 0, -1):
            print('До старта', j, 'секунд(ы)')
        print('Старт ' + str(i) + '!!!')


if __name__ == "__main__":
    main()
