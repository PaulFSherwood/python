import time

n = 2949846230
x = 1
print("x: %s||n: %s" % (x, n))
time.sleep(1)

while (n):
    if (n % 2 == 0):
        n = n / 2
        x = x + 1
        print("x: %s||n: %s" % (x, n))
        time.sleep(.2)
    else:
        n = (3*n) + 1
        x = x + 1
        print("x: %s||n: %s" % (x, n))
        time.sleep(.2)
    if (n == 1):
        print("run completed")
        break
