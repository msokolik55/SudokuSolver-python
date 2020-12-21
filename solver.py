from typing import List, Set, Optional

Row = List[int]
Playground = List[Row]


def row_without_number() -> None:
    print(f"{9 * '+---'}+")


def draw(playground: Playground) -> None:
    row_without_number()
    for row in playground:
        print('|', end='')
        for elem in row:
            if elem == 0:
                print("   ", end='|')
            else:
                print(f" {elem} ", end='|')
        print()
        row_without_number()


def main():
    plg: Playground = [[0, 5, 0, 2, 4, 0, 1, 9, 8],
                       [4, 9, 0, 1, 0, 6, 7, 0, 0],
                       [0, 1, 2, 3, 0, 8, 5, 6, 0],
                       [0, 2, 0, 5, 0, 0, 0, 0, 0],
                       [9, 0, 7, 0, 2, 0, 0, 0, 0],
                       [1, 4, 0, 0, 3, 9, 2, 8, 0],
                       [0, 0, 4, 9, 7, 5, 3, 2, 1],
                       [2, 7, 0, 8, 1, 0, 0, 4, 5],
                       [5, 3, 1, 0, 0, 2, 8, 7, 0]]
    draw(plg)


if __name__ == '__main__':
    main()
