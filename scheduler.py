import datetime
import random
from sqlalchemy as sqla

db = sqla.create_engine('postgres://postgres:Fucking10@localhost:5432/toll')
connection = engine.connect()
metadata = db.MetaData()
tollCollectors = db.Table('tollcollectors', metadata, autoload=True, autoload_with=engine)


monthdays = {30:[9, 4, 6, 11], 28:[2,], 31: [1, 3, 5, 7, 8, 10, 12]}
tollcollectors = {1:[1,2,2], 2:[2,2,3], 3:[1], 4:[3], 5:[2]}

acceptable = {1:[1,'OFF'],2:[1,2,'OFF'],3:[2,3]}

def is_leap(month):
    if(year%4==0 and year%100!=0 or year%400==0):
        return True
    else:
        return False

def get_days(month):
    if(month==2 and is_leap(month)):
        return 29
    else:
        for key, values in monthdays.items():
            if month in values:
                return key
def get_all():
    

def getAvailable(shift):
    available = []
    for key, values in tollcollectors.items():
        if (len(values)<5 and values[len(values)-1] in acceptable[shift]):
            available.append(key)
    return available


def populate_shift(date, shift, reqNum):
    availableTCs = getAvailable(shift)
    random.shuffle(availableTCs)
    tba = availableTCs[0:reqNum]
    
    
def populate_month(month):
    
    month_shift = {}
    for day in get_days(month):
        for shift in range(3):
            populate_shift(day, shift, reqNum=5)
        
    

#print(getAvailable(2))
    
        
