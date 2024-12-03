
def is_safe(line):
    """
    returns 1 if line is safe, 0 otherwise
    :param line:
    :return:
    """
    descending = line[0] > line[-1]
    for i in range(len(line) - 1):
        difference = line[i] - line[i + 1]
        if descending:
            if not(0 < difference <= 3):
                return 0
        else:
            if not(0 > difference >= -3):
                return 0
    return 1


with open('input', 'r') as file:
    lines = [[int(j) for j in i.split()] for i in file]
    c = 0
    for i in lines:
        c += is_safe(i)
    print(c)