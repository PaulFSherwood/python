def factorial ( numList, total=0):
    if len(numList) == 1:
        print ("End ", numList[0] + total)
        total = numList[0] + total
        return total
    else:
        total = numList[0] + total
        
        numList.pop(0)
        return factorial(numList, total)

print (factorial([1,3,5]))
print (factorial([1,3,5,1,1,3]))
