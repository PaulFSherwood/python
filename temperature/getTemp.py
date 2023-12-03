web_path = "home/pi/sources/Pi_Graph/"
SimBay767 = "SimBay767"
PcRoom767 = "PcRoom767"

import random
import os
import time
import json
import Adafruit_DHT

DHT_TYPE = Adafruit_DHT.AM2303
DHT_PIN = 14    # 767 Sim Bay
DHT_PIN2 = 4    # 767 Computer Room

while True:
# ==================================================
    # Get readings from Sim Bay
    h, t = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
    while t is None or t > 100 or t < 0 or h is None or h > 100 or h < 10:
        h, t = Adafruit_DHT.read(DHT_TYPE, DHT_PIN)
    t = t * 9.0/5.0 + 32
    # Get readings fro Computer Room
    h2, t2 = Adafruit_DHT.read(DHT_TYPE, DHT_PIN2)
    while t2 is None or t2 > 100 or t2 < 0 or h2 is None or h2 > 100 or h2 < 10:
        h2, t2 = Adafruit_DHT.read(DHT_TYPE, DHT_PIN2)
    t2 = t2 * 9.0/5.0 + 32

# ==================================================
#       print("%.2f || %.2f" % (h, t))
#       print("%.2f || %.2f" % (h2, t2))
# ==================================================
    # Store values in dictionary
    data = {'humidity':h, 'temperature':t}
    data2 = {'humidity':h2, 'temperature':t2}

    # Open file and dump data formatted as JSON
    with open(os.path.join(web_path, SimBay767), 'w') as f:
        json.dump(data, f)
    with open(os.path.join(web_path, PcRoom767), 'w') as f:
        json.dump(data2, f)
    time.sleep(5)
    