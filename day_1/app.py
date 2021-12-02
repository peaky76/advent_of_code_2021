file = open("puzzle_input.txt", "r")
readings = [int(line.rstrip('\n')) for line in file]

def get_increase_count(readings_list):
    # Because we are iterating over a list with the first item removed, 
    # i is equivalent to i - 1 in the full list
    return sum([1 for i, x in enumerate(readings_list[1:]) if x > readings_list[i]])

# PART ONE
print(get_increase_count(readings))

# PART TWO
windows = [sum(readings[i:i+3]) for i in range(len(readings) - 2)]
print(get_increase_count(windows))
