from itertools import permutations, product


def main():
    n = input()
    s = ['бубен', 'пик', 'треф', 'червей']
    bs = [x for x in s if x[0] == n[0]][0]
    nm = sorted([*[str(x) for x in range(2, 11)], "валет", "дама", "король", "туз"])
    nm.remove(input())
    card_list = [f"{value} {suit}" for value, suit in product(nm, s)]
    card_layout_list = [', '.join(card_layout) for card_layout in product(card_list, repeat=3) if
                        len(set(card_layout)) == 3]
    print(*[card_layout for card_layout in card_layout_list if bs in card_layout][:10], sep="\n")


if __name__ == "__main__":
    main()
