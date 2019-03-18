class User : 
    def __init__( self, name="", age=0):
        self.name=name
        self.age=age
    def setName(self, name):
        self.name=name
    def setAge(self, age):
        self.age=age
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    
user=User()