def main():
    with open("secret.txt", "r", encoding="UTF-8") as f:
        print(''.join([chr(ord(x) % 128) for x in f.read()]))


if __name__ == "__main__":
    main()
