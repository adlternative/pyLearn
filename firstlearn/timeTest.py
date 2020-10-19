from datetime import timedelta
from datetime import datetime

a = timedelta(days=2, hours=6)
n = timedelta(hours=18.5)
# print((a+n).days)
print((a + n))

b = datetime(2012, 3, 3)
c = b + timedelta(days=10)
print(c)
now = datetime.today()
print(now)

from dateutil.relativedelta import relativedelta

now += relativedelta(months=1)
print(now)

d = relativedelta(now, b)
print(d)

from datetime import datetime, timedelta

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_date=None):
    if start_date is None:
        start_date = datetime.today()
        day_num = start_date.weekday()
        day_num_target = weekdays.index(dayname)
        days_ago = (7 + day_num - day_num_target) % 7
        if days_ago == 0:
            days_ago = 7
        target_date = start_date - timedelta(days=days_ago)
        return target_date


print(get_previous_byday('Friday'))

from datetime import datetime, date, timedelta
import calendar


def get_month_range(start_date=None):
    if start_date is None:
        start_date = date.today().replace(day=1)

    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days=days_in_month)
    return (start_date, end_date)


a_day = timedelta(days=1)
first_day, last_day = get_month_range()
while first_day < last_day:
    print(first_day)
    first_day += a_day
    
    
from datetime import datetime
text = '2012-09-20'
y = datetime.strptime(text, '%Y-%m-%d')

z = datetime.now()
diff = z - y
print(diff)
# diff=datetime.timedelta(3, 77824, 177393)
z=datetime(2012,9,23,21,37,4,177393)
nice_z =datetime.strftime(z,"%A %B %d, %Y")
print(nice_z)