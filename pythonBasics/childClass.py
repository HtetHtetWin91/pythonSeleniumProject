
from parentClass import Calculator

class childClass(Calculator):
    num2 = 200
    def __init__(self):
        Calculator.__init__(self, 2, 3)
        self.childAttribute = 'I am a child attribute'
        print("I am now executing as a constructor in child class")

    def getCompleteData(self):
        return self.firstNumber + self.secondNumber + self.num + self.num2

obj = childClass()
print("Childobj", obj.getCompleteData())