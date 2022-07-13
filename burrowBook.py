#import library to get date and time
from datetime import datetime

def burrowBooks(name, titles, bookList):
    '''function to burrow books'''
    print("\n\n------------------------Generating notes for books burrowed-----------------------")

    #set intial total to 0
    totalPrice = 0

    #create/openfile for the person who wants to burrow
    burrow = open(name+" burrowed on "+datetime.now().strftime("%m_%d_%Y, %H_%M_%S")+".txt", "w")

    #write to file the name of burrower and time of burrow
    burrow.write("The books burrowed by "+name+" on "+datetime.now().strftime("%m/%d/%Y, %H:%M")+":\n")

    #display similar information to the user
    print(name, "burrowed the following books:")

    #iterate over the titles to add
    for title in titles:

        #iterate over the list of books looking for the tile
        for book in bookList:

            #if title is found
            if title == book.title:

                #get the quantity and convert to int
                quantity = int(book.quantity)

                #if the book is available
                if quantity > 0:
                    #write the tile to file and display to user
                    burrow.write(title+"\n")
                    print(title)

                    #add total price
                    totalPrice += float(book.price)

                    #call the burrow method of book class to decrease the quantity of book 
                    book.burrowBook()

                    #after book burrowed exit out of loop
                    break

                else:
                    #display message if all book are burrowed
                    print("We are out of stock on ", title)

                    #even cannot burrow that book exit out of loop
                    break

    #display info to user
    print("Date and Time of burrow is: "+datetime.now().strftime("%m/%d/%Y, %H:%M"))
    
    #write total price to file and display to user				
    burrow.write("The total price is: Rs."+str(totalPrice)+"\n\n")
    print("The total price is: Rs."+str(totalPrice))

    #closet the file for the burrower
    burrow.close()

    #return the current modified book list
    return bookList
