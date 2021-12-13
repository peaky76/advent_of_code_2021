import time

file = open("example_input.txt", "r")
lines = [line.rstrip('\n') for line in file]
coords = []
folds = []

for line in lines:
    if ',' in line:
        coords.append(line.split(','))
    if '=' in line:
        folds.append(line.replace('fold along ','').split('='))
        
# print(coords)
# print(folds)

def limit(coords, direction):
    index = 0 if direction == 'x' else 1
    return max([int(coord[index]) for coord in coords])
    
def pretty_print(coords):
    for j in range(limit(coords, 'y') + 1):
        for i in range(limit(coords, 'x') + 1):
            if [str(i), str(j)] in coords:
                print('#', end='')
            else:
                print('.', end='')
        print('\n')
        
def cut(coords, direction, dotted_line):
    index = 0 if direction == 'x' else 1
    pre = [coord for coord in coords if int(coord[index]) < dotted_line]
    if direction == 'x':
        post = [[str(int(coord[0]) - dotted_line - 1), coord[1]] for coord in coords if int(coord[index]) >= dotted_line]
    else:
        post = [[coord[0], str(int(coord[1]) - dotted_line - 1)] for coord in coords if int(coord[index]) >= dotted_line]
    return [pre, post]

def flip(coords, direction):
    if direction == 'x':
        return [[str(limit(coords, 'x') - int(coord[0])), coord[1]] for coord in coords]
    else:
        return [[coord[0], str(limit(coords, 'y') - int(coord[1]))] for coord in coords]
    
def merge(coords_1, coords_2):
    return [list(s) for s in set([tuple(l) for l in coords_1 + coords_2])]
        
# PART ONE
before_fold, after_fold = cut(coords, folds[0][0], int(folds[0][1]))
folded = merge(before_fold, flip(after_fold, folds[0][0]))
print(len(folded))

# PART TWO
for fold in folds:
    direction = fold[0]
    line = int(fold[1])
    before_fold, after_fold = cut(coords, direction, line)
    coords = merge(before_fold, flip(after_fold, direction))
    
pretty_print(coords)