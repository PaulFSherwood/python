
# Libraries
import os
import time

# Local files
from display import *
from deck import *

## Setup
display = Display()
isRunning = True
counter = 1
index = 0
timeout = 60
deckSize = 1074

while isRunning == True:
  print("Index: ", index)
  
  # change display
  display.showThing(tup[index])
  
  
  # upkeep
  time.sleep(1)
  os.system('clear')
  if index >= deckSize:
    index = 0
  else:
    index += 1
    
  # Used to break out of the loop
  counter += 1
  if counter >= timeout:
    isRunning = False  
    
    
    