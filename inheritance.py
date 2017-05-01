class Parent():
    age = 20
    def print_last_name(self):
        print('sherwood')

class Child(Parent):
    def print_first_name(self):
        print('Paul')
    def setAge(self, tempAge):
        self.age = tempAge

paul = Child()
paul.print_first_name()
paul.print_last_name()
print("Age: %s" % (paul.age))
paul.setAge(36)
print("Age: %s" % (paul.age))
