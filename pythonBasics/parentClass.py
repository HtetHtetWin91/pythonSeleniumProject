class Calculator:
    num = 100
    def __init__(self,a,b):
        self.firstNumber = a
        self.secondNumber = b
        print("I am now executing as a constructor")

    def getData(self):
        self.firstNumber = 10
        self.secondNumber = 20
        print("I am now executing as a method in class")

    def Summation(self):
        return self.firstNumber + self.secondNumber + self.num

obj = Calculator(2,3)
obj.getData()
print("Parentobj1", obj.Summation())

obj1 = Calculator(4,5)
print("Parentobj2", obj1.Summation())