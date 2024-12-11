from collections import deque

DIRECTIONS = [(0, 1), (1, 0), (0, -1), (-1, 0)]
FILE_NAME = "input"
scores = {}

def find_starts(path):
    starts = []
    for i in range(len(path)):
        for j in range(len(path[i])):
            if path[i][j] == 0:
                starts.append((i, j))
    return starts


def bfs(x, y, is_part1=True):
    visited = set()  # part 1
    total = 0  # part 2
    queue = deque([(x, y, 0)])
    while queue:
        x, y, height = queue.popleft()
        if height == 9:
            visited.add((x, y))  # part 1
            total += 1  # part 2
        for dx, dy in DIRECTIONS:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < len(path) and 0 <= new_y < len(path[0]) and path[new_x][new_y] == height + 1:
                queue.append((new_x, new_y, height + 1))
    return len(visited) if is_part1 else total


with open(FILE_NAME, 'r') as file:
    path = [[int(i) for i in line.strip()] for line in file.readlines()]

res = 0
for start in find_starts(path):
    res += bfs(start[0], start[1], False)
print(res)
