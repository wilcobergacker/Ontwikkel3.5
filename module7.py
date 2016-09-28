
import datetime

currentDate = datetime.date.today()

print(currentDate)
print(currentDate.year)
print(currentDate.month)
print(currentDate.day)

test=(currentDate.strftime('%d %b, %Y'))

print(test)
print("dit is de datum")

print(currentDate.strftime('Please attend our event %A, %B %d in the year %Y'))