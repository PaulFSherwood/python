

def super_can_access_sibiling():
    class Root:
        varF = "Root"
        def f(self):
            print("Root.f", self)

    class A(Root):
        varFx = "A"
        def f(self):
            print("A.f", self)
            super().f()

    class B(Root):
        varFx = "B"
        def f(self):
            print("B.f", self)

    class C(A, B):
        varFx = "C"
        def f(self):
            print("C.f", self)
            super().f()


    a = C()
    a.f()
    print([cls.__name__ for cls in C.__mro__])
    print(a.varF)

super_can_access_sibiling()