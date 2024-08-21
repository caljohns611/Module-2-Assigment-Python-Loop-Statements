#question 2 task 1

import random

moods_for_the_day = ["Happy", "Sad", "tired"]
time_of_day = ["Morning", "Afternoon", "evening"]
over_the_week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for moods in moods_for_the_day:
    random.shuffle(moods_for_the_day)

    for i in range(3):
        days = over_the_week[i]
        for m in range(3):
            time = time_of_day[m]

            print(f"On this {days} {time} you were {moods}.")