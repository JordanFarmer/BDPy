day_of_week = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
lengthArray = []
for day in day_of_week:
    lengthArray.append(len(day))
print(lengthArray)

print([len(day) for day in day_of_week])
print(day_of_week)

_, mon, tue, wed, thr, fri, sat = day_of_week

print(mon, wed, fri)
print(tue, thr, sat)