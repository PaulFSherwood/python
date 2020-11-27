from array import *

# make array and set it to closed.
doors = ['Closed'] * 100

for y in range(100):
    for x in range(y, 100):
        # Toggle the door
        if doors[x] == 'Opened':
            doors[x] = 'Closed'
        elif doors[x] == 'Closed':
            doors[x] = 'Opened'
    x += 1
print (doors)
