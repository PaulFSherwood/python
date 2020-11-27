def checkio(data):
    x = len(data)
    if x > 0:
        count[0] = count[0] + data[x-1]
        data2 = data[0:x-1]
        return checkio(data2)
    else:
        return count[0]

count = [0]

print (checkio([1,2,1,2,1]))
