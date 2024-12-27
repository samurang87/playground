# Loop through the rows.
# As soon as I find a blank spot, check if any of the remaining words fit.
# If so, call the function with the word filled in, and one less word in the word list.
# Endgame
# If the puzzle is complete, return puzzle and words
# If the puzzle cannot be continued, return none?


def prep_input(input: str) -> tuple[list[str], list[str]]:
    lines = input.strip().split("\n")
    words = lines.pop().split(";")
    return lines, words


def fits(word: str, line: str, index: int) -> bool:
    remaining_line = line[index:]
    if index != 0 and line[index - 1] != "+":
        return False
    if len(remaining_line) < len(word):
        return False
    if len(remaining_line) > len(word) and remaining_line[len(word)] != "+":
        return False
    for i, letter in enumerate(word):
        if remaining_line[i] not in ["-", letter]:
            return False
    return True


def make_new_row_col(word: str, line: str, index: int) -> str:
    start = line[:index]
    end = line[(len(start) + len(word)) :]
    return start + word + end


def do_crossword(grid: list[str], word_list: list[str]) -> list[str]:
    if not word_list:
        if all(["-" not in row for row in grid]):
            return grid
        else:
            return []

    for n_row, row in enumerate(grid):
        for n_col, letter in enumerate(row):
            column = "".join([line[n_col] for line in grid])
            if letter != "+":
                for word in word_list:
                    if fits(word, row, n_col):
                        new_row = make_new_row_col(word, row, n_col)
                        new_grid = grid[:]
                        new_grid[n_row] = new_row
                        result = do_crossword(
                            new_grid, [w for w in word_list if w != word]
                        )
                        if result:
                            return result
                    if fits(word, column, n_row):
                        new_col = make_new_row_col(word, column, n_row)
                        new_grid = [line[:] for line in grid]
                        for n_line in range(len(grid)):
                            new_grid[n_line] = (
                                new_grid[n_line][:n_col]
                                + new_col[n_line]
                                + new_grid[n_line][n_col + 1 :]
                            )
                        result = do_crossword(
                            new_grid, [w for w in word_list if w != word]
                        )
                        if result:
                            return result
    return []


def crosswordPuzzle(grid: list[str], words: str) -> list[str]:
    return do_crossword(grid, words.split(";"))


def crossword_wrapped(input: str) -> str:
    lines, words = prep_input(input)

    res = do_crossword(lines, words)

    return "\n".join(res)
