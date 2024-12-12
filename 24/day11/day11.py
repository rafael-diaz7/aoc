import itertools
import time
sample = [125, 17]
input = [77, 515, 6779622, 6, 91370, 959685, 0, 9861]


def part1_solve(data, num_iterations):
    for iteration in range(num_iterations):
        for i in range(len(data)):
            num = data[i]
            if num == 0:
                data[i] = [1]
            elif len(str(num)) % 2 == 0:
                data[i] = [int(str(num)[:len(str(num)) // 2]), int(str(num)[len(str(num)) // 2:])]
            else:
                data[i] = [num * 2024]
        data = list(itertools.chain(*data))
    return len(data)


def part2_solve(data, num_iterations):
    # i wanted to memoize in the first part but couldn't think how i'd keep track of the result at each iteration,
    # now i'm thinking i could do all the blinks on the first stone, memoize all the transformations, and continue
    # through the list using my cache
    memo = {}
    def transform(num, iterations):
        if (num, iterations) in memo:  # cache to skip compute
            return memo[(num, iterations)]
        if iterations == 0:  # base case is the stone we are evaluating
            return 1  # if no iterations left, this is one stone
        if num == 0:  # does not create a new stone (in raw count)
            end_state = transform(1, iterations - 1)
        elif len(str(num)) % 2 == 0:  # creates 2 stones
            left = int(str(num)[:len(str(num)) // 2])
            right = int(str(num)[len(str(num)) // 2:])
            end_state = transform(left, iterations - 1) + transform(right, iterations - 1)
        else:  # creates 1 stone
            end_state = transform(num * 2024, iterations - 1)
        # cache the final result and return
        memo[(num, iterations)] = end_state
        return end_state

    res = 0
    for i in range(len(data)):
        res += transform(data[i], num_iterations)
    return res
start_time = time.time()
print(part2_solve(input, 75))
print("--- %s seconds ---" % (time.time() - start_time))
# --- 0.10152626037597656 seconds ---