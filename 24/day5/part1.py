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


def is_valid_line(nums: list) -> bool:
    for ind, num in enumerate(nums):
        for next_num in nums[ind+1:]:
            if next_num not in order:
                continue
            if num in order[next_num]:
                return False
    return True


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
    if is_valid_line(li):
        res += li[len(li)//2]

print(res)