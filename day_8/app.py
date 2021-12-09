SEVEN_SEGMENT_DISPLAYS = {
    'abcefg': 0,
    'cf': 1,
    'acdeg': 2,
    'acdfg': 3,
    'bcdf': 4,
    'abdfg': 5,
    'abdefg': 6,
    'acf': 7,
    'abcdefg': 8,
    'abcdfg': 9 
}

PATTERNS = SEVEN_SEGMENT_DISPLAYS.keys()
UNIQUE_LENGTHS = [len(v) for v in PATTERNS if [len(x) for x in PATTERNS].count(len(v)) == 1] 

def get_pattern_lengths_by_segment(patterns):
    return {
        letter: ''.join(sorted([str(len(p)) for p in patterns if letter in list(p)])) for letter in list('abcdefg')
    }

class Decoder:
    
    def __init__(self, corrupted_patterns):
        self.input_dict = get_pattern_lengths_by_segment(corrupted_patterns)   
        
    @property    
    def decoding_dict(self):
        output_dict = {v: k  for k, v in get_pattern_lengths_by_segment(PATTERNS).items()}
        return {
            k1: v2 for k1, v1 in self.input_dict.items() for k2, v2 in output_dict.items() if v1 == k2
        }
        
    def decode(self, code):
        return SEVEN_SEGMENT_DISPLAYS[''.join(sorted([self.decoding_dict[letter] for letter in code]))]            

class Note:
    
    def __init__(self, line):
        self.patterns, self.readings = [section.split(' ') for section in line.split(' | ')]

    @property
    def output(self):
        decoder = Decoder(self.patterns)
        digits = [decoder.decode(reading) for reading in self.readings]
        return int(''.join([str(digit) for digit in digits]))

# READ IN
file = open("puzzle_input.txt", "r")
notes = [Note(line.rstrip('\n')) for line in file]

# PART ONE
readings = [reading for note in notes for reading in note.readings]
result = len([len(x) for x in readings if len(x) in UNIQUE_LENGTHS])
print(result) # 255 

# PART TWO  
print(sum([note.output for note in notes])) # 982158
