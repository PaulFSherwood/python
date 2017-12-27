# Simple example of reading the MCP3008 analog input channels and printing
# them all out.
# from flightgear hosted website
# throttle
# http://10.0.12.142:5500/props/controls/engines/engine[0]?submit=set&throttle[0]=0.0

import time
import urllib2
import itertools
import sys

# Import SPI library (for hardware SPI) and MCP3008 library.
import Adafruit_GPIO.SPI as SPI
import Adafruit_MCP3008

ipAddress = 'http://192.168.1.6:5500'
ipAddress2 = 'http://10.0.12.142:5500'

# Software SPI configuration:
CLK  = 11 # GPIO18 pin 12
MISO =  9 # GPIO23 pin 16
MOSI = 10 # GPIO24 pin 18
CS   =  8 # GPIO25 pin 22
mcp = Adafruit_MCP3008.MCP3008(clk=CLK, cs=CS, miso=MISO, mosi=MOSI)

# Hardware SPI configuration:
# SPI_PORT   = 0
# SPI_DEVICE = 0
# mcp = Adafruit_MCP3008.MCP3008(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

def setND(val):
    a = 1014
    b = val
    x = (b * 100) / a
    currentAddress = ipAddress2 + "/props/instrumentation/nd?submit=set&range%5B0%5D=" + format(str(x))
    urllib2.urlopen(currentAddress)
    pass

def setThrottle(val):
    a = 1014.0
    b = val
    x = b / a # (value * .1) / 1024
    currentAddress1 = ipAddress2 + "/props/controls/engines/engine[0]?submit=set&throttle[0]=" + format(str(x))
    currentAddress2 = ipAddress2 + "/props/controls/engines/engine[1]?submit=set&throttle[0]=" + format(str(x))
    urllib2.urlopen(currentAddress1)
    urllib2.urlopen(currentAddress2)
    pass

def setFlaps(val):
    x = 0
    if (val < 50):
        x = 0       # FLAPS 0
    if (val > 50 and val < 256):
         x = .14    # FLAPS 5
    if (val > 256 and val < 500):
        x = .428    # FLAPS 15
    if (val > 515):
        x = 1       # FLAPS 35
    #print(val)
    currentAddress = ipAddress2 + "/props/controls/flight?submit=set&flaps[0]=" + format(str(x))
    urllib2.urlopen(currentAddress)
    pass

print('Reading MCP3008 values, press Ctrl-C to quit...')
# Print nice channel column headers.
print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*range(8)))
print('-' * 57)
# Main program loop.
while True:
    # Read all the ADC channel values in a list.
    values = [0]*8
    for i in range(8):
        # The read_adc function will get the value of the specified channel (0-7).
        values[i] = mcp.read_adc(i)
    # Print the ADC values.
    # print('| {0:>4} | {1:>4} | {2:>4} | {3:>4} | {4:>4} | {5:>4} | {6:>4} | {7:>4} |'.format(*values))
    # print(values[0] + values[1])
    setND(values[0])
    setThrottle(values[1])
    setFlaps(values[2])
    print("ND: %s || Throttle: %s || Flaps: %s" % (values[0], values[1], values[2]))
    # Pause for half a second.
    time.sleep(0.1)
