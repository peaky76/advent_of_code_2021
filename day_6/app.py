from collections import Counter
import time

def get_count(initial_fish, num_of_days):
    count_dict = Counter(initial_fish)

    for i in range(-8, num_of_days + 1):
        spawning_days = [x for x in range(i + 9, num_of_days + 1, 7)] 
        for day in spawning_days:
            count_dict[day] += count_dict[i]
    
    return sum(count_dict.values())
                              
file = open("puzzle_input.txt", "r")
fish = [int(item) - 8 for line in file for item in line.split(',')]

# PART ONE
bef = time.perf_counter()
print(get_count(fish, 80))    
aft = time.perf_counter()
print(aft - bef)

# PART TWO
bef = time.perf_counter()
print(get_count(fish, 256))    
aft = time.perf_counter()
print(aft - bef)