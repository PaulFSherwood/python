import time

segments =  (11,4,23,8,7,10,18,25)
digits = (22,27,17,24)
num = {' ':(0,0,0,0,0,0,0),
    '0':(1,1,1,1,1,1,0),
    '1':(0,1,1,0,0,0,0),
    '2':(1,1,0,1,1,0,1),
    '3':(1,1,1,1,0,0,1),
    '4':(0,1,1,0,0,1,1),
    '5':(1,0,1,1,0,1,1),
    '6':(1,0,1,1,1,1,1),
    '7':(1,1,1,0,0,0,0),
    '8':(1,1,1,1,1,1,1),
    '9':(1,1,1,1,0,1,1)}



while True:
    n = time.ctime()[11:13]+time.ctime()[14:16]
    s = str(n).rjust(4)
    for digit in range(4):
        for loop in range(0,7):
            print("State: %s || GPIO: %s || array#: %s" % (num[s[digit]][loop], segments[loop], loop))
            time.sleep(0.001)
        print("==================== %s" % (n))
        print("GPIO.ouput(%s,0)" % (digits[digit]))
        time.sleep(1)

