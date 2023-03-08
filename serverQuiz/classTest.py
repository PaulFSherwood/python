class Parent:
    def __init__(self):
        self.my_var = 0

    def increment_var(self, value):
        self.my_var += value

class Child(Parent):
    def __init__(self):
        super().__init__()

    def modify_var(self):
        self.increment_var(1)

child_obj = Child()
print(child_obj.my_var) # Output: 0

child_obj.modify_var()
print(child_obj.my_var) # Output: 1

child_obj.modify_var()
print(child_obj.my_var) # Output: 2
