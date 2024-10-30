def main():
    otv = []
    for x in (input()).split():
        s = bin(int(x))[1:]
        otv.append({'digits': len(s) - 1, 'units': s.count('1'), 'zeros': s.count('0')})
    print(otv)


if __name__ == "__main__":
    main()
