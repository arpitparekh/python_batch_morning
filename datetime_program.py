import datetime

currentTime = datetime.datetime.now()
print(currentTime)

print(currentTime.year)
print(currentTime.month)
print(currentTime.day)
print(currentTime.hour)
print(currentTime.minute)
print(currentTime.second)
print(currentTime.microsecond)

print(currentTime.strftime("%C"))  # to get any formatted date and time
