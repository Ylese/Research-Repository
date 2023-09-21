class A:
    def __init__(self, a, b): #there's argument in this method
        self.a = a
        self.b = b

    def addNumber(self):
        print('addition is:', self.a+self.b)

abc = A(10, 30) #nothing will print, still calling the constructor
abc.addNumber()