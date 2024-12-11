def create_blocks(dense_disk_map):
    id = 0
    res = []
    for i in range(0, len(dense_disk_map), 2):
        res.extend([id] * dense_disk_map[i])
        res.extend([' '] * dense_disk_map[i+1] if i+1 < len(dense_disk_map) else [])
        id += 1
    return res


def move_blocks(blocks):
    l, r = 0, len(blocks)-1
    while l < r:
        if blocks[l] == ' ' and blocks[r] != ' ':
            blocks[l], blocks[r] = blocks[r], ''
            l += 1
            r -= 1
        if blocks[l] != ' ':
            l += 1
        if blocks[r] == ' ':
            r -= 1
    return blocks[:l]


file_name = 'input'
with open(file_name, 'r') as file:
    data = [int(i) for i in file.read()]
blocks = create_blocks(data)
moved_blocks = move_blocks(blocks)
res = 0
for i in range(len(moved_blocks)):
    res += i * int(moved_blocks[i])
print(res)