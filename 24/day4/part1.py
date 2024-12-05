from collections import deque
directions = [(0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
visited = set()  # holds a tuple consisting of current x, y, and direction to avoid repeating a path
count = 0
X_TO_S = ['X', 'M', 'A', 'S']
file_name = 'input'
with open(file_name, 'r') as file:
    lines = [line.strip() for line in file.readlines()]
queue = deque()
queue.append((0, 0, 0, None))  # start node consists of x, y, index_of_route, direction

while queue:
    x, y, ind, direction = queue.popleft()

    if (x, y, direction) in visited:
        continue
    visited.add((x, y, direction))

    if lines[x][y] == X_TO_S[ind]:
        if ind == 3:
            count += 1
            visited.add((x, y, direction))
        else:
            for dx, dy in directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < len(lines) and 0 <= ny < len(lines[0]):
                    if direction is None or direction == (dx, dy):
                        queue.append((x + dx, y + dy, ind + 1, (dx, dy)))
    else:
        for dx, dy in directions:
            if 0 <= x + dx < len(lines) and 0 <= y + dy < len(lines[0]):
                queue.append((x + dx, y + dy, 0, None))

print(count)
