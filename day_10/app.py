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
    
class Line:

    def __init__(self, line):
        self.line = line
    
    @property
    def swept(self):
        line = self.line
        orig_line = self.line
        while True:
            for pair in BRACKET_PAIRS: 
                line = line.replace(pair, '')
            if line == orig_line:
                break
            orig_line = line              
        return line

    @property
    def is_corrupt(self):
        return any([x[1] in self.swept for x in BRACKET_PAIRS])

    @property
    def is_incomplete(self):
        return not self.is_corrupt and not self.swept == ''
        
    @property
    def corrupting_char(self):
        return None if not self.is_corrupt else [char for char in self.swept if char in [y[1] for y in BRACKET_PAIRS]][0]

    @property
    def completion(self):
        return [] if not self.is_incomplete else ''.join([pair[1] for bracket in self.swept[::-1] for pair in BRACKET_PAIRS if bracket == pair[0]])
    
    @property
    def completion_score(self):
        score = 0 
        for bracket in self.completion:
            score *= 5
            score += COMPLETIONS[bracket]
        return score
        

file = open("puzzle_input.txt", "r")
lines = [Line(line.rstrip('\n')) for line in file]

# PART ONE
corrupting_char_count = Counter([line.corrupting_char for line in lines if line.is_corrupt])
score = sum([ILLEGALS[k] * v for k, v in corrupting_char_count.items()])
print(score) # 26397 / 344193

# PART TWO
scores = [line.completion_score for line in lines if line.completion_score > 0]
print(median(scores)) # 288957 / 3241238967