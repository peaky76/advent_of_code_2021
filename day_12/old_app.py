import copy
import time

class Cave:
    
    def __init__(self, cave_code):
        self.code = cave_code
        self.exits = []
        
    def __str__(self):
        return self.code
        
    @property
    def is_large(self):
        return self.code.upper() == self.code

    @property    
    def is_small(self):
        return self.code.lower() == self.code
    
    @staticmethod
    def create_connection(cave_1, cave_2):
        cave_1.exits.append(cave_2)
        cave_2.exits.append(cave_1)

class CaveNetwork:
    
    def __init__(self, caves = []):
        self.caves = caves
        
    def find_or_create(self, cave_code):
        for cave in self.caves:
            if cave.code == cave_code:
                return cave
        new_cave = Cave(cave_code)
        self.caves.append(new_cave)
        return new_cave
    
    @property
    def exits_dict(self):
        return {cave.code: [cave.code for cave in cave.exits] for cave in self.caves}
    
    @property
    def start(self):
        return self.find_or_create('start')
    
    @property
    def end(self):
        return self.find_or_create('end')
    
    def get_paths(self, allow_double_visits = False):
        paths = [Path(self.start, self.end, allow_double_visits = allow_double_visits)]
        complete_paths = []
        while any([path.is_complete == False for path in paths]):
            new_paths = []
            for path in paths:
                if not path.is_blocked:
                    for step in path.next_steps[1:]:
                        new_path = copy.deepcopy(path)
                        new_path.add(step)
                        new_paths.append(new_path)
                    path.add(path.next_steps[0])
                    new_paths.append(path)
            complete_paths += [path for path in new_paths if path.is_complete]
            paths = [path for path in new_paths if not path.is_complete]
        return complete_paths
    
class Path:
    
    def __init__(self, start, end, steps = None, allow_double_visits = False):
        self.start = start
        self.end = end
        self.steps = steps if steps else [start]
        self.allow_double_visits = allow_double_visits
    
    def __str__(self):
        return ','.join([str(x) for x in self.steps])
        
    @property    
    def next_steps(self):
        if not self.allow_double_visits or self.has_double_visited_a_small_cave:
            return [ex for ex in self.steps[-1].exits if ex.is_large or ex.code not in [s.code for s in self.steps]]    
        else:
            return [ex for ex in self.steps[-1].exits if ex.code != 'start']
    
    @property
    def double_visited_small_cave(self):
        small_caves = [step.code for step in self.steps if step.is_small]
        for cave in set(small_caves):
            small_caves.remove(cave)
        return small_caves[0] if small_caves else None
    
    @property
    def has_double_visited_a_small_cave(self):
        return not self.double_visited_small_cave is None
        
    @property
    def is_blocked(self):
        return len(self.next_steps) == 0
    
    @property
    def is_complete(self):
        return self.steps[-1].code == self.end.code
    
    def add(self, step):
        self.steps.append(step)
                                    
file = open("example_input.txt", "r")
lines = [line.rstrip('\n') for line in file]
cave_network = CaveNetwork()

# READ IN
for pair in [line.split('-') for line in lines]:
    start_cave = cave_network.find_or_create(pair[0])
    end_cave = cave_network.find_or_create(pair[1])
    Cave.create_connection(start_cave, end_cave)

bef = time.perf_counter()
    
# PART ONE    
print(len(cave_network.get_paths())) # 3421

# PART TWO
print(len(cave_network.get_paths(True))) # WORKS BUT TAKES TOO LONG

aft = time.perf_counter()
print(aft - bef)
