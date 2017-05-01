import thread
import time
import random

def runOften(threadName, sleepTime):
    while 1 < 2:
        time.sleep(sleepTime)
        print("%s" % (threadName))

def runLessOften(threadName, sleepTime):
    while 1 < 2:
        time.sleep(sleepTime)
        print("%s" % (threadName))

def runRandomly(threadName, sleepTime):
    while 1 < 2:
        time.sleep(sleepTime)
        print("%s" % (threadName))

try:
    thread.start_new_thread(runOften, ("Runs Often", 2))
    thread.start_new_thread(runLessOften, ("Runs Less Often", 2))
    thread.start_new_thread(runRandomly, ("Runs Random and Often", random.random()))
except Exception, e:
    print str(e)
