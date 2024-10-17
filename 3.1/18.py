def main():
    s = input()
    k = 1
    curr_num = s[0]
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            k += 1
            if i == len(s) - 2:
                print(s[i], k)
        else:
            print(s[i], k)
            k = 1
            curr_num = s[i + 1]
    if s[-2] != s[-1]:
        print(s[-1], 1)


if __name__ == "__main__":
    main()
