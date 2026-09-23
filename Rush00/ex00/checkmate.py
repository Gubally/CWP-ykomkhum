#!/usr/bin/python3

VALID_PIECES = "KQRBP"


def parse_board(board):
    if board.endswith("\n"):
        board = board[:-1]
    rows = board.split("\n")
    return rows


def is_square(rows):
    size = len(rows)
    for row in rows:
        if len(row) != size:
            return False
    return True


def find_king(rows):
    king_position = None
    king_count = 0
    for row_index, row in enumerate(rows):
        for col_index, cell in enumerate(row):
            if cell == "K":
                king_count += 1
                king_position = (row_index, col_index)
    if king_count != 1:
        return None
    return king_position


def is_valid_square(rows, row, col):
    if row < 0 or row >= len(rows):
        return False
    if col < 0 or col >= len(rows[row]):
        return False
    return True


def check_line(rows, king_row, king_col, direction, attacking_pieces):
    row_step, col_step = direction
    row = king_row + row_step
    col = king_col + col_step
    while is_valid_square(rows, row, col):
        cell = rows[row][col]
        if cell in attacking_pieces:
            return True
        if cell in VALID_PIECES:
            return False
        row += row_step
        col += col_step
    return False


def check_pawn(rows, king_row, king_col):
    for col_step in (-1, 1):
        row = king_row + 1
        col = king_col + col_step
        if is_valid_square(rows, row, col):
            if rows[row][col] == "P":
                return True
    return False


def checkmate(board):
    if not isinstance(board, str):
        print("Error: board must be a string.")
        return

    rows = parse_board(board)

    if len(rows) == 0 or not is_square(rows):
        print("Error: board must be a non-empty square.")
        return

    king_position = find_king(rows)
    if king_position is None:
        print("Error: there must be exactly one king on the board.")
        return

    king_row, king_col = king_position

    straight_directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    diagonal_directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

    for direction in straight_directions:
        if check_line(rows, king_row, king_col, direction, "RQ"):
            print("Success")
            return

    for direction in diagonal_directions:
        if check_line(rows, king_row, king_col, direction, "BQ"):
            print("Success")
            return

    if check_pawn(rows, king_row, king_col):
        print("Success")
        return

    print("Fail")
