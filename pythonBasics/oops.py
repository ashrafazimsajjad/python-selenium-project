class Calculator():
    num = 100

    def __init__(self,a,b):
        self.firstNum = a
        self.secondNum = b
        print("I am called autometically when object is created")

    def getData(self):
        print("Hello OOPs")

    def Summation(self):
        return self.firstNum + self.secondNum + self.num


obj = Calculator(4, 5)
obj.getData()
print(obj.Summation())

obj1 = Calculator(2, 3)
obj1.getData()
print(obj1.Summation())