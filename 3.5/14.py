import json


def main():
    a, b = input(), input()
    with open(a, 'r') as f:
        rec = json.load(f)
    with open(b, 'r') as f:
        re2 = json.load(f)
    rec = {i["name"]: {k: v for k, v in i.items() if k != "name"} for i in rec}
    for x in re2:
        if x["name"] in rec:
            for key in x:
                if (key not in rec[x["name"]] or x[key] > rec[x["name"]][key]) and key != "name":
                    rec[x["name"]][key] = x[key]
        else:
            rec[x["name"]] = {k: v for k, v in x.items() if k != "name"}
    with open(a, 'w') as g:
        json.dump(rec, g, ensure_ascii=False, indent=4)


if __name__ == "__main__":
    main()
