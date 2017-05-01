import threading, time

class MyThread(threading.Thread):
    def run(self):
        print("About to sleep")
        time.sleep(5)
        print("Finished sleeping")

m = MyThread()
m.start()

time.sleep(1)
print("Im still running")
