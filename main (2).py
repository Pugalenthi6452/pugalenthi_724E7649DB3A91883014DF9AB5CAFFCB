# 1.1 Implement a recursive function to calculate the factorial of a given number.






""
def isLeapYear(year):
  if (year % 4 == 0 and year % 100 != 0) or year % 400==0:
    return True
  else:
    return False

year = int(input("Enter a year :2024 "))

if isLeapYear (year):
  print('{} is a leap year.'.format(year))
else:
  print('{} is not a leap year. '.format(year))