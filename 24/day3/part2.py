import re

with open('input', 'r') as file:
    lines = file.readlines()


def calculate_product_from_match(match):
    nums = re.search(r'\d+,\d+', match).group().split(",")
    return int(nums[0]) * int(nums[1])

c = 0
for i in lines:
    first_match = re.findall(r'.+?(?=don\'t\(\))', i)[0]
    other_matches = re.findall(r'(?<=do\(\))(.+?)(?=don\'t\(\)|$)', i)

    valid_segments = [first_match] + other_matches
    for segment in valid_segments:
        for match in re.findall(r'mul\(\d+,\d+\)', segment):
            c += calculate_product_from_match(match)
print(c)