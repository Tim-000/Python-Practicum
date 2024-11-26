def main():
    k = int(input())
    a = "abcdefghijklmnopqrstuvwxyz"
    with open("public.txt", encoding="UTF-8") as f:
        rec = f.read()
    sp = [x.lower() for x in rec]
    otv = [a[(a.find(x.lower()) + k) % 26] if x in a else x for x in sp]
    for x in range(len(otv)):
        if rec[x].isupper():
            otv[x] = otv[x].upper()
    with open("private.txt", "w", encoding="UTF-8") as f:
        print(''.join(x for x in otv), file=f)


if __name__ == "__main__":
    main()
