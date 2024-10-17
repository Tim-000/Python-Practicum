def main():
    k = 0
    for i in range(n := int(input())):
        k += (s := input()).count('зайка')
    print(k)


if __name__ == "__main__":
    main()
