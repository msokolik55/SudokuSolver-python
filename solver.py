from typing import List, Set, Tuple

Value = int
Row = List[Value]
Playground = List[Row]


def solve(playground: Playground) -> Tuple[Playground, bool]:
    rows_available = available_in_rows(playground)
    cols_available = available_in_cols(playground)
    matrix: List[List[Set[Value]]] = []
    to_input = 0
    for i_row in range(9):
        matrix.append([])
        for i_col in range(9):
            square_available = available_in_squares(playground)
            if playground[i_row][i_col] != 0:
                matrix[i_row].append(set())
                continue
            available = rows_available[i_row].copy()
            available = available.intersection(cols_available[i_col])
            available = available.intersection(
                square_available[i_row // 3][i_col // 3])
            to_input += 1
            matrix[i_row].append(available)

    for i_row, row in enumerate(matrix):
        for i_col in range(9):
            if len(row[i_col]) == 1:
                playground[i_row][i_col] = list(row[i_col])[0]
                matrix[i_row][i_col] = set()
                to_input -= 1

    if to_input > 0:
        for i_row, row in enumerate(matrix):
            for i_col in range(9):
                if len(row[i_col]) > 1:
                    options: List[Value] = list(row[i_col])
                    for opt in options:
                        playground[i_row][i_col] = opt
                        new_plg = playground.copy()
                        solution, is_result = solve(new_plg)
                        if is_result:
                            return solution, True
                        playground[i_row][i_col] = 0
        return playground, False

    return playground, True


def available_in_square(playground: Playground, pos: Tuple[int, int]) \
        -> Set[Value]:
    row, col = pos
    used: Set[Value] = set()
    for i_row in range(3):
        for i_col in range(3):
            used.add(playground[row + i_row][col + i_col])
    return set(range(10)) - used


def available_in_squares(playground: Playground) -> List[List[Set[Value]]]:
    result: List[List[Set[Value]]] = []
    for i_row in range(0, 9, 3):
        result.append([])
        for i_col in range(0, 9, 3):
            result[i_row // 3].append(
                available_in_square(playground, (i_row, i_col)))
    return result


def available_in_col(playground: Playground, pos: Tuple[int, int]) \
        -> Set[Value]:
    row, col = pos
    used: Set[Value] = set([row[col] for row in playground])
    return set(range(10)) - used


def available_in_cols(playground: Playground) -> List[Set[Value]]:
    result: List[Set[Value]] = []
    for i_col in range(9):
        result.append(available_in_col(playground, (0, i_col)))
    return result


def available_in_row(playground: Playground, pos: Tuple[int, int]) \
        -> Set[Value]:
    row, _ = pos
    used: Set[Value] = set(playground[row])
    return set(range(10)) - used


def available_in_rows(playground: Playground) -> List[Set[Value]]:
    result: List[Set[Value]] = []
    for i_row in range(9):
        result.append(available_in_row(playground, (i_row, 0)))
    return result


# DRAW
def row_without_number(char: str, i_row: int) -> None:
    if i_row % 3 == 2:
        cell = 4 * char
    else:
        cell = char + "---"
    row = f"{9 * cell}{char}"
    # row = '#' + row[1:-1] + '#'
    alter = ""
    for i in range(len(row) - 1):
        if i % 12 == 0:
            alter += '#'
        else:
            alter += row[i]
    alter += '#'
    print(alter)


def draw(playground: Playground) -> None:
    print(f"{(4 * 9 + 1) * '#'}")
    for i_row, row in enumerate(playground):
        print('#', end='')
        for i_col, elem in enumerate(row):
            if i_col % 3 == 2:
                ending = '#'
            else:
                ending = '|'
            if elem == 0:
                print("   ", end=ending)
            else:
                print(f" {elem} ", end=ending)
        print()
        if i_row % 3 == 2:
            row_without_number('#', i_row)
        else:
            row_without_number('+', i_row)
# END DRAW


# FILE HANDLING
def load_file(path: str) -> Playground:
    playground: Playground = []
    with open(path, "r") as file:
        for line in file:
            row = line.split()
            playground.append([int(elem) for elem in row])
    return playground


def save_file(path: str, playground: Playground) -> None:
    with open(path, "w") as file:
        for row in playground:
            line = [str(elem) for elem in row]
            file.write(" ".join(line) + '\n')
# END FILE HANDLING


def main() -> None:
    plg: Playground = load_file("input.txt")
    """plg: Playground = [[0, 5, 0, 2, 4, 0, 1, 9, 8],
                       [4, 9, 0, 1, 0, 6, 7, 0, 0],
                       [0, 1, 2, 3, 0, 8, 5, 6, 0],
                       [0, 2, 0, 5, 0, 0, 0, 0, 0],
                       [9, 0, 7, 0, 2, 0, 0, 0, 0],
                       [1, 4, 0, 0, 3, 9, 2, 8, 0],
                       [0, 0, 4, 9, 7, 5, 3, 2, 1],
                       [2, 7, 0, 8, 1, 0, 0, 4, 5],
                       [5, 3, 1, 0, 0, 2, 8, 7, 0]]"""
    print("Original SUDOKU")
    draw(plg)
    """solved_plg, _ = solve(plg)"""
    print()
    print("Solved SUDOKU")
    solve(plg)
    """draw(solved_plg)"""
    draw(plg)
    save_file("solution.txt", plg)


if __name__ == '__main__':
    main()
