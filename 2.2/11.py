def main():
    n = int(input())
    m = [int(x) for x in str(n)]
    s = max(m) + min(m)
    m.remove(max(m))
    m.remove(min(m))
    if m[0] * 2 == s:
        print('YES')
    else:
        print('NO')


if __name__ == "__main__":
    main()
