import sys
import os
import time
import urllib.request
from wmi import WMI

apiWRITEkey = "8LZ465OQZBEWV84I"
apiREADkey = "4SWW24NWH9N58M4"

def sendReq(apiWRITEkey, val=1):
    #address setup
    currentAddress = "https://api.thingspeak.com/update?api_key=8LZ465OQZBEWV84I&field1=" + format(str(val))
    #                 https://api.thingspeak.com/update?api_key=      YOUR_CHANNEL_API_KEY     &field1=               99
    urllib.request.urlopen(currentAddress)
    pass

def memory():
    import os
    from wmi import WMI
    w = WMI('.')
    result = w.query("SELECT WorkingSet FROM Win32_PerfRawData_PerfProc_Process WHERE IDProcess=%d" % os.getpid())
    return int(result[0].WorkingSet)

print(memory())

x = 10

while(x > 1):
    number = memory()
    sendReq(number)
    print("Number %s is: %s" % (x, number))
    time.sleep(60)
    x = x - 1
