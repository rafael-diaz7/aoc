file_name = "input"


def is_valid_equation(nums, total):
    def recurse(running_total, index, total):
        if running_total > total:
            return False
        if index == len(nums):
            if running_total == total:
                return True
            return False

        return (recurse(running_total + nums[index], index + 1, total) or
                recurse(running_total * nums[index], index + 1, total))

    return recurse(nums[0], 1, total)


with open(file_name) as file:
    lines = file.readlines()

res = 0
for line in lines:
    line_info = line.strip().split(":")
    total = int(line_info[0])
    num_list = [int(i) for i in line_info[1].split(" ")[1:]]
    if is_valid_equation(num_list, total):
        res += total
print(res)
