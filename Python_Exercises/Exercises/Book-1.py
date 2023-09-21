## class book, displaying simple data

# class Book:
#     def __init__(self):
#         self.quantity = 10
#         self.price =  ("$95.00")
#         self.author = ("Huie")
#         self.publication_name = ("Tiramisu")
        
#     def displayData(self):
#         print('Quantity:', self.quantity,'\nPrice:', self.price, '\nAuthor:', self.author, '\nPublised by:', self.publication_name)

# book = Book()
# book.displayData()

#it's more okay to be general (general program), it'll be easier to modify data/smth

class Book:
    def __init__(self, quantity, price, author, publication_name):
        self.quantity = quantity
        self.price = price
        self.author = author 
        self.publication_name = publication_name

    def displayData(self):
        print('Quantity:', self.quantity,'\nPrice:', self.price, '\nAuthor:', self.author, '\nPublised by:', self.publication_name)

book = Book(10, "$95", "Huie", "Tiramisu")
book.displayData()