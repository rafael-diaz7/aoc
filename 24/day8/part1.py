import itertools
antinodes = set()

def get_info(filename):
    with open(filename) as f:
        return [i.strip() for i in f.readlines()]


def create_map(data):
    res = {}
    for y, i in enumerate(data):
        for x, antenna in enumerate(i):
            if antenna == '.':
                continue
            if antenna in res:
                res[antenna].append((x, y))
            else:
                res[antenna] = [(x, y)]
    return res


def calculate_slope(p1, p2):
    return p2[1] - p1[1], p2[0] - p1[0]


def calculate_antinodes(data, antenna_locations):
    max_x = len(data[0])
    max_y = len(data)
    for p1, p2 in itertools.combinations(antenna_locations, 2):
        dy, dx = calculate_slope(p1, p2)
        for i in (p1, p2):
            x, y = i
            for mult in (1, -1):
                x2 = x + dx * mult
                y2 = y + dy * mult
                if 0 <= x2 < max_x and 0 <= y2 < max_y and (x2, y2) not in antinodes and (x2, y2) not in (p1, p2):
                    antinodes.add((x2, y2))


data = get_info('input')
antennas = create_map(data)
# this is going to be so inefficient but I'm going to generate every possible combination for each antenna within
# a dictionary and then attempt to place an antinode following the slope of the antenna combinations
for antenna_type in antennas.keys():
    calculate_antinodes(data, antennas[antenna_type])
print(len(antinodes))
print(antinodes)