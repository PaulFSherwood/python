# battery
def battery(isBatteryGood):
    if isBatteryGood == True:
        return True
    else:
        return False

# ignition switch
def ignition_switch(isKeyTurned):
    if isKeyTurned == True:
        # isTurnedOn = True
        return True
    else:
        return False

# alternator
def alternator(hasPower, hasGround, isAlternatorGood, isTurnedOn):
    if hasPower == True and hasGround == True and isAlternatorGood == True:
        # Turn on output shaft
        return True
    else:
        return False

# starter solenoid
def starter_solenoid(isIgnitionOn, hasPower):
    if isIgnitionOn == True and hasPower == True:
        # send output to alternator/starter
        return True
    else:
        return False

# starter
def starter(hasPower):
    if hasPower == True:
        # solenoid sent power send output
        return True
    else:
        return False


