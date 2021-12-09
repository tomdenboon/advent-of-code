fishes_created = {}


def calculate_fishes(breed_time, days):
    fish = 1
    next_fish = breed_time
    save_days = days
    if (breed_time, days) in fishes_created:
        return fishes_created[(breed_time, days)]
    while(days - next_fish >= 0):
        days -= next_fish
        fish += calculate_fishes(8 + 1, days)
        next_fish = 6 + 1
    fishes_created[(breed_time, save_days)] = fish
    return fish


days = [0] * 256
file = open('input')
line = file.readline()
fishes = [int(x) for x in line.split(',')]
total_fish = 0
for fish in fishes:
    days[fish]
    total_fish += calculate_fishes(fish+1, 256)
print(total_fish)
