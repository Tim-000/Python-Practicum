def main():
    print('YES' if (s := input()).lower().replace(' ', '') == s[::-1].lower().replace(' ', '') else 'NO')


if __name__ == "__main__":
    main()
