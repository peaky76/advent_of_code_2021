from collections import Counter

file = open("puzzle_input.txt", "r")
lines = [line.rstrip('\n') for line in file]
crabs = [int(x) for x in lines[0].split(',')]
crab_count = Counter(crabs)

def get_delta_flat_rate(target):
    return sum([v * abs(target - k) for k, v in crab_count.items()])

def get_delta_incremental(target):
    return sum([v * sum([i for i in range(1, abs(target - k) + 1)]) for k, v in crab_count.items()])

test_target = (min(crabs) + max(crabs)) // 2
curr_value = get_delta_incremental(test_target)
    
while True:
    lower_value = get_delta_incremental(test_target - 1)
    if lower_value < curr_value:
        curr_value = lower_value
        test_target -= 1
    else:
        break 

while True:
    upper_value = get_delta_incremental(test_target + 1)
    if upper_value < curr_value:
        curr_value = upper_value
        test_target += 1
    else:
        break               

print(test_target)
print(curr_value)

# PART ONE 343605
# PART TWO 96744904