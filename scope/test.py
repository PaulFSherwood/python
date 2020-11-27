x = 1
print(hex(id(x)) + ":" + str(x) + " Global")
class Foo:
    x = 2
    print(hex(id(x)) + ":" + str(x) + " Class 1")
    def foo():
        x = 3
        print(hex(id(x)) + ":" + str(x) + " Class 1 Def 1")
        class Foo:
            print(hex(id(x)) + ":" + str(x) + " Class 2") # prints 11

Foo.foo()
############################################
print("\n")
############################################
x = 1
print(hex(id(x))+ ":" + str(x) + " Global")
class Foo:
    x = 23
    print(hex(id(x)) + ":" + str(x) + " Class 1")
    def foo():
        x = 3
        b = "bob"
        print(hex(id(x)) + ":" + str(x) + " Class 1 Def 1")
        class Foo:
            x += 10
            print(hex(id(x)) + ":" + str(x) + " Class 2") # prints 11

Foo.foo()
