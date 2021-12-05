from collections import Counter

class Vent:
    
    def __init__(self, start_coords, end_coords):
        self.start_coords = start_coords
        self.end_coords = end_coords

    @classmethod
    def from_input(cls, input):
        raw_start, raw_end = input.split(' -> ')
        return cls([int(i) for i in raw_start.split(',')], [int(i) for i in raw_end.split(',')])
    
    @property
    def is_horizontal(self):
        return self.start_coords[0] == self.end_coords[0] or self.start_coords[1] == self.end_coords[1]
    
    @property
    def squares_covered(self):
       x_range = [i for i in range(self.start_coords[0], self.end_coords[0] + self._get_step(0), self._get_step(0))]
       y_range = [i for i in range(self.start_coords[1], self.end_coords[1] + self._get_step(1), self._get_step(1))]
       x_range = x_range if len(x_range) > 1 else [x_range[0]] * len(y_range)
       y_range = y_range if len(y_range) > 1 else [y_range[0]] * len(x_range)
       return list(zip(x_range, y_range)) 
   
    def _get_step(self, index):
       return 1 if self.start_coords[index] <= self.end_coords[index] else -1
    
class Seafloor:
    
    def __init__(self, vents):
        self.vents = vents
        
    def vent_coverage(self, horizontal_only = False):
        return [square for vent in vents for square in vent.squares_covered if horizontal_only == False or vent.is_horizontal]

    def dangerous_areas(self, horizontal_only = False):
        return [key for key, value in Counter(self.vent_coverage(horizontal_only)).items() if value >= 2]
        
                    
file = open("puzzle_input.txt", "r")
vents = [Vent.from_input(line.rstrip('\n')) for line in file]
seafloor = Seafloor(vents)

# PART ONE
print(len(seafloor.dangerous_areas(True)))

# PART TWO
print(len(seafloor.dangerous_areas()))
