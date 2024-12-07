direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # start facing up, every turn is 90 degrees clockwise
move = 0
visited = set()

def read_input(filename):
    with open(filename) as f:
        return [list(line.strip()) for line in f]


def find_start(grid):
    for i, row in enumerate(grid):
        for j, cell in enumerate(row):
            if cell == '^':
                return i, j


def is_barrier(grid, x, y):
    return grid[x][y] == '#'


def print_grid(grid):
    for row in grid:
        print(''.join(row))


grid = read_input("input")
x, y = find_start(grid)
visited.add((x, y))
print_grid(grid)
while True:
    visited.add((x, y))
    dx, dy = direction[move]
    if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
        if is_barrier(grid, x + dx, y + dy):
            move = (move + 1) % 4
            continue
        x += dx
        y += dy
    else:
        break
print(len(visited))