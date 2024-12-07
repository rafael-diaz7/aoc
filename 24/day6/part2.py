direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # start facing up, every turn is 90 degrees clockwise

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


# just brute forcing all possible barriers
# will investigate solution that tries to find squares created in a path
def find_loop(grid, x, y):
    visited_turn_with_direction = set()
    move = 0
    while True:
        dx, dy = direction[move]
        if 0 <= x + dx < len(grid) and 0 <= y + dy < len(grid[0]):
            if is_barrier(grid, x + dx, y + dy):
                if (x, y, move) in visited_turn_with_direction:
                    return 1
                else:
                    visited_turn_with_direction.add((x, y, move))
                move = (move + 1) % 4
                continue
            x += dx
            y += dy
        else:
            return 0
    return 0


grid = read_input("input")
x, y = find_start(grid)
print_grid(grid)
c = 0
for i in range(len(grid)):
    for j in range(len(grid[0])):
        if (i, j) != (x, y):
            copy = [row.copy() for row in grid]
            copy[i][j] = '#'
            c += find_loop(copy, x, y)

print(c)