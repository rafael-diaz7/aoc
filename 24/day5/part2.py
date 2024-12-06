FILE_NAME = 'input'
is_order = True
order = {}
order_lines = []
update_lines = []


def populate_order_map(orders: list) -> None:
    for order_pair in orders:
        k, v = map(int, order_pair.split('|'))
        if k in order:
            order[k].add(v)
        else:
            order[k] = {v}


def line_to_nums(line: str) -> list:
    return [int(i) for i in line.split(",")]


def is_not_valid_line(nums: list) -> tuple:
    for ind, num in enumerate(nums):
        for next_ind, next_num in enumerate(nums[ind+1:], ind+1):
            if next_num not in order:
                continue
            if num in order[next_num]:
                return (ind, next_ind)
    return ()


def rearrange_line(nums: list, ind: int, next_ind: int) -> list:
    nums[ind], nums[next_ind] = nums[next_ind], nums[ind]
    return nums


with open(FILE_NAME) as file:
    for line in file:
        if line == '\n':
            is_order = False
            continue
        if is_order:
            order_lines.append(line.strip())
        else:
            update_lines.append(line.strip())

populate_order_map(order_lines)
res = 0
for line in update_lines:
    li = line_to_nums(line)
    if not is_not_valid_line(li):
        continue
    while is_not_valid_line(li):
        ind, next_ind = is_not_valid_line(li)
        li = rearrange_line(li, ind, next_ind)
    res += li[len(li)//2]
print(res)