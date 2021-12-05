file = open("puzzle_input.txt", "r")
power_ratings = [line.rstrip('\n') for line in file]
rating_length = len(power_ratings[0])
    
def digits_by_position(power_ratings, position):
    return [rating[position] for rating in power_ratings]

def digit_count_by_position(power_ratings, position, digit):
    return digits_by_position(power_ratings, position).count(digit)
    
def get_least_common_digit(power_ratings, position):
    return min(lst := digits_by_position(power_ratings, position), key=lst.count)

def get_most_common_digit(power_ratings, position):
    return max(lst := digits_by_position(power_ratings, position), key=lst.count)

def epsilon_rate(power_ratings):
    epsilon_rate_bin_str = ''.join([get_least_common_digit(power_ratings, i) for i in range(rating_length)])
    return int(epsilon_rate_bin_str, 2)
    
def gamma_rate(power_ratings):
    gamma_rate_bin_str = ''.join([get_most_common_digit(power_ratings, i) for i in range(rating_length)])
    return int(gamma_rate_bin_str, 2)

def oxygen_scrubber_rating(power_ratings):
    filtered_ratings = power_ratings
    for i in range(rating_length):
        most_common_digit = get_most_common_digit(filtered_ratings, i)
        occurrence_count = digit_count_by_position(filtered_ratings, i, most_common_digit)
        most_common_digit = most_common_digit if occurrence_count > len(filtered_ratings) / 2 else '1'
        filtered_ratings = [rating for rating in filtered_ratings if rating[i] == most_common_digit]
        if len(filtered_ratings) == 1:
            break
    return int(filtered_ratings[0], 2)

def co2_scrubber_rating(power_ratings):
    filtered_ratings = power_ratings
    for i in range(rating_length):
        least_common_digit = get_least_common_digit(filtered_ratings, i)
        occurrence_count = digit_count_by_position(filtered_ratings, i, least_common_digit)
        least_common_digit = least_common_digit if occurrence_count < len(filtered_ratings) / 2 else '0'
        filtered_ratings = [rating for rating in filtered_ratings if rating[i] == least_common_digit]
        if len(filtered_ratings) == 1:
            break
    return int(filtered_ratings[0], 2)

def power_consumption(power_ratings):
    return gamma_rate(power_ratings) * epsilon_rate(power_ratings)

def life_support_rating(power_ratings):
    return oxygen_scrubber_rating(power_ratings) * co2_scrubber_rating(power_ratings)

# PART ONE
print(power_consumption(power_ratings)) # 3277364

# PART TWO
print(life_support_rating(power_ratings)) # 5736383

