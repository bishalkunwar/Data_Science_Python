import datetime

print('The Date and Time Today is  :', datetime.datetime.today())


date_today = datetime.date.today()
print(date_today)
print('This Year   :', date_today.year)
print('This Month    :', date_today.month)
print('Month Name:',date_today.strftime('%B'))
print('This Week Day    :', date_today.day)
print('Week Day Name:',date_today.strftime('%A'))

#Output:

'''The Date and Time Today is  : 2021-04-06 00:26:22.410714
2021-04-06
This Year   : 2021
This Month    : 4
Month Name: April
This Week Day    : 6
Week Day Name: Tuesday'''