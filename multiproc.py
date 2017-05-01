from multiprocessing import Process
import time
import sys

rocket = 0
ticks = 0.00
addTime = 2.09 * (2.09 * 1024)
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
    global ticks
    global addTime
    print('Start addTime:%.2f||Ticks:%.2f' % (addTime, ticks))
    while ticks < addTime:
        ticks += .01
    print('Start addTime:%.2f||Ticks:%.2f' % (addTime, ticks))

if __name__=='__main__':
     p1 = Process(target = func1)
     p1.start()
     p2 = Process(target = func2)
     p2.start()
