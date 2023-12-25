# Sudoku Solver

## Overview

Welcome to the Sudoku Solver Python script repository! This script allows you to solve Sudoku puzzles and visualize the solution. It utilizes a backtracking algorithm to find the solution to a given Sudoku puzzle.

## Features

- **Sudoku Solving:**
  Solve Sudoku puzzles of varying difficulties using a backtracking algorithm.

- **Visualization:**
  Visualize the original Sudoku puzzle and the solved result.

- **File Handling:**
  Load Sudoku puzzles from a text file and save the solved puzzle to another file.

## Usage

1. **Load Sudoku Puzzle:**
   - Prepare a text file (`input.txt`) with the Sudoku puzzle. Use '0' to represent empty cells.
   - Each row in the file should represent a row in the Sudoku grid, and numbers should be separated by spaces.

2. **Run the Solver:**
   - Execute the script (`sudoku_solver.py`).

3. **View Results:**
   - The script will display the original Sudoku puzzle and the solved result.

4. **Save Solution:**
   - The solved puzzle will be saved to a text file (`solution.txt`).

## Requirements

- **Python 3:** Ensure you have Python 3 installed on your system.

## File Format

The Sudoku puzzle file (`input.txt`) should follow the format below:

5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9

## License

This Sudoku Solver script is licensed under MIT - see the [LICENSE](LICENSE) file for details.
