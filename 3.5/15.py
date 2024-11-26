from sys import stdin
import json


def main():
    ans = [x.strip() for x in stdin]
    with open("scoring.json", encoding="UTF-8") as f:
        rec = json.load(f)
    s, k = 0, 0
    rec = [{i["pattern"]: k["points"] // len(k["tests"]) for i in k["tests"]} for k in rec]
    for i in rec:
        for j in range(k, len(i) + k):
            if ans[j] in i:
                s += i[ans[j]]
            k += 1
    print(s)


if __name__ == "__main__":
    main()
