visited = set()  # holds x, y of visited 'a'
count = 0
file_name = 'input'
directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
diagonals = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
with open(file_name, 'r') as file:
    lines = [line.strip() for line in file.readlines()]


def verify_diagonals(x, y):
    ref = {}
    for dx, dy in diagonals:
        if 0 <= x + dx < len(lines) and 0 <= y + dy < len(lines[0]):
            nx, ny = x + dx, y + dy
            letter = lines[nx][ny]
            if letter in ('M', 'S'):
                if letter not in ref:
                    ref[letter] = [(nx, ny)]
                else:
                    ref[letter].append((nx, ny))
    if 'M' not in ref or 'S' not in ref:
        return False
    if len(ref['M']) != 2 or len(ref['S']) != 2:
        return False

    # last thing we need to check is to see if the diagonals are actually MAS and not MAM or SAS
    # we can do this by checking the slope of the lines created by same letters
    # if the slope is not 0 or infinity, then it's not a valid path
    (mx1, my1), (mx2, my2) = ref['M']
    (sx1, sy1), (sx2, sy2) = ref['S']
    m_slope = (my2 - my1) / (mx2 - mx1) if mx2 - mx1 != 0 else float('inf')
    s_slope = (sy2 - sy1) / (sx2 - sx1) if sx2 - sx1 != 0 else float('inf')
    return m_slope == 0 or m_slope == float('inf') and s_slope == 0 or s_slope == float('inf')


for x in range(len(lines)):
    for y in range(len(lines[0])):
        if lines[x][y] == 'A':
            count += int(verify_diagonals(x, y))

print(count)