class Test:
    a = 10
    __b = 20 #error, it is now private

#normal method
    def display(self):
        print('My first class program')

    def addNumbers(self):
        print('Addition is:', self.a+self.b)

#self = current instance of the class. talking about the same class
#[display] and [addNumbers] = the method name in this program

t1= Test()
t1.display() #method
t1.addNumbers() #method