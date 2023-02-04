# Import Things
import datetime
import time

# This code will create a method for tracking the time of your process execution
print(time.time())

# create a function that measure run time
def calcProd():
    # Calculate the product of the first 100,000 numbers
    product = 1
    for i in range(1,100000):
        product = product * i
    return product

startTime = time.time()
prod = calcProd()
endTime = time.time()
print('The result is %s digits long. '% (len(str(prod))))
print('Took %s seconds to calculate.' % (endTime - startTime))

print(time.ctime())
thisMoment = time.time()
time.ctime(thisMoment)
print(thisMoment)
print(time.ctime(thisMoment))

# The following code here is for Datetime
print(datetime.datetime.now())
init_time = datetime.datetime.now()
dt = datetime.datetime(2019,10,21,16,29,0)
print(dt.year, dt.month, dt.day)
print(dt.hour, dt.minute, dt.second)
print(init_time.year, init_time.month, init_time.day)
print(init_time.hour, init_time.minute, init_time.second)

# Calculating Time Deltas
delta = datetime.timedelta(days=11, hours=10, minutes=9,seconds=8)
print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())

str(delta)

# Create a Timedelta for one day. 
today = datetime.datetime.now()
one_day = datetime.timedelta(days=1)
yesterday = today - one_day
print(today)
print(yesterday)

