#### Class

"""
class <class name>:
    def __init__(self, params, ...):
        ...
    def method1(self,  params, ...):
        ...
    def method2(self,  params, ...):
        ...    
"""

class Name:
    def __init__(self, name):
        self.name = name
        print("Initialized!")
    
    def Hello(self):
        print("Hello %s!" % self.name)
    
    def Goodbye(self):
        print("Goodbye %s!" % self.name)

r = Name("David")       # Initialized!
r.Hello()               # Hello David!
r.Goodbye()             # Goodbye David!