import json
from sys import stdin


def main():
    n = input()
    rec = {}
    with open(n, encoding="UTF-8") as file_in:
        rec = json.load(file_in)
    for x in stdin:
        y = x[:x.find('=')].rstrip()
        z = x[x.find('==') + 2:].lstrip()
        rec[y] = z.rstrip()
    with open(n, "w", encoding="UTF-8") as file_out:
        json.dump(rec, file_out, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
