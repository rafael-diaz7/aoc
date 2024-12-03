import re

with open('input', 'r') as file:
    lines = file.readlines()

c = 0
for i in lines:
    matches = re.findall(r'mul\(\d+,\d+\)', i)
    for j in matches:
        nums = re.search(r'\d+,\d+', j).group().split(",")
        c += int(nums[0]) * int(nums[1])

print(c)