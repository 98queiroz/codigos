#https://doc.python.org/3.0/library/datetime.html
from datetime import datetime, timedelta
from sqlite3 import DatabaseError


#strptmie(str, fmt)
#.strftime(fmt)
#timestamp
#fromtimestamp()

d1 = datetime.strptime('20/04/1987 20:00:00', '%d/%m/%Y %H:%M:%S')
d2 = datetime.strptime('25/04/1987 22:33:00', '%d/%m/%Y %H:%M:%S')

print(d1.time())





#data = datetime.fromtimestamp(1660017600.0)
#print(data)

#data = datetime.strptime('09/8/2022', '%d/%m/%Y')
# print(data.timestamp())
#data = datetime(2022, 8, 20, 10, 53, 20)
#data = datetime(2022, 8, 20, 10, 53, 20)
#print(data.strftime('%d/%m/%y 5H:%M:%S'))

