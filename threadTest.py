import threading, time

def run(n, name, startTime):
    while n > 0:
        stopTime = (time.time() / 60)
        difTime = stopTime - startTime
        n -= 1
        print("Thread:%s||Count:%s:||StartTime:%s||StopTime:%s||DifTime:%s" % (name, n, startTime, stopTime, difTime,))
        time.sleep(.01) 

count = 100
try:
    t1startTime = (time.time() / 60)
    t1 = threading.Thread(target=run, args=(count, "t1", t1startTime))
    t1.start()

    t2startTime = (time.time() / 60)
    t2 = threading.Thread(target=run, args=(count, "t2", t2startTime))
    t2.start()
    
    t1.join(); t2.join()
except KeyboardInterrupt:
    # this should exit on ctrl-c
    print("exiting")
