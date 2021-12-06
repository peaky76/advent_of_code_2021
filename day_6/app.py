from collections import Counter

fish = [int(item) - 8 for line in open("puzzle_input.txt", "r") for item in line.split(',')]

def get_count(initial_fish, num_of_days):
    count_dict = Counter(initial_fish)
    for day_in_cycle in range(-8, num_of_days + 1):
        for spawning_day in range(day_in_cycle + 9, num_of_days + 1, 7):
            count_dict[spawning_day] += count_dict[day_in_cycle]
    return sum(count_dict.values())

print(get_count(fish, 80)) # PART ONE
print(get_count(fish, 256)) # PART TWO