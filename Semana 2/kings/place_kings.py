import sys



def place_kings(height, width):
    recursion_limit = sys.getrecursionlimit()
    sys.setrecursionlimit(200000)
    if (height == 1 and width == 1):
        return 0

    places = [[False for x in range(height)] for y in range(width)]
    add_king(0, 0, places)
    flat = [x for sublist in places for x in sublist]
    sys.setrecursionlimit(recursion_limit)
    return flat.count(True)


def add_king(x, y, current_board):
    current_board[x][y] = True
    within_limits = verify_condition(x, y, current_board)
    if (not has_more_places(x, y, len(current_board), len(current_board[0]))):
        current_board[x][y] = within_limits
        return within_limits
    new_x, new_y = move_forward(
        x, y, len(current_board), len(current_board[0]))
    if (within_limits):
        return add_king(new_x, new_y, current_board)
    else:
        current_board[x][y] = False
        return add_king(new_x, new_y, current_board)


def has_more_places(x, y, max_column, max_row):
    return not (x + 1 == max_column and y + 1 == max_row)


def verify_condition(x, y, current_board):
    return check_king(x - 1, y - 1, current_board) and check_king(x, y - 1, current_board) and check_king(x + 1, y - 1, current_board) and check_king(x - 1, y, current_board)


def move_forward(x, y, max_column, max_row):
    if (x + 1 < max_column):
        return (x + 1, y)
    else:
        return (0, y + 1)


def check_king(x, y, current_board):
    if (x < 0 or y < 0 or x >= len(current_board) or y >= len(current_board[0])):
        return True

    has_free_space = is_free(x, y, current_board) or is_free(x-1, y-1, current_board) or is_free(x, y-1, current_board) or is_free(x+1, y-1, current_board) or is_free(
        x-1, y, current_board) or is_free(x+1, y, current_board) or is_free(x-1, y+1, current_board) or is_free(x, y+1, current_board) or is_free(x+1, y+1, current_board)
    return has_free_space


def is_free(x, y, board):
    if (x < 0 or y < 0):
        return False
    if (x >= len(board) or y >= len(board[0])):
        return False

    return not board[x][y]
