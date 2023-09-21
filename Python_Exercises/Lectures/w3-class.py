class Test:
    a = 10
    b = 20
    __cvv = 123 #double underscore is used to make your variable private
    #getter and setter (if we want to access a private variable)
    _cvv = 123 #single underscore is used to make your variable protected
    def hello(self):
        print("Hello")

# OUTSIDE OF THE CLASS (CAN ACCESS BECAUSE IT IS PUBLIC BY DEFAULT)   
t1 = Test()
print (t1.a)
print(t1.b)
t1.hello()
# print(t1.__cvv) #will error