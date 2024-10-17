import math


def main():
    s, otv = input(), []
    lt = list(s.split())
    for x in lt:
        if x.isdigit():
            otv.append(int(x))
        elif x == '/':
            a = otv.pop()
            otv[-1] //= a
        elif x == '~':
            otv[-1] = -otv[-1]
        elif x == '!':
            otv[-1] = math.factorial(otv[-1])
        elif x == '#':
            otv.append(otv[-1])
        elif x == '@':
            otv.append(otv.pop(-3))
        else:
            a = otv.pop()
            exec('otv[-1]' + x + '=a')
    print(*otv)


if __name__ == "__main__":
    main()
