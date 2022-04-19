def name_of_oldest(names, ages):
    max_ages = max(ages)
    oldest_ages_pos = ages.index(max_ages)
    return names[oldest_ages_pos]

names=["Bill", "Jane", "Sven"]
ages = [21, 34, 56]

print(name_of_oldest(names, ages))

