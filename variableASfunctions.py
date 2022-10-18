def hello():
    print("Hello")

print(hello)
hi = hello
print(hi)
hi()

def double(x):
    return x*2
def tripple(x):
    return x*3
def quad(x):
    return x*4

d = double
t = tripple
q = quad

myList = [d, t, q]

for i in myList:
    print(i(2))


class numbers:
    def __init__(self):
        self.index = 3
    def setIndex(self, num):
        self.index = num + 100
    def getIndex(self):
        return self.index
# create object and reasign it to a variable
num = numbers()
bacon = num.setIndex
# Show the class object and the variable both working
num.setIndex(3)
print("Set the object index to 3, and call the object.getIndex()")
print(num.getIndex())
# we are using the same object
print("Set the variable index to 3, and call the object.getIndex()")
bacon(5)
print(num.getIndex())
