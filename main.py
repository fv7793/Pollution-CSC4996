class Parent:
    def __init__(self):
        self.var = 3
    def getVar(self):
        return self.var

class Parent2:
    def __init__(self):
        self.var2 = 6
    def printSomething(self):
        print("something")


class Child(Parent, Parent2):
    def __init__(self):
        self.var = 5


parent = Parent()
print(parent.getVar())

child = Child()
print(child.getVar())
child.printSomething()