import json


def main():
    a, b = [input() for _ in range(2)]
    m = []
    with open(a, encoding="UTF=8") as file_in:
        for ln in file_in:
            m.extend([int(x) for x in ln.split()])

    rec = {"count": len(m),
           "positive_count": len([x for x in m if int(x) > 0]),
           "min": min(m),
           "max": max(m),
           "sum": sum(m),
           "average": "{:.2f}".format(sum(m) / len(m))}
    with open(b, "w", encoding="UTF-8") as file_out:
        json.dump(rec, file_out, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    main()
