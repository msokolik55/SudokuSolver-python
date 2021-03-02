from typing import List, Set, Tuple, Optional

Value = int
Row = List[Value]
Playground = Optional[List[Row]]


def remove_duplicities(cells_options: List[List[Set[Value]]],
                       pos: Tuple[int, int], value: Value) -> None:
    i_row, i_col = pos
    for i in range(9):
        cells_options[i_row][i] -= {value}
        cells_options[i][i_col] -= {value}

    new_row, new_col = i_row // 3, i_col // 3
    for i in range(3):
        for j in range(3):
            cells_options[new_row + 1][new_col + 1] -= {value}


def solve_rec(playground: Playground, cells_options: List[List[Set[Value]]], to_input: int) \
        -> Optional[Playground]:

    if to_input == 0:
        return playground

    # inserting only one option
    for i_row, row in enumerate(cells_options):
        for i_col in range(9):
            if len(row[i_col]) == 1:
                value = list(row[i_col])[0]
                playground[i_row][i_col] = value
                pos = (i_row, i_col)
                remove_duplicities(cells_options, pos, value)
                """
                for i in range(9):
                    cells_options[i_row][i] -= {value}
                    cells_options[i][i_col] -= {value}
                """
                to_input -= 1

    # checking duplicities
    for i_row in range(9):
        for i_col in range(9):
            if playground[i_row][i_col] == 0 and len(cells_options[i_row][i_col]) == 0:
                return None

    # if to_input > 0:
    for i_row, row in enumerate(cells_options):
        for i_col in range(9):
            if len(row[i_col]) > 1:
                options: List[Value] = list(row[i_col])
                for opt in options:
                    playground[i_row][i_col] = opt

                    new_plg = [line[:] for line in playground]
                    new_opts = [[elem.copy() for elem in line] for line in cells_options]
                    new_opts[i_row][i_col] = set()

                    pos = (i_row, i_col)
                    remove_duplicities(new_opts, pos, opt)

                    solution = solve_rec(new_plg, new_opts, to_input)
                    if solution is not None:
                        return solution
                    playground[i_row][i_col] = 0
    return None
    # return playground


def solve(playground: Playground) -> Optional[Playground]:
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

    """
    # inserting only one option
    for i_row, row in enumerate(matrix):
        for i_col in range(9):
            if len(row[i_col]) == 1:
                value = list(row[i_col])[0]
                playground[i_row][i_col] = value

                for i in range(9):
                    matrix[i_row][i] -= {value}
                    matrix[i][i_col] -= {value}
                to_input -= 1
    """

    """
    # checking duplicities
    for i_row in range(9):
        for i_col in range(9):
            if playground[i_row][i_col] == 0 and len(matrix[i_row][i_col]) == 0:
                return None, False
    """

    """
    if to_input > 0:
        for i_row, row in enumerate(matrix):
            for i_col in range(9):
                if len(row[i_col]) > 1:
                    options: List[Value] = list(row[i_col])
                    for opt in options:
                        playground[i_row][i_col] = opt
                        new_plg = [line[:] for line in playground]
                        solution, is_result = solve(new_plg)
                        if is_result:
                            return solution, True
                        playground[i_row][i_col] = 0
        return None, False

    return playground, True
    """

    return solve_rec(playground, matrix, to_input)


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
def get_assign_tiles(playground: Playground) -> Optional[List[List[bool]]]:
    if playground is None:
        return

    return [[elem > 0 for elem in row] for row in playground]


def row_without_number(char: str, i_row: int) -> None:
    if i_row % 3 == 2:
        cell = 4 * char
    else:
        cell = char + "---"
    row = f"{9 * cell}{char}"
    alter = ""
    for i in range(len(row) - 1):
        if i % 12 == 0:
            alter += '#'
        else:
            alter += row[i]
    alter += '#'
    print(alter)


def draw(playground: Playground, assign_tiles: List[List[bool]]) -> None:
    if playground is None:
        return

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
                if assign_tiles[i_row][i_col]:
                    print(f"<{elem}>", end=ending)
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
    if playground is None:
        return None

    with open(path, "w") as file:
        for row in playground:
            line = [str(elem) for elem in row]
            file.write(" ".join(line) + '\n')
# END FILE HANDLING


def main() -> None:
    # assignment
    plg: Playground = load_file("input.txt")
    assign_tiles = get_assign_tiles(plg)
    print("Original SUDOKU")
    draw(plg, assign_tiles)

    # solution
    print()
    print("Solved SUDOKU")
    solved = solve(plg)
    draw(solved, assign_tiles)
    save_file("solution.txt", solved)


if __name__ == '__main__':
    main()
