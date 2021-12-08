SEVEN_SEGMENT_DISPLAYS = {
    0: 'abcefg',
    1: 'cf',
    2: 'acdeg',
    3: 'acdfg',
    4: 'bcdf',
    5: 'abdfg',
    6: 'abdefg',
    7: 'acf',
    8: 'abcdefg',
    9: 'abcdfg'
}

PATTERNS = SEVEN_SEGMENT_DISPLAYS.values()
UNIQUE_LENGTHS = [len(v) for v in PATTERNS if [len(x) for x in PATTERNS].count(len(v)) == 1] 

def get_segment_occurrences_by_pattern_length(patterns):
    segment_occurrence_dict = {}
    for letter in list('abcdefg'):
        segment_occurrence_dict[letter] = []
        for p in patterns:
            if letter in list(p):
                segment_occurrence_dict[letter] += str(len(p))
    for k, v in segment_occurrence_dict.items():
        segment_occurrence_dict[k] = ''.join(sorted(v))
    return segment_occurrence_dict

def get_decoder(patterns):
    decoder_dict = {}
    for ak, av in get_segment_occurrences_by_pattern_length(patterns).items():
        for bk, bv in get_segment_occurrences_by_pattern_length(PATTERNS).items():
            if av == bv:
                decoder_dict[ak] = bk
    return decoder_dict

def decode(code, decoder):
    translation = ''.join(sorted([decoder[letter] for letter in code]))
    for k, v in SEVEN_SEGMENT_DISPLAYS.items():
        if v == translation:
            return str(k)

class Note:
    
    def __init__(self, line):
        self.patterns, self.readings = [section.split(' ') for section in line.split(' | ')]

    @property
    def decoder(self):
        return get_decoder(self.patterns)    

    @property
    def output(self):
        return int(''.join([decode(reading, self.decoder) for reading in self.readings]))
        
# READ IN
file = open("puzzle_input.txt", "r")
notes = [Note(line.rstrip('\n')) for line in file]

# PART ONE
outputs = [output for note in notes for output in note.readings]
result = len([len(x) for x in outputs if len(x) in UNIQUE_LENGTHS])
print(result) # 255 

# PART TWO
print(sum([note.output for note in notes])) # 982158