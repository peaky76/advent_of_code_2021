from collections import defaultdict
import copy
import time

file = open("example_input.txt", "r")
lines = [line.rstrip('\n') for line in file]

# READ IN
exits = defaultdict(list)
for pair in [line.split('-') for line in lines]:
    exits[pair[0]].append(pair[1])
    exits[pair[1]].append(pair[0])
            
class Path:
    
    def __init__(self, steps = [], allow_double_visits = False):
        self.steps = steps
        self.allow_double_visits = allow_double_visits
        
    def __str__(self):
        return ','.join([str(x) for x in self.steps])

    @property
    def is_blocked(self):
        return len(self.next_steps) == 0        
    
    @property
    def is_complete(self):
        return len(self.steps) > 0 and self.steps[-1] == 'end'    
    
    @property
    def next_steps(self):
        if self.steps == []:
            return ['start']
        return [cave for cave in exits[self.steps[-1]] if cave not in self.non_returnable_caves]
    
    @property
    def non_returnable_caves(self):
        if not self.allow_double_visits or self.has_double_visited:
            return self.visited_small_caves
        else:
            return ['start']
                             
    @property
    def visited_small_caves(self):
        return [cave for cave in self.steps if cave.lower() == cave]    
    
    @property
    def has_double_visited(self):
        return any([self.visited_small_caves.count(cave) == 2 for cave in self.visited_small_caves])
        

def get_paths(allow_double_visits):    
    paths = [Path(allow_double_visits = allow_double_visits)]
    complete_paths = []

    while any([path.is_complete == False for path in paths]):
        new_paths = []
        for path in paths:
            if not path.is_blocked:
                for step in path.next_steps[1:]:
                    new_path = copy.deepcopy(path)
                    new_path.steps.append(step)
                    new_paths.append(new_path)
                path.steps.append(path.next_steps[0])
                new_paths.append(path)
        complete_paths += [path for path in new_paths if path.is_complete]
        paths = [path for path in new_paths if not path.is_complete]
        
    return complete_paths
    
bef = time.perf_counter()

# PART ONE
# print(len(get_paths(False)))

# PART TWO
print(len(get_paths(True)))

aft = time.perf_counter()
print(aft - bef)
