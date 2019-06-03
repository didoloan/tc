import datetime
import random
import psycopg2 as pg
import psycopg2.extras

REQ_NUM = 2

conn = pg.connect(host='127.0.0.1', port='5432', user='postgres', password='Fucking10', dbname='toll')
cur = conn.cursor()

monthdays = {30:[9, 4, 6, 11], 28:[2,], 31: [1, 3, 5, 7, 8, 10, 12]}
unavailable = {}
tollcollectors = {}

acceptable = {1:[1,'OFF'],2:[1,2,'OFF'],3:[2,3]}

def is_leap(month):
    if(year%4==0 and year%100!=0 or year%400==0):
        return True
    else:
        return False

def get_all():
    cur.execute('select tc_id, array_agg(shift) from toll_collectors left join toll_shifts on toll_collectors.tc_id = toll_shifts.tollcollector group by tc_id;')
    alls = cur.fetchall()
    for e in alls:
        if(e[1]==[None]):
            tollcollectors[e[0]] = []
        else:
            tollcollectors[e[0]] = e[1]

def get_days(month):
    if(month==2 and is_leap(month)):
        return 29
    else:
        for key, values in monthdays.items():
            if month in values:
                return key

def getAvailable(shift, day):
    available = []
    for key, values in tollcollectors.items():
        if (len(values)==0):
            available.append(key)
        elif (len(values)==5):
            
        else:
            if (len(values)<5 and values[len(values)-1] in acceptable[shift]):
                available.append(key)
    
    return available

def populate_shift(date, shift, reqNum):
    availableTCs = getAvailable(shift)
    random.shuffle(availableTCs)
    tba = availableTCs[0:reqNum]
    for ava in tba:
        tollcollectors[ava].append(shift)
    print(tba)
    #print(tollcollectors)
    
def populate_month(month):
    
    month_shift = {}
    for day in range(get_days(month)):
        for shift in range(1,4):
            print(f'day {day} shift {shift}', end='')
            populate_shift(day, shift, reqNum=3)
        
    

get_all()
populate_month(7)

    
        
