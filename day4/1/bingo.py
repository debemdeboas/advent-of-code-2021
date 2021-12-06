
with open('input.txt') as f:
    data = f.readlines()

pop_order = list(map(lambda x: int(x), data[0].split(',')))
data = data[2:]

boards = []
board = []
for line in data:
    if line == '\n' or line == '\r\n':
        boards.append(board)
        board = []
    else:
        board.append(list(map(lambda x: int(x), line.split())))

print()

def verify_bingo(board, i, j):
    return all(x == 'X' for x in board[i]) \
        or all(l[j] == 'X' for l in board)

def board_mark(board, num) -> bool:
    for i, m in enumerate(board):
        for j, n in enumerate(m):
            if n == num:
                board[i][j] = 'X'
                if verify_bingo(board, i, j):
                    return True
    return False


def play(nums, boards):
    for num in nums:
        for board in boards:
            if board_mark(board, num):
                score = sum(map(lambda x: x if x != 'X' else 0, (x for l in board for x in l)))
                assert(isinstance(score, int))
                score *= num
                return score

print(play(pop_order, boards))
