#question 1 task 1

import random

moods_for_the_week = ["Happy", "Sad", "Energetic", "Calm"]
random.shuffle(moods_for_the_week)
weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for i in range(len(weekdays)):
        days = weekdays[i]
for moods in moods_for_the_week:
    print(f"I feelt {moods} on this day {days}.")   