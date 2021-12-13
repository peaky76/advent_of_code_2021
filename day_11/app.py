
def adjacent(x, y):
    return [(i, j) for i in range(x - 1, x + 2) for j in range(y - 1, y + 2) if 0 <= i < limit and 0 <= j < limit and not (i == x and j == y)]

def pretty_print(octopodes):
    for i in range(limit):
        line = ''
        for j in range(limit):
            line += str(octopodes[(i, j)])
        print(line)
    
def step(octopodes):
    flashes = 0
    for k in octopodes.keys():
        octopodes[k] += 1
    while any([o > 9 for o in octopodes.values()]):
        change_dict = {k: 0 for k in octopodes.keys()}
        for k in octopodes.keys():
            neighbours = adjacent(k[0], k[1])
            neighbour_flashes = sum([octopodes[n] > 9 for n in neighbours])
            change_dict[k] = neighbour_flashes
        for k in octopodes.keys():
            if octopodes[k] > 9:
                octopodes[k] = -1
            elif octopodes[k] != -1:
                octopodes[k] += change_dict[k]
    for k in octopodes.keys():
        if octopodes[k] == -1:
            flashes += 1
            octopodes[k] = 0
    return [octopodes, flashes]
       

# READ IN
file = open("puzzle_input.txt", "r")
lines = [str(line.rstrip('\n')) for line in file]
rows = [[int(x) for x in list(line)] for line in lines]
      
# PART ONE
octopodes = {(i, j): cell for i, row in enumerate(rows) for j, cell in enumerate(row)}
limit = len(lines)
total_flashes = 0
for i in range(100):
    octopodes, flashes = step(octopodes)
    total_flashes += flashes
print(total_flashes) # 1656 / 1681

# PART TWO
octopodes = {(i, j): cell for i, row in enumerate(rows) for j, cell in enumerate(row)}
limit = len(lines)
step_count = 0
flashes = 0
while flashes != 100:
    step_count += 1
    octopodes, flashes = step(octopodes)
print(step_count) # 195 / 276