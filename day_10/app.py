from collections import Counter
from statistics import median

ILLEGALS = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

COMPLETIONS = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

BRACKET_PAIRS = ['()','[]','{}','<>']

def sweep(line):
    for pair in BRACKET_PAIRS:
        line = line.replace(pair, '')
    return line

def multi_sweep(line):
    orig_line = line
    while True:
        line = sweep(line)
        if line == orig_line:
            break
        orig_line = line
    return line

def is_corrupt(multi_swept_line):
    return any([x[1] in multi_swept_line for x in BRACKET_PAIRS])

def corrupting_char(corrupt_multi_swept_line):
    return [char for char in corrupt_multi_swept_line if char in [y[1] for y in BRACKET_PAIRS]][0]

def get_line_completion(incomplete_line):
    brackets = ''.join([pair[1] for bracket in incomplete_line[::-1] for pair in BRACKET_PAIRS if bracket == pair[0]])
    return brackets

def completion_score(completion):
    score = 0
    for bracket in completion:
        score *= 5
        score += COMPLETIONS[bracket]
    return score

file = open("puzzle_input.txt", "r")
lines = [line.rstrip('\n') for line in file]

# SWEEP AND CLEAN
lines = [multi_sweep(line) for line in lines]

# PART ONE
corrupting_char_count = Counter([corrupting_char(line) for line in lines if is_corrupt(line)])
score = sum([ILLEGALS[k] * v for k, v in corrupting_char_count.items()])
print(score) # 26397 / 344193

# PART TWO
incomplete_lines = [line for line in lines if not is_corrupt(line)]
completions = [get_line_completion(line) for line in incomplete_lines]
scores = [completion_score(completion) for completion in completions]
print(median(scores)) # 288957 / 3241238967
