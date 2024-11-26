from sys import stdin


def main():
    for x in stdin.readlines():
        if x[0] != '#':
            print(x[:x.find('#')])


if __name__ == "__main__":
    main()
