from multiprocessing import Process
import time
import sys

rocket = 0
addTime = 2.09
addTime = 8.36 * (addTime * .01)
curTime = 0

def getTime():
    return time.time() * 1000

def func1():
    global rocket
    global addTime
    global curTime
    curTime = getTime()
    print('Start Time1:%.2f' % (curTime))
    while curTime + addTime > getTime() :
        rocket += 1
    curTime = getTime()
    print('end func1:%.2f' % (curTime))

def func2():
    global rocket
    global curTime
    print('Start Time2:%.2f' % (curTime))
    while rocket < 5656789:
        rocket += 1
    curTime = getTime()
    print('end func2:%.2f' % (curTime))

if __name__=='__main__':
     p1 = Process(target = func1)
     p1.start()
     p2 = Process(target = func2)
     p2.start()
