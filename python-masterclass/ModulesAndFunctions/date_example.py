import datetime
import locale

locale.setlocale(locale.LC_ALL, 'fr_FR.utf-8')

start = datetime.date(2022, 2, 4)
print(start)

# pretty_start = start.strftime('%A %d %B, %Y')
pretty_start = start.strftime('%a %d %b, %y')
print(pretty_start)

year = start.year
month = start.month
day = start.day

print(f'The {year} winter olympics started on day {day} of month {month}')

today = datetime.date.today()
print(f'Today\'s date: {today}')
print(f'Today is {today.strftime('%A')}')
print(f'Today is day {today.weekday()} of the week')
