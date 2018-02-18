import urllib.request
from bs4 import BeautifulSoup
import math

def getRollDeg():
    
    url = "http://127.0.0.1:5500/props/orientation/roll-deg?value="
    
    usock = urllib.request.urlopen(url)  # open html
    data = usock.read()                 # stuff html into variable
    usock.close()                       # cleanup
    soup = BeautifulSoup(data)          # make a BS object (i think/pretysure)
    
    value = 0
    number = 0
    # trying to hold onto the last number (should be the variable we need)
    # would rather have it pull from the html using the tags, but can't find
    # the right wording to use in BeautifulSoup4
    for link in soup.find_all("input"):
        value = link.get("value")
        # print(value)
    
    # this thing realy doesn't want to be a float do some conversion
    number = float(value)
    isinstance(number, float)
    # shorten to one decimal place
    number = math.floor(number*10)/10
    
    print(number)


getRollDeg()
