class Board:

    def __init__(self, rows):
        self.rows = [row.lstrip(' ').replace('  ',' ').split(' ') for row in rows]
        
    @property    
    def columns(self):
        columns = []
        for i in range(5):
            column = []
            for row in self.rows:
                column.append(row[i])
            columns.append(column)
        return columns
    
    @property
    def cells(self):
        return [cell for row in self.rows for cell in row]
        
    @property
    def lines(self):
        return self.rows + self.columns
    
    @property        
    def has_line(self):
        return any([True for line in self.lines if all([cell == 'X' for cell in line])])
    
    @property
    def score(self):
        return sum([int(cell) for cell in self.cells if cell != 'X'])
    
    def check(self, call):
        for i, row in enumerate(self.rows):
            for j, cell in enumerate(row):
                if cell == call:
                    self.rows[i][j] = 'X'
    
    
file = open("puzzle_input.txt", "r")
lines = [line.rstrip('\n') for line in file]

calls = lines[0].split(',')

bingo_rows = list(filter(None, lines[1:]))
boards = [Board(bingo_rows[i:i + 5]) for i in range(0, len(bingo_rows), 5)]


# PART ONE
# won = False
# for call in calls:
#     for board in boards:
#         board.check(call)
#         if board.has_line:
#             print(int(call) * board.score)
#             won = True
#             break
#     if won == True:
#         break
    
# PART TWO
final_board = None
for call in calls:
    for board in boards:
        board.check(call)
    uncompleted_board_count = len([board for board in boards if not board.has_line])
    if uncompleted_board_count == 1:
        final_board = [board for board in boards if not board.has_line][0]
    if uncompleted_board_count == 0:
        print(int(call) * final_board.score)
        break    
