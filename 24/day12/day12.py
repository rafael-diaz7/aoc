from collections import deque

directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def get_grid(filename):
    with open(filename) as f:
        return [line.strip() for line in f.readlines()]


def solve1(grid):
    total = 0
    visited = set()
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (i, j) in visited:
                continue
            # perimeter is number of cells not same as current cell around it
            # area is just number of cells
            letter = grid[i][j]
            queue = deque([(i, j)])
            area, perimeter = 0, 0
            while queue:
                y, x = queue.popleft()
                if (y, x) in visited:
                    continue
                visited.add((y, x))
                cur = grid[y][x]
                area += 1
                perimeter += sum(
                    [int(is_not_same_or_out_of_bounds(grid, y + dy, x + dx, cur)) for dy, dx in directions])
                for dy, dx in directions:
                    if is_valid(grid, y + dy, x + dx) and (y + dy, x + dx) and is_same(grid, y + dy, x + dx,
                                                                                       letter) and (
                    y + dy, x + dx) not in visited:
                        queue.append((y + dy, x + dx))
            total += area * perimeter
    return total


def is_valid(grid, i, j):
    return 0 <= i < len(grid) and 0 <= j < len(grid[i])


def is_same(grid, i, j, cur):
    return grid[i][j] == cur


def is_not_same_or_out_of_bounds(grid, i, j, cur):
    return not is_valid(grid, i, j) or not is_same(grid, i, j, cur)


print(solve1(get_grid("input")))
