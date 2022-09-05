import sys

# showing all the locations where the interpreter might look for modules
locations = sys.path
print(locations)
for i in locations:
    print(i)


# press "ctrl" or "cmd" key and hover over module name/click on it to get more info
import calendar

# check for leapdays
leapdays = calendar.leapdays(2000,2022)
print(leapdays)

# check if a year is a leap year
is_leap_year = calendar.isleap(2036)
print(is_leap_year)
