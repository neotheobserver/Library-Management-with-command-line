class Book():
    '''definition for a book'''

    def __init__(self, title, author, quantity, price):
        '''initializer for a book'''
        self.title = title
        self.author = author
        self.quantity = quantity
        self.price = price

    def burrowBook(self):
        '''if book is burrowed decrease quantity'''
        #convert quantity to integer
        quantity = int(self.quantity)
        #decrease by one
        quantity = quantity - 1
        #assign to the instance variable
        self.quantity = str(quantity)

    def returnBook(self):
        '''if book is returned increase quantity'''
        #convert quantity to integer
        quantity = int(self.quantity)
        #increase by one
        quantity = quantity + 1
        #assign to the instance variable
        self.quantity = str(quantity)

    def writeToFile(self, file):
        '''write a line to given file'''
        file.write(self.title+","+self.author+","+self.quantity+","+self.price)

    def display(self):
        '''display details of the book'''
        print("Title: ", self.title, "------ Author: ", self.author, "------- Quantity: ", self.quantity, "------ Price of each: ", "Rs. "+self.price)
