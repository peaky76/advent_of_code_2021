import math

class Cave:
    
    def __init__(self, lines):
        self.locations = {
            (i, j): int(item) for i, line in enumerate(lines) for j, item in enumerate(list(line))
        }
        self.far_x = len(lines) - 1
        self.far_y = len(list(lines[0])) - 1

    @property
    def basins(self):
        basins = []
        for low in self.low_points:
            new_basin = []
            additions = [low]
            while additions:
                next_additions = []
                for add in additions:
                    new_additions = [loc for loc in self.get_adjacents(add[0], add[1]) if loc not in self.peaks and loc not in new_basin]
                    next_additions += new_additions
                new_basin += additions
                additions = set(next_additions)
            basins.append(new_basin)
        return sorted(basins, key=len, reverse=True)
    
    @property
    def largest_basins_product(self):
        return math.prod([len(x) for x in self.basins[0:3]])
        
    @property
    def low_points(self):
        return [loc for loc in self.locations if all([self.locations[v] > self.locations[loc] for v in self.get_adjacents(loc[0], loc[1])])]
    
    @property
    def peaks(self):
        return [loc for loc in self.locations if self.locations[loc] == 9]        
        
    @property
    def risk_level(self):
        return sum([self.locations[loc] + 1 for loc in self.low_points])
                        
    def get_adjacents(self, x, y):
        left = (x - 1, y) if x > 0 else None
        right = (x + 1, y) if x < self.far_x else None
        fore = (x, y + 1) if y < self.far_y else None
        aft = (x, y - 1) if y > 0 else None
        return [item for item in [left, right, fore, aft] if not item is None]
    
        
file = open("puzzle_input.txt", "r")
lines = [str(line.rstrip('\n')) for line in file]
cave = Cave(lines)

# PART ONE
print(cave.risk_level) # 15 / 516

# PART TWO
print(cave.largest_basins_product) # 1134 / 1023660