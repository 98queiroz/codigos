from datetime import datetime
from pprint import pprint

""" data1 = [3,1,4,5,7,2]

pprint(data1)
data1_sorted = sorted(data1, reverse=True)

pprint(data1_sorted) """

data2 = [
    {'name': 'product A', 'id': 29, 'dt1':'2022/01/01', 'dt2':'01/01/2022'},
    {'name': 'product C', 'id': 25, 'dt1':'2022/02/01', 'dt2':'01/02/2022'},
    {'name': 'product B', 'id': 21, 'dt1':'2022/03/01', 'dt2':'01/03/2022'},
    {'name': 'product D', 'id': 23, 'dt1':'2021/02/01', 'dt2':'01/02/2021'},
    {'name': 'product F', 'id': 22, 'dt1':'2022/20/04', 'dt2':'20/04/2022'},
    {'name': 'product E', 'id': 20, 'dt1':'1995/12/29', 'dt2':'29/12/1995'},
]

def convert_br_date_to_obj(date):
    dt = date.split('/')
    return datetime(
        int(dt[2]),
        int(dt[1]),
        int(dt[0]),
    )


def order_data(value):
    return convert_br_date_to_obj(value['dt2'])

data2.sort(key=order_data)
pprint(data2)