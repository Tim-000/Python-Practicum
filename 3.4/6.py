from os import remove


def main():
    sp = ['пик', 'треф', 'бубен', 'червей']
    sp.remove(input())
    print(*[f'{i} {x}' for i in range(2, 11) for x in sp], sep='\n')
    print(*[f'{x} {y}' for x in ['валет', 'дама', 'король', 'туз'] for y in sp], sep='\n')


if __name__ == "__main__":
    main()
