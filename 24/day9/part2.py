def create_blocks(dense_disk_map):
    id = 0
    res = []
    free_space = []  # will hold the amount of free space and span of the free space
    disk_index_map = {}  # will hold the span of the disks
    for i in range(0, len(dense_disk_map), 2):
        disk_index_map[id] = len(res), len(res) + dense_disk_map[i]
        res.extend([id] * dense_disk_map[i])
        if i + 1 < len(dense_disk_map):
            free_space.append((dense_disk_map[i + 1], len(res), len(res) + dense_disk_map[i + 1]))
            res.extend([' '] * dense_disk_map[i + 1])
        id += 1
    return res, free_space, disk_index_map, id - 1


def fill_open_free_space(cur):
    id_start, id_end = disk_map[cur]
    id_size = id_end - id_start
    for i in range(len(free_space)):
        free_size, free_start, free_end = free_space[i]
        if free_start >= id_end:  # early exit if no free space left of the disk
            break
        if free_size >= id_size:  # if the free space is big enough to fit the disk
            new_start, new_end = free_start, free_start + id_size
            blocks[new_start:new_end] = blocks[id_start:id_end]
            blocks[id_start:id_end] = [' '] * id_size
            if free_size == id_size:  # if we used all the free space, remove it
                free_space.pop(i)
            else:  # otherwise update the free space to the new span
                free_space[i] = (free_size - id_size, new_end, free_end)
            return sum([j * cur for j in range(new_start, new_end)])
    return sum(
        [j * cur for j in range(id_start, id_end)])  # if we didn't find any free space, return the sum of the disk


file_name = 'input'
with open(file_name, 'r') as file:
    data = [int(i) for i in file.read()]
blocks, free_space, disk_map, max_id = create_blocks(data)
res = 0
while max_id > 0:
    res += fill_open_free_space(max_id)
    max_id -= 1
print(res)
