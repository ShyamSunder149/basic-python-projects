import calendar

year = int(input('enter year:'))
month = int(input('enter month:'))

print(calendar.prmonth(year,month,w=1,l=0))
